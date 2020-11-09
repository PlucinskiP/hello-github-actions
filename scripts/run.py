from github import Github
import os

g = Github(os.environ.get('GITHUB_TOKEN'))
repo = g.get_repo('PlucinskiP/hello-github-actions')
commit   = repo.get_commit(os.environ.get('GITHUB_SHA'))
pullr = commit.get_pulls()
print("PR number", pullr[0].number)

print( "add label", pullr[0].add_to_labels('test') )

#create_status = commit.create_status(state='success', description='status from py script')
#review_status = pullr[0].get_reviews()

if 'automated_pr' in [a.name for a in pullr[0].labels]:
    print([a.name for a in commit.get_pulls()[0].labels])
    print("Approve PR", pullr[0].create_review(event="APPROVE") )
    print("Merge PR", pullr[0].merge(commit_title="test automerge") )
