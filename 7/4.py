from flask import Flask, request

app = Flask(__name__)

@app.route("/planet-details", methods=["GET"])
def save():
    json = request.get_json("https://swapi.co/api/planets/?format=json&search={}".format(request.args.get("planet")))
    return json


app.run(debug=True)
