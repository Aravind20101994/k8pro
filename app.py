from flask import Flask, render_template, redirect, url_for 

app = Flask(__name__) 


@app.route("/") 
def home(): 
	return render_template("index.html") 


@app.route("/default") 
def default(): 
	return render_template("layout.html") 


@app.route("/variable") 
def var(): 
	user = "Geeksforgeeks"
	return render_template("variable_example.html", name=user) 

