# Textanalyse-Formular: Zählt Wörter und Buchstaben
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def textanalyse():
	result = None
	text = ''
	if request.method == 'POST':
		text = request.form.get('text', '')
		words = len([w for w in text.split() if w.strip()])
		letters = len([c for c in text if c.isalpha()])
		result = {'words': words, 'letters': letters}
	return render_template('textanalyse.html', result=result, text=text)

if __name__ == '__main__':
	app.run(debug=True)
