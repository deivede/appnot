from flask import Flask, render_template, request, jsonify, make_response, redirect
from twitterapi import taketts
from dbget import getusr

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/", methods=["POST"])
def button():

    req = request.data

    print(req)

    usr_res = req.decode("utf-8")

    retw = taketts(usr_res)

    res = make_response(jsonify({"nwtt": retw["ntw"]}), 200)

    return res

@app.route("/dbusr", methods=["GET"])
def usr():

    ret = getusr()

    resp = make_response(jsonify({"usr": ret}), 200)

    print(resp)

    return resp



if __name__ == "__main__":
    app.run(debug=True)