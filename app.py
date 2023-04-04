from flask import Flask

app = Flask(__name__)

@app.route("/")
def happy_ghw():
    return "<p>Happy, ghw to me!</p>"

if __name__ == "__main__":
    app.run(debug = True)