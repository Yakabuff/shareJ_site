from flask import Blueprint

entry = Blueprint('entry', 'entry')

@entry.route('/changelog/<int:version>', methods=["GET"])
def getEntry():
    return None