from github import Github
import os
import requests
import json

g = Github(os.environ.get('GITHUB_TOKEN'))
repo = g.get_repo('PlucinskiP/hello-github-actions')
commit   = repo.get_commit(os.environ.get('GITHUB_SHA'))
#commit_sha = commit.sha
pull_no = commit.get_pulls()[0].number
pr = repo.get_pull(pull_no)

label_check = False
for labels in pr.labels:
    if labels.name == 'automated_pr':
        print(labels.name)
        label_check = True

if label_check:
    tt = commit.get_pulls()
    # review_pr = tt[0].create_review(event="APPROVE")
    merge_pr = tt[0].merge(commit_title="test automerge")
