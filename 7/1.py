from flask import Flask

app = Flask(__name__)

@app.route("/add/<value_one>/<value_two>")
def add(value_one, value_two):
    return "To jest równe {}".format(int(value_one)+int(value_two))

app.run(debug=True)
