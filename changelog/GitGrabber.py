from github import Github
from app import settings
from model import Changelog
from model.dbWrapper import db


def initialRetrival():


    g = Github(settings.GITHUB_KEY)
    repo = g.get_repo("yakabuff/shareJ")
    releases = repo.get_releases()

    for release in releases:

        entry = Changelog(release.tag_name, release.created_at, release.body, release.zipball_url)
        db.session.add(entry)
        db.session.commit()

def getUpdates():
    pass

