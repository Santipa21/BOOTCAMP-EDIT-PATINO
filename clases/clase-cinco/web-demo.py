from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Hola, Mundo EDIT!"

@app.route("/secreto")
def secreto():
    return "¡Este es un mensaje secreto! TE AMO"

if __name__ == "__main__":
    app.run(debug=True)