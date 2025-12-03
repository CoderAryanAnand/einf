from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return 'Hello, Flask!'

@app.route('/add/<int:num1>/<int:num2>')
def add_numbers(num1, num2):
    result = num1 + num2
    return f"Das Resultat von {num1} + {num2} ist {result}"

if __name__ == '__main__':
    app.run(debug=True)