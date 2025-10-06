from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route("/saludo")
def hello():
    app.logger.debug("Ruta Saludo fue llamada")
    return "Hola desde Bolivia!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)