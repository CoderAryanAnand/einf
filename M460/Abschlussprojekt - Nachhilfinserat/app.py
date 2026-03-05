from flask import Flask, render_template, request, redirect, url_for, abort, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nachhilfe.db'
app.config['SECRET_KEY'] = 'super_safe_trust_me'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class NachhilfeInserat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price_per_hour = db.Column(db.Float, nullable=False)
    contact_info = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form['username'].strip()
        password = request.form['password'].strip()
        if not name or not password:
            flash('Benutzername und Passwort dürfen nicht leer sein.', 'error')
            return render_template("login.html")
        existing_user = User.query.filter_by(name=name).first()
        if existing_user:
            if existing_user.password == password:
                session['user_id'] = existing_user.id
                return redirect(url_for('main'))
            else:
                flash('Falsches Passwort.', 'error')
                return render_template("login.html")
        else:
            new_user = User(name=name, password=password)
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            flash('Konto erfolgreich erstellt!', 'success')
            return redirect(url_for('main'))
    return render_template("login.html")

@app.route("/", methods=["GET"])
def main():
    if not session.get('user_id'):
        return redirect(url_for('login'))
    inserate = NachhilfeInserat.query.all()
    return render_template("main.html", inserate=inserate)

@app.route("/logout", methods=["GET"])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route("/admin", methods=["GET"])
def admin():
    if not session.get('user_id'):
        return redirect(url_for('login'))
    if not (session['user_id'] == 1):
        abort(403)
    users = User.query.all()
    return render_template("admin.html", users=users)

@app.route("/create_inserat", methods=["GET", "POST"])
def create_inserat():
    if not session.get('user_id'):
        return redirect(url_for('login'))
    if request.method == "POST":
        subject = request.form['subject'].strip()
        description = request.form['description'].strip()
        price_per_hour = request.form['price_per_hour'].strip()
        contact_info = request.form['contact_info'].strip()
        if not subject or not description or not price_per_hour:
            flash('Fach, Beschreibung und Preis sind Pflichtfelder.', 'error')
            return render_template("create_inserat.html")
        try:
            price = float(price_per_hour)
            if price <= 0:
                flash('Der Preis muss grösser als 0 sein.', 'error')
                return render_template("create_inserat.html")
        except ValueError:
            flash('Bitte einen gültigen Preis eingeben.', 'error')
            return render_template("create_inserat.html")
        new_inserat = NachhilfeInserat(
            subject=subject,
            description=description,
            price_per_hour=price,
            contact_info=contact_info,
            user_id=session['user_id']
        )
        db.session.add(new_inserat)
        db.session.commit()
        flash('Inserat erfolgreich erstellt!', 'success')
        return redirect(url_for('main'))
    return render_template("create_inserat.html")

@app.route("/delete_inserat/<int:inserat_id>", methods=["POST"])
def delete_inserat(inserat_id):
    if not session.get('user_id'):
        return redirect(url_for('login'))
    inserat = NachhilfeInserat.query.get_or_404(inserat_id)
    if inserat.user_id != session['user_id']:
        abort(403)
    db.session.delete(inserat)
    db.session.commit()
    flash('Inserat gelöscht.', 'success')
    return redirect(url_for('main'))

@app.route("/edit_inserat/<int:inserat_id>", methods=["GET", "POST"])
def edit_inserat(inserat_id):
    if not session.get('user_id'):
        return redirect(url_for('login'))
    inserat = NachhilfeInserat.query.get_or_404(inserat_id)
    if inserat.user_id != session['user_id']:
        abort(403)
    if request.method == "POST":
        subject = request.form['subject'].strip()
        description = request.form['description'].strip()
        price_per_hour = request.form['price_per_hour'].strip()
        contact_info = request.form['contact_info'].strip()
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
        inserat.subject = subject
        inserat.description = description
        inserat.price_per_hour = price
        inserat.contact_info = contact_info
        db.session.commit()
        flash('Inserat erfolgreich aktualisiert!', 'success')
        return redirect(url_for('main'))
    return render_template("edit_inserat.html", inserat=inserat)

@app.route("/delete_user/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    if not session.get('user_id'):
        return redirect(url_for('login'))
    if not (session['user_id'] == 1):
        abort(403)
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('Benutzer gelöscht.', 'success')
    return redirect(url_for('admin'))


@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if not session.get('user_id'):
        return redirect(url_for('login'))
    if not (session['user_id'] == 1):
        abort(403)
    user = User.query.get_or_404(user_id)
    if request.method == "POST":
        new_name = request.form['name'].strip()
        if not new_name:
            flash('Der Name darf nicht leer sein.', 'error')
            return render_template("edit_user.html", user=user)
        existing = User.query.filter_by(name=new_name).first()
        if existing and existing.id != user.id:
            flash('Dieser Benutzername ist bereits vergeben.', 'error')
            return render_template("edit_user.html", user=user)
        user.name = new_name
        db.session.commit()
        flash('Benutzer erfolgreich aktualisiert!', 'success')
        return redirect(url_for('admin'))
    return render_template("edit_user.html", user=user)