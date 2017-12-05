from flask import Flask, request

app = Flask(__name__)

@app.route("/current-status", methods=["GET","POST"])
def save():
    fdgds=""
    if request.method=="GET":
        return "{}".format(fdgds)
    if request.method=="POST":
        fdgds = request.get_json()["status"]
        return fdgds


app.run(debug=True)
