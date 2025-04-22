# main.py

from github_service import GitHubService
from data_analysis import commits_to_dataframe, contributors_to_dataframe

if __name__ == "__main__":
    service = GitHubService()
    repo = service.get_repo("Projeto-IGNIS/todoList")

    commits = service.get_commits(repo)
    df_commits = commits_to_dataframe(commits)

    contributors = service.get_contributors(repo)
    df_contributors = contributors_to_dataframe(contributors)

    print("\n📊 Top 5 commits:")
    print(df_commits.head())

    print("\n👨‍💻 Contribuidores:")
    print(df_contributors)
