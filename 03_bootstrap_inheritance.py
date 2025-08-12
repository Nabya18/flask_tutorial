from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("new.html")

if __name__ == '__main__':
    app.run(debug=True)