import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'just-a-thought'
app.config["MONGO_URI"] = 'mongodb+srv://thoughts-thought:thought123@milestone-3.fjn9g.mongodb.net/just-a-thought?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/add_thought')
def add_thought():
    return render_template("add_thought.html", thoughts = mongo.db.thoughts.find())


if(__name__) == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
