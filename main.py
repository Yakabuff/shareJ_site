

from github import Github

# First create a Github instance:

# or using an access token
g = Github("ef7a1ada4e9ff31624daae9eabf42852b3f9b588")
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


