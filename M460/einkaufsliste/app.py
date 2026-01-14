from flask import Flask, redirect, render_template, request, session, url_for, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'gskjd%hsgd82jsd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///einkaeufe.db'
db = SQLAlchemy()
db.init_app(app)


class ShoppingItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)


@app.route('/', methods=('GET', 'POST'))
def home():
    message = ""
    number = ""
    description = ""
    if request.method == 'POST':
        number = request.form["number"]
        description = request.form["description"]
        if not number.isnumeric():
            message = "Bitte geben Sie bei Anzahl eine Zahl ein."
        if not description:
            message = "Bitte geben Sie bei der Beschreibung einen Text ein."
        if not message:
            shopping_item = ShoppingItem(number=number, description=description)
            db.session.add(shopping_item)
            db.session.commit()
            number = ""
            description = ""
            message = "Ihr Einkauf wurde der Liste hinzugefügt."
    groceries = db.session.execute(
        db.select(ShoppingItem).order_by(ShoppingItem.description)
    ).scalars()
    return render_template(
        'index.html',
        groceries=groceries,
        message=message,
        number=number,
        description=description
    )

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    grocery = ShoppingItem.query.filter_by(id=id).first()
    if not grocery:
        abort(404)
    db.session.delete(grocery)
    db.session.commit()
    return redirect(url_for('home'))