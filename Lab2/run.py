from flask import Flask,render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		# print request.form.get('led')
		# print request.form['led'].strip()
		if (request.form.get('led')=="on"):
			print "LED On"
		else :
			print "LED Off"
		return render_template('index.html')
	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
