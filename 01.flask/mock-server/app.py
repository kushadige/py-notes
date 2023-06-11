from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods = ["POST"])
def hello():
    print(request.json)
    return jsonify({"message": "hi from mock-server"})

if __name__ == "__main__":
    app.run(debug = True)