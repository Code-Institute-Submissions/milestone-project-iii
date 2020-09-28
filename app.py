import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'just-a-thought'
app.config["MONGO_URI"] = 'mongodb+srv://thoughts-thought:thought123@milestone-3.fjn9g.mongodb.net/just-a-thought?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_thoughts')
def get_thoughts():
    return render_template("get_thoughts.html", thoughts=mongo.db.thoughts.find())


@app.route('/add_thought')
def add_thought():
    return render_template("add_thought.html", thoughts=mongo.db.thoughts.find())


@app.route('/insert_thoughts', methods=['POST'])
def insert_thoughts():
    thoughts = mongo.db.thoughts
    thoughts.insert_one(request.form.to_dict())
    return redirect(url_for('get_thoughts'))


@app.route('/edit_thought/<thought_id>')
def edit_thought(thought_id):
    the_thought = mongo.db.thoughts.find_one({"_id": ObjectId(thought_id)})
    return render_template('edit_thought.html', thought=the_thought)


@app.route('/update_thought/<thought_id>', methods=["POST"])
def update_thought(thought_id):
    thoughts = mongo.db.thoughts
    thoughts.update({'_id': ObjectId(thought_id)},
                    {
        'title': request.form.get('title'),
        'content': request.form.get('content'),
        'name': request.form.get('name'),
    })
    return redirect(url_for('get_thoughts'))


if(__name__) == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
