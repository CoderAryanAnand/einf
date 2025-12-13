from flask import Flask, render_template, request
import os
root_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=os.path.join(root_dir, 'templates'))

print("Root directory is:", root_dir)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/hi/<name>')
def hi(name):
    return render_template('hi.html', title="Hallo Homepage", username=name)

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    result = None
    if request.method == 'POST':
        num1 = request.form.get('num1', type=float)
        num2 = request.form.get('num2', type=float)
        operation = request.form.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
        else:
            result = 'Invalid operation'

        return render_template('adder.html', title="Calculator Page", result=result, num1=num1, num2=num2, operation=operation)
    return render_template('adder.html', title="Calculator Page", result=result)


@app.route('/color_picker', methods=['GET', 'POST'])
def color_picker():
    selected_color = None
    red = green = blue = None
    if request.method == 'POST':
        selected_color = request.form.get('color')
        red = request.form.get('red')
        green = request.form.get('green')
        blue = request.form.get('blue')
        print(f"Color received: {selected_color} (RGB: {red}, {green}, {blue})")
    return render_template('color_picker.html', selected_color=selected_color, red=red, green=green, blue=blue)


if __name__ == '__main__':
    app.run(debug=True)