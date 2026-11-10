
from flask import Flask, jsonify
from pymongo import MongoClient
from pymongo.errors import PyMongoError
import os

app = Flask(__name__)


MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
MONGO_PORT = int(os.getenv("MONGO_PORT", "27017"))
MONGO_USER = os.getenv("MONGO_USER", "admin")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "password123")

client = MongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    username=MONGO_USER,
    password=MONGO_PASSWORD,
    authSource="admin",
    serverSelectionTimeoutMS=5000
)

db = client["ma_base"]

@app.route("/")
def home():
    return "Bienvenue dans mon application Flask avec Docker et MongoDB !"

@app.route("/db-check")
def db_check():
    try:
        client.admin.command("ping")
        return jsonify({
            "status": "success",
            "message": "Connexion à MongoDB réussie !",
            "database": "ma_base"
        })
    except PyMongoError as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
