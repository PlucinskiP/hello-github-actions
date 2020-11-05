from github import Github
import os
import requests

g = Github(os.environ.get('GITHUB_TOKEN'))

user    = g.get_user('PlucinskiP')
repo    = user.get_repo("hello-github-actions")
commit   = repo.get_commit(os.environ.get('COMMIT_SHA'))



pull_no = commit.get_pulls()[0].number
pr = repo.get_pull(pull_no)

label_check = False
for labels in pr.labels:
    if labels.name == 'automated_pr':
        label_check = True

token = "token "+os.environ.get('GITHUB_TOKEN')
url = "https://api.github.com/repos/PlucinskiP/hello-github-actions/pulls/"+pull_no+"/merge"
if label_check:
    # add approve to pr
    # merge pr
    headers = {
        'Authorization': token,
    }
    response = requests.put(url, headers=headers)
