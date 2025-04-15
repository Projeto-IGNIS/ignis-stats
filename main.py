
from github_service import GitHubService

if __name__ == "__main__":
    
    service = GitHubService()
    repo = service.get_repo("Projeto-IGNIS/todoList")

    print(f"📁 Repositório: {repo.full_name}")
    print(f"⭐ Stars: {repo.stargazers_count}")
    print("👥 Contribuidores:")
    for user in service.get_contributors(repo):
        print(f" - {user.login} ({user.contributions} contribuições)")

    print("\n📦 Últimos 5 commits:")
    for commit in service.get_commits(repo)[:5]:
        print(f"- {commit.commit.author.name}: {commit.commit.message}")
