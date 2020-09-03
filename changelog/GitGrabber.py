from github import Github
from app import settings
from model import Changelog
from model.Changelog import db


def initialRetrival():


    g = Github(settings.GITHUB_KEY)
    repo = g.get_repo("yakabuff/shareJ")
    releases = repo.get_releases()

    for release in releases:

        # entry = Changelog.Changelog(release.tag_name, release.created_at, release.body, release.zipball_url)
        db.session.add(Changelog.Changelog( release.id, release.tag_name,release.created_at, release.body, release.zipball_url))
        db.session.commit()

def getUpdates():
    pass

