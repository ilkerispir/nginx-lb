from flask import Flask, jsonify
import uuid

app = Flask(__name__)

id = uuid.uuid4()

@app.route("/")
def hello_world():
    return {
        "id": id
    }

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)