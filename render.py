from flask import Flask, render_template, request, jsonify, make_response, redirect
from twitterapi import taketts

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def button():

    retw = taketts()

    req = request.get_json()

    print(req)

    res = make_response(jsonify({"nwtt": retw}), 200)

    return res

if __name__ == "__main__":
    app.run(debug=True)