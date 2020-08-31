

from github import Github

# First create a Github instance:

# or using an access token
g = Github("e0b8617ecb6a5327cd3edb7ed455260e0912509a")
# g= Github()

# Then play with your Github objects:
repo = g.get_repo("yakabuff/shareJ")
releases = repo.get_releases()

for release in releases:

        print(release)
        print(release.tag_name)
        print(release.created_at)
        # print(release.body)
        print(release.zipball_url)


