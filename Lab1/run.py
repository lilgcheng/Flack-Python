from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/whoami')
def whoami():
	user = { 'name':'Cheng'}
	posts = [
		{
		'author': {'authorname': 'John'},
		},
		{
		'author': {'authorname': 'Ming'},
		}
	]
	return render_template('whoami.html'
		,user =user
		,posts = posts)

@app.route('/base')
def base():
	user = { 'name':'Ming'}
	posts = [
		{
		'author': {'authorname': 'Harry'},
		},
		{
		'author': {'authorname': 'Lealy'},
		}
	]
	return render_template('extendsbase.html'
		,user =user
		,posts = posts)

if __name__ == '__main__':
	app.run(debug=True)
