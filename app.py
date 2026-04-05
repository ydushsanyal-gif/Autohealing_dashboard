from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/optimizer")
def optimizer():
    return render_template("optimizer.html")

@app.route("/healing")
def healing():
    return render_template("healing.html")

@app.route("/reports")
def reports():
    return render_template("reports.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)