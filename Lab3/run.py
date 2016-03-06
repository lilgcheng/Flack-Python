from flask import Flask,render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		# print request.form.get('led')
		# print request.form['led'].strip()
		print "x1 = "+request.form.get('x1'),
		print "y1 = "+request.form.get('y1'),
		print "x2 = "+request.form.get('x2'),
		print "y2 = "+request.form.get('y2'),
		print "w = "+request.form.get('w'),
		print "h = "+request.form.get('h')
		return render_template('index.html')
	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
