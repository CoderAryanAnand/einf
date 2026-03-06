# Flask-Imports: Funktionen für Webserver, Templates, Requests, Weiterleitungen, Fehler, Session und Flash-Nachrichten
from flask import Flask, render_template, request, redirect, url_for, abort, session, flash
# SQLAlchemy ist ein ORM (Object Relational Mapper) – damit kann man mit Python-Klassen auf die Datenbank zugreifen
from flask_sqlalchemy import SQLAlchemy

# Flask-App erstellen
app = Flask(__name__)
# Datenbank-Pfad: SQLite-Datei im instance-Ordner
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nachhilfe.db'
# Secret Key wird für die Session-Verschlüsselung (Cookies) benötigt
app.config['SECRET_KEY'] = 'super_safe_trust_me'
# Datenbank-Objekt erstellen und mit der App verbinden
db = SQLAlchemy(app)


# ==================== MODELS (Datenmodell) ====================

# User-Tabelle: speichert Benutzername und Passwort
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)          # Eindeutige ID, wird automatisch hochgezählt
    name = db.Column(db.String(100), unique=True, nullable=False)  # Benutzername, muss einzigartig sein
    password = db.Column(db.String(100), nullable=False)   # Passwort (Klartext – in Produktion würde man hashen)

# NachhilfeInserat-Tabelle: speichert die Inserate
# 1:n-Beziehung: Ein User kann viele Inserate haben (über user_id als ForeignKey)
class NachhilfeInserat(db.Model):
    id = db.Column(db.Integer, primary_key=True)           # Eindeutige ID
    subject = db.Column(db.String(100), nullable=False)    # Fach (z.B. "Mathematik")
    description = db.Column(db.Text, nullable=False)       # Beschreibung des Angebots
    price_per_hour = db.Column(db.Float, nullable=False)   # Preis pro Stunde
    contact_info = db.Column(db.String(100), nullable=True) # Kontaktinfo (optional)
    # ForeignKey: Verknüpfung zur User-Tabelle – jedes Inserat gehört einem User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# ==================== CONTROLLER (Routen / Logik) ====================

# --- LOGIN & REGISTRIERUNG ---
# Route für Login-Seite, akzeptiert GET (Seite anzeigen) und POST (Formular absenden)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Formulardaten auslesen und Leerzeichen am Rand entfernen
        name = request.form['username'].strip()
        password = request.form['password'].strip()

        # Validierung: Felder dürfen nicht leer sein
        if not name or not password:
            flash('Benutzername und Passwort dürfen nicht leer sein.', 'error')
            return render_template("login.html")

        # Prüfen ob ein User mit diesem Namen bereits existiert
        existing_user = User.query.filter_by(name=name).first()

        if existing_user:
            # User existiert → Passwort prüfen
            if existing_user.password == password:
                # Passwort stimmt → User-ID in der Session speichern (= eingeloggt)
                session['user_id'] = existing_user.id
                return redirect(url_for('main'))
            else:
                # Passwort falsch → Fehlermeldung
                flash('Falsches Passwort.', 'error')
                return render_template("login.html")
        else:
            # User existiert nicht → neues Konto erstellen (Registrierung)
            new_user = User(name=name, password=password)
            db.session.add(new_user)    # Neuen User zur Datenbank hinzufügen
            db.session.commit()         # Änderungen in der Datenbank speichern
            session['user_id'] = new_user.id  # Direkt einloggen
            flash('Konto erfolgreich erstellt!', 'success')
            return redirect(url_for('main'))

    # GET-Request: Login-Seite anzeigen
    return render_template("login.html")


