from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ["POST"])
def add():
    a = request.form["a"]
    b = request.form["b"]
    c = request.form["c"]
    d = request.form["d"]
    return str(int(a) + int(b) + int(c) + int(d))

if __name__ == "__main__":
    app.run()