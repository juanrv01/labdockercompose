from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/api", methods=["GET"])
def my_service():
    return jsonify({"message": "Hola desde el servicio de Juan Sebastian H."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
