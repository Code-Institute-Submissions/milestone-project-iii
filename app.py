import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)


mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html", thoughts=mongo.db.thoughts.find())


@app.route('/add_thought')
def add_thought():
    return render_template("add_thought.html", thoughts=mongo.db.thoughts.find())


@app.route('/insert_thoughts', methods=['POST'])
def insert_thoughts():
    thoughts = mongo.db.thoughts
    thoughts.insert_one(request.form.to_dict())
    return redirect(url_for('index'))


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
    return redirect(url_for('index'))


@app.route('/delete_thought/<thought_id>')
def delete_thought(thought_id):
    mongo.db.thoughts.remove({'_id': ObjectId(thought_id)})
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')


if(__name__) == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