# --- HAUPTSEITE (READ: alle Inserate anzeigen + Suche/Filter) ---
@app.route("/", methods=["GET"])
def main():
    # Wenn nicht eingeloggt → zur Login-Seite weiterleiten
    if not session.get('user_id'):
        return redirect(url_for('login'))

    # URL-Parameter auslesen (z.B. /?search=Mathe&max_price=30&sort=price_asc)
    search = request.args.get('search', '').strip()       # Suchbegriff
    max_price = request.args.get('max_price', '').strip()  # Maximaler Preis
    sort = request.args.get('sort', 'newest')              # Sortierung (Standard: neueste zuerst)

    # Basis-Query: alle Inserate
    query = NachhilfeInserat.query

    # Filter: Suchbegriff in Fach ODER Beschreibung (ilike = case-insensitive)
    if search:
        query = query.filter(
            db.or_(
                NachhilfeInserat.subject.ilike(f'%{search}%'),
                NachhilfeInserat.description.ilike(f'%{search}%')
            )
        )

    # Filter: nur Inserate mit Preis <= max_price
    if max_price:
        try:
            query = query.filter(NachhilfeInserat.price_per_hour <= float(max_price))
        except ValueError:
            pass  # Ungültiger Preis wird ignoriert

    # Sortierung anwenden
    if sort == 'price_asc':
        query = query.order_by(NachhilfeInserat.price_per_hour.asc())   # Preis aufsteigend
    elif sort == 'price_desc':
        query = query.order_by(NachhilfeInserat.price_per_hour.desc())  # Preis absteigend
    else:
        query = query.order_by(NachhilfeInserat.id.desc())              # Neueste zuerst (höchste ID)

    # Query ausführen und alle Ergebnisse holen
    inserate = query.all()
    # Template rendern und Variablen übergeben (für die Anzeige und Filter-Persistence)
    return render_template("main.html", inserate=inserate, search=search, max_price=max_price, sort=sort)


# --- LOGOUT ---
@app.route("/logout", methods=["GET"])
def logout():
    # User-ID aus der Session entfernen (= ausloggen)
    session.pop('user_id', None)
    return redirect(url_for('login'))


# --- ADMIN PANEL (nur für User mit ID 1) ---
@app.route("/admin", methods=["GET"])
def admin():
    if not session.get('user_id'):
        return redirect(url_for('login'))
    # Nur User mit ID 1 darf auf Admin zugreifen, sonst 403 Forbidden
    if not (session['user_id'] == 1):
        abort(403)
    # Alle User aus der Datenbank laden und an Template übergeben
    users = User.query.all()
    return render_template("admin.html", users=users)


# --- CREATE: Neues Inserat erstellen ---
@app.route("/create_inserat", methods=["GET", "POST"])
def create_inserat():
    if not session.get('user_id'):
        return redirect(url_for('login'))

    if request.method == "POST":
        # Formulardaten auslesen
        subject = request.form['subject'].strip()
        description = request.form['description'].strip()
        price_per_hour = request.form['price_per_hour'].strip()
        contact_info = request.form['contact_info'].strip()

        # Validierung: Pflichtfelder prüfen
        if not subject or not description or not price_per_hour:
            flash('Fach, Beschreibung und Preis sind Pflichtfelder.', 'error')
            return render_template("create_inserat.html")

        # Preis validieren: muss eine positive Zahl sein
        try:
            price = float(price_per_hour)
            if price <= 0:
                flash('Der Preis muss grösser als 0 sein.', 'error')
                return render_template("create_inserat.html")
        except ValueError:
            flash('Bitte einen gültigen Preis eingeben.', 'error')
            return render_template("create_inserat.html")

        # Neues Inserat-Objekt erstellen mit den Formulardaten
        new_inserat = NachhilfeInserat(
            subject=subject,
            description=description,
            price_per_hour=price,
            contact_info=contact_info,
            user_id=session['user_id']  # Aktuell eingeloggter User wird als Ersteller gespeichert
        )
        db.session.add(new_inserat)  # In DB einfügen
        db.session.commit()          # Speichern
        flash('Inserat erfolgreich erstellt!', 'success')
        return redirect(url_for('main'))

    # GET-Request: Formular anzeigen
    return render_template("create_inserat.html")


