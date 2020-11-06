from github import Github
import os
import requests

g = Github(os.environ.get('GITHUB_TOKEN'))

user    = g.get_user('PlucinskiP')
repo    = user.get_repo("hello-github-actions")
commit   = repo.get_commit(os.environ.get('COMMIT_SHA'))
commit_no = commit.sha
pull_no = commit.get_pulls()[0].number
pr = repo.get_pull(pull_no)

label_check = False
for labels in pr.labels:
    if labels.name == 'automated_pr':
        label_check = True

token = "token "+os.environ.get('GITHUB_TOKEN')
url_approve = "https://api.github.com/repos/PlucinskiP/hello-github-actions/pulls/"+str(pull_no)+"/reviews"
url_merge = "https://api.github.com/repos/PlucinskiP/hello-github-actions/pulls/"+str(pull_no)+"/merge"
if label_check:

    headers_approve = {
        'Authorization': token,
    }
    data = '{"event": "APPROVE"}'
    approve_res = requests.post(url_approve, headers=headers_approve, data=data)

    headers_merge = {
        'Authorization': token,
    }
    merge_res = requests.put(url_merge, headers=headers_merge)
