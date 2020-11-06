from github import Github
import os
import requests

g = Github(os.environ.get('GITHUB_TOKEN'))

user    = g.get_user('PlucinskiP')
repo    = user.get_repo("hello-github-actions")
commit   = repo.get_commit(os.environ.get('GITHUB_SHA'))
commit_no = commit.sha
pull_no = commit.get_pulls()[0].number
pr = repo.get_pull(pull_no)

label_check = False
for labels in pr.labels:
    if labels.name == 'automated_pr':
        label_check = True

if label_check:
    approve_pr = commit.get_pulls()[0].number.reviews( event="APPROVE" )
    merge_pr = commit.get_pulls()[0].merge