# --- DELETE: Inserat löschen ---
# URL-Parameter <int:inserat_id> wird aus der URL extrahiert (z.B. /delete_inserat/3)
# Nur POST erlaubt, damit man nicht per Link versehentlich löschen kann
@app.route("/delete_inserat/<int:inserat_id>", methods=["POST"])
def delete_inserat(inserat_id):
    if not session.get('user_id'):
        return redirect(url_for('login'))
    # Inserat aus DB laden, oder 404-Fehler wenn es nicht existiert
    inserat = NachhilfeInserat.query.get_or_404(inserat_id)
    # Nur der Ersteller darf sein eigenes Inserat löschen
    if inserat.user_id != session['user_id']:
        abort(403)  # 403 = Forbidden (keine Berechtigung)
    db.session.delete(inserat)  # Aus DB entfernen
    db.session.commit()         # Speichern
    flash('Inserat gelöscht.', 'success')
    return redirect(url_for('main'))


# --- UPDATE: Inserat bearbeiten ---
@app.route("/edit_inserat/<int:inserat_id>", methods=["GET", "POST"])
def edit_inserat(inserat_id):
    if not session.get('user_id'):
        return redirect(url_for('login'))
    inserat = NachhilfeInserat.query.get_or_404(inserat_id)
    # Nur der Ersteller darf sein eigenes Inserat bearbeiten
    if inserat.user_id != session['user_id']:
        abort(403)

    if request.method == "POST":
        subject = request.form['subject'].strip()
        description = request.form['description'].strip()
        price_per_hour = request.form['price_per_hour'].strip()
        contact_info = request.form['contact_info'].strip()

        # Gleiche Validierung wie beim Erstellen
        if not subject or not description or not price_per_hour:
            flash('Fach, Beschreibung und Preis sind Pflichtfelder.', 'error')
            return render_template("edit_inserat.html", inserat=inserat)
        try:
            price = float(price_per_hour)
            if price <= 0:
                flash('Der Preis muss grösser als 0 sein.', 'error')
                return render_template("edit_inserat.html", inserat=inserat)
        except ValueError:
            flash('Bitte einen gültigen Preis eingeben.', 'error')
            return render_template("edit_inserat.html", inserat=inserat)

        # Bestehende Felder aktualisieren (kein neues Objekt, sondern Update)
        inserat.subject = subject
        inserat.description = description
        inserat.price_per_hour = price
        inserat.contact_info = contact_info
        db.session.commit()  # Änderungen speichern (UPDATE statt INSERT)
        flash('Inserat erfolgreich aktualisiert!', 'success')
        return redirect(url_for('main'))

    # GET-Request: Formular mit aktuellen Werten anzeigen
    return render_template("edit_inserat.html", inserat=inserat)


# --- DELETE: Benutzer löschen (nur Admin) ---
@app.route("/delete_user/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    if not session.get('user_id'):
        return redirect(url_for('login'))
    if not (session['user_id'] == 1):
        abort(403)
    user = User.query.get_or_404(user_id)
    # Admin (ID 1) darf nicht sich selbst löschen
    if user.id != 1:
        db.session.delete(user)
        db.session.commit()
        flash('Benutzer gelöscht.', 'success')
        return redirect(url_for('admin'))
    flash('Der Admin-Benutzer kann nicht gelöscht werden.', 'error')
    return redirect(url_for('admin'))


# --- UPDATE: Benutzer bearbeiten (nur Admin) ---
@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if not session.get('user_id'):
        return redirect(url_for('login'))
    if not (session['user_id'] == 1):
        abort(403)
    user = User.query.get_or_404(user_id)

    if request.method == "POST":
        new_name = request.form['name'].strip()

        # Validierung: Name darf nicht leer sein
        if not new_name:
            flash('Der Name darf nicht leer sein.', 'error')
            return render_template("edit_user.html", user=user)

        # Prüfen ob der neue Name schon von einem anderen User verwendet wird
        existing = User.query.filter_by(name=new_name).first()
        if existing and existing.id != user.id:
            flash('Dieser Benutzername ist bereits vergeben.', 'error')
            return render_template("edit_user.html", user=user)

        user.name = new_name
        db.session.commit()
        flash('Benutzer erfolgreich aktualisiert!', 'success')
        return redirect(url_for('admin'))

    return render_template("edit_user.html", user=user)