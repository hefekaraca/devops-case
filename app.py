from flask import Flask, request, jsonify

app = Flask(__name__)

# GET /
@app.route("/", methods=["GET"])
def root():
    return jsonify({"msg": "BC4M"})

# GET /health
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

# POST /
@app.route("/", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)

