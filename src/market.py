from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Namaste India</h1>"


@app.route('/about')
def about():
    return "About us"
if __name__ == "__main__":
    app.run(debug=True)