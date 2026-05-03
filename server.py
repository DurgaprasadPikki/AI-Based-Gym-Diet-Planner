from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/exp")
def exp():
    return 

("exp.html")

@app.route("/diet1")
def diet1():
    return render_template("diet1.html")
@app.route("/diet2")
def diet2():
    return render_template("diet2.html")
@app.route("/diet3")
def diet3():
    return render_template("diet3.html")

if __name__ == "__main__":
    app.run(debug=True)