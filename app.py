from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Kubernetes!"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/metrics")
def metrics():
    return f"random_metric {random.randint(1, 100)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
