from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route("/saludo/<nombre>")
def hello(nombre):
    app.logger.info(f"Ruta /saludo/{nombre} fue llamada")
    return f"Hola {nombre} desde Bolivia!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)