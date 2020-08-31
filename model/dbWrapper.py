import os

from flask_sqlalchemy import SQLAlchemy

from changelog import Entry
from model import Changelog;
from app.app import app





basedir = os.path.abspath(os.path.dirname(__file__));
db = SQLAlchemy(app)

@staticmethod
def addEntry(e) -> None:
    ins = db.insert(e)

@staticmethod
def first_init()->None:
    db.create_all()

@staticmethod
def remEntry() -> None:

    return None

@staticmethod
def updateEntry() -> None:
    return None

def db_setup():
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def getEntry(version) -> Entry:
    entry = Changelog.query.filter_by(version = version).first()

    return Entry(entry.date, entry.body, entry.version, entry.commit_id, entry.release_link)