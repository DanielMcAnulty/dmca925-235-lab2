from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("page.html")


@app.route('/<name>')
def hello_name(name):
    return f"Hello {name}, wassup biitch??"


if __name__ == '__main__':
    app.run(debug=True)
