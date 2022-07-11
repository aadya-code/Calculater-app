from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")

def main():
	return render_template("index.html")
	@app.route('/', methords=['POST'])
	
def math_operations():
	equation=request.form['text']
	operation=request.form['operation']
	result./li>'https://newton.vercel.app/api/v2'+operation+'/'+equation
	requests.get(result).json()
	