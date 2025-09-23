from flask import Flask, render_template, request

app = Flask(__name__)

userList = [
    {"id": "001", "name": "刘德华", "num": 0},
    {"id": "002", "name": "陈小春", "num": 0},
    {"id": "003", "name": "左小青", "num": 0},
    {"id": "004", "name": "贾静雯", "num": 0},
]


@app.route("/")
def index():
    return render_template("index.html", userList=userList)


@app.route("/dianzan")
def dianzan():
    idStr = request.args.get("id")
    for user in userList:
        if user["id"] == idStr:
            user["num"] += 1
            break
    return render_template("index.html", userList=userList)


app.run(debug=True)
