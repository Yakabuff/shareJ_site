from model.dbWrapper import db


class Changelog(db.model):
    commit_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.dateTime())
    body = db.Column(db.String(120))
    release_link = db.Column(db.String(128))