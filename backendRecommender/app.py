from flask import Flask
import json
from Recommender import getRecommendedItems
import databaseCon

app = Flask(__name__)


@app.route("/predictions/<int:uid>", strict_slashes=False)
def predictions(uid):
    return json.dumps(getRecommendedItems(uid), indent=2)


@app.route("/createUser/<string:uid>", strict_slashes=False)
def createUser(uid):
    con = databaseCon.Database()
    return con.insertUser(uid)

@app.route("/getUser/<string:uid>", strict_slashes=False)
def getUser(uid):
    con = databaseCon.Database()
    return json.dumps(con.getUser(uid))


@app.route("/rateItem/<string:recipeName>/<int:ratedValue>/<string:uid>", strict_slashes=False)
def rateItem(recipeName, ratedValue, uid):
    con = databaseCon.Database()
    return con.rateItem(recipeName, ratedValue, uid)


if __name__ == '__main__':
    app.run(debug=True)
