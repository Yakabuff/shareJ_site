import json
import os
from marshmallow import Schema
from flask import Flask, render_template,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app._static_folder = 'static'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.abspath(os.path.dirname(__file__))+'.db';
db = SQLAlchemy(app)
import model.Changelog as Changelog

Changelog.db_setup()
from changelog import GitGrabber
#
# GitGrabber.initialRetrival()

@app.route('/changelog/<version>', methods=["GET"])
def returnReleaseDetails(version):

    e = Changelog.getEntry(version)

    return jsonify(
        date=e.date,
        body=e.body,
        version=e.version,
        file = e.release_link,
        id = e.commit_id
    )

@app.route('/changelog/', methods=["GET"])
def returnAllRelease():
    e = Changelog.getAll()

    list = []

    for entry in e:
        dict = {
            "date": entry.date,
            "body": entry.body,
            "version": entry.version,
            "commit_id": entry.commit_id,
            "release_link": entry.release_link
        }
        list.append(dict)

    return jsonify(list)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()





# initial launch, check if db exists
# if db not exist, get all changelog data
#else, check if up to date

#connect webhook. if get post request from github, get new release data and update database

#in / route, get stored changelog data and store in a datastructure (dictionary)