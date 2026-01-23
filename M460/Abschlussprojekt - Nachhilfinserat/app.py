from flask import Flask, render_template, request, redirect, url_for, abort, session
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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']
        user = User.query.filter_by(name=name, password=password).first()
        if not name or not password:
            abort(404)
        if user:
            session['user_id'] = user.id
            return redirect(url_for('main'))
        else:
            new_user = User(name=name, password=password)
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return redirect(url_for('main'))
    return render_template("login.html")

@app.route("/main", methods=["GET"])
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
    return render_template("admin.html")

@app.route("/create_inserat", methods=["GET", "POST"])
def create_inserat():
    if not session.get('user_id'):
        return redirect(url_for('login'))
    if request.method == "POST":
        subject = request.form['subject']
        description = request.form['description']
        price_per_hour = request.form['price_per_hour']
        if not subject or not description or not price_per_hour:
            abort(404)
        new_inserat = NachhilfeInserat(
            subject=subject,
            description=description,
            price_per_hour=float(price_per_hour),
            user_id=session['user_id']
        )
        db.session.add(new_inserat)
        db.session.commit()
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
    return redirect(url_for('main'))

@app.route("/edit_inserat/<int:inserat_id>", methods=["GET", "POST"])
def edit_inserat(inserat_id):
    if not session.get('user_id'):
        return redirect(url_for('login'))
    inserat = NachhilfeInserat.query.get_or_404(inserat_id)
    if inserat.user_id != session['user_id']:
        abort(403)
    if request.method == "POST":
        inserat.subject = request.form['subject']
        inserat.description = request.form['description']
        inserat.price_per_hour = float(request.form['price_per_hour'])
        db.session.commit()
        return redirect(url_for('main'))
    return render_template("edit_inserat.html", inserat=inserat)

