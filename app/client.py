import requests
from app.config import GITHUB_TOKEN

BASE_URL = "https://api.github.com"

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


def get_user_repos(username: str):
    url = f"{BASE_URL}/users/{username}/repos"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.json()}")

    return response.json()


def list_repo_issues(owner: str, repo: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.json()}")

    return response.json()


def create_issue(owner: str, repo: str, title: str, body: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"

    payload = {
        "title": title,
        "body": body
    }

    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code not in [200, 201]:
        raise Exception(f"GitHub API error: {response.json()}")

    return response.json()

def list_repo_commits(owner: str, repo: str, per_page: int = 10, branch: str = "main"):
    url = f"{BASE_URL}/repos/{owner}/{repo}/commits"
    params = {
        "per_page": per_page
    }
    if branch:
        params["sha"] = branch

    response = requests.get(url,  params=params)
    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.json()}")

    return response.json()