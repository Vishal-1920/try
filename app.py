from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
@app.route("/new")
def new():
    return render_template('new.html') 
app.run()       
