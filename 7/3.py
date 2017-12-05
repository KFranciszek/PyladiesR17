from flask import Flask, request

app = Flask(__name__)

@app.route("/user/<username>/set-password", methods=["POST"])
def save(username):
    global db
    db={}
    if request.method=="POST":
        passwd = request.get_json()["passwd"]
        db.update({username: passwd})
        return "Hasło u/{} zostało zmienione na {}".format(username, passwd)
@app.route("/user/<username>/login", methods=["POST"])
def login(username):
    if request.method=="POST":
        passwdl = request.get_json()["passwd"]
        if username in db:
            if passwdl == db[username]:
                return "Login successful"
            else:
                return "Wrong password or username"
        else:
            return "Wrong username or password"



app.run(debug=True)