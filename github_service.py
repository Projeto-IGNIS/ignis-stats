import os
from dotenv import load_dotenv
from github import Github

load_dotenv()

class GitHubService:
    def __init__(self):
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            raise ValueError("GITHUB_TOKEN não encontrado no .env")
        self.github = Github(token)

    def get_repo(self, full_repo_name):
        return self.github.get_repo(full_repo_name)

    def get_commits(self, repo):
        return repo.get_commits()

    def get_contributors(self, repo):
        return repo.get_contributors()

    def get_issues(self, repo, state='all'):
        return repo.get_issues(state=state)

    def get_pull_requests(self, repo, state='all'):
        return repo.get_pulls(state=state)

    def get_commit_activity(self, repo):
        return repo.get_stats_commit_activity()
