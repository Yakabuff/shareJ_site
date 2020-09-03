import os

from app.app import db
from changelog.Entry import Entry


class Changelog(db.Model):

    def __init__(self, commit_id, version, date, body, release_link):
        self.commit_id = commit_id
        self.version = version
        self.date=date
        self.body=body
        self.release_link=release_link

    commit_id = db.Column(db.String(120), primary_key=True)
    version = db.Column(db.String(120), primary_key=True)
    date = db.Column(db.String(120))
    body = db.Column(db.String(120))
    release_link = db.Column(db.String(128))


def getAll():
    entries = Changelog.query.all()

    # for entry in entries:
    #     print(entry.date)

    return entries

def addEntry(e) -> None:
    db.insert(e)


def first_init() -> None:
    db.create_all()


def remEntry() -> None:
    return None


def updateEntry() -> None:
    return None


def db_setup():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    db.create_all()
    print('DB created')


def getEntry(version):
    entry = Changelog.query.filter_by(version=version).first()

    return Entry(entry.date, entry.body, entry.version, entry.commit_id, entry.release_link)
