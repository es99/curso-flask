from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/sobre')
def sobre():
    return "<p>Este é o melhor app de delivery</p>"

if __name__ == "__main__":
    app.run(debug=True)