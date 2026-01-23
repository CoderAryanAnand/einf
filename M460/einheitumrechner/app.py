"""
Flask app, where on the home page users can enter a number and select two units from a dropdown, and upon submission, the app converts the number from the first unit to the second unit and displays the result.
Admin page, where an admin can add, update, or delete units and their conversion rates. If for example m to km is added, km to m should not have to be added separately, the app should handle the reverse conversion automatically.

"""

from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///units.db'
db = SQLAlchemy(app)

class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name1 = db.Column(db.String(50), nullable=False)  # e.g. 'km'
    name2 = db.Column(db.String(50), nullable=False)  # e.g. 'm'
    rate = db.Column(db.Float, nullable=False)  # e.g. 1 km = rate * m
    # rate: how many name2 in 1 name1 (e.g. 1 km = 1000 m, rate=1000)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    units = Unit.query.all()
    # Build a flat list of all unique unit names
    unit_names = set()
    for u in units:
        unit_names.add(u.name1)
        unit_names.add(u.name2)
    unit_names = sorted(unit_names)

    if request.method == 'POST':
        number = float(request.form['number'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        if from_unit == to_unit:
            result = number
        else:
            direct = Unit.query.filter_by(name1=from_unit, name2=to_unit).first()
            if direct:
                result = number * direct.rate
            else:
                reverse = Unit.query.filter_by(name1=to_unit, name2=from_unit).first()
                if reverse:
                    result = number / reverse.rate
                else:
                    result = f"No conversion found between {from_unit} and {to_unit}."

    return render_template('index.html', units=unit_names, result=result)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name1 = request.form['name1']
        name2 = request.form['name2']
        rate = float(request.form['rate'])

        new_unit = Unit(name1=name1, name2=name2, rate=rate)
        db.session.add(new_unit)
        db.session.commit()
        return redirect(url_for('admin'))

    units = Unit.query.all()
    return render_template('admin.html', units=units)