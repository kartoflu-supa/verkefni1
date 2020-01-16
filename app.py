from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/sida1')
def sida1():
	return render_template("sida1.html")

@app.route('/sida2')
def sida2():
	return render_template("http.html")

if __name__ == "__main__":
	app.run(debug=True)