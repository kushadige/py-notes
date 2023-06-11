from flask import Flask, request, jsonify
from threading import Thread

from script import wait_process

app = Flask(__name__)

thread_value = []
@app.route("/", methods = ['POST'])
def hello():
    contract_data = request.json
    Thread(target=wait_process, args=([contract_data, thread_value])).start()
    return jsonify({"status": 200, "message": "talebini aldım"}), 200

if __name__ == "__main__":
    app.run(debug=True)