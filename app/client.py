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


def list_repo_issues(username: str, repo: str):
    url = f"{BASE_URL}/repos/{username}/{repo}/issues"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.json()}")

    return response.json()


def create_issue(username: str, repo: str, title: str, body: str):
    url = f"{BASE_URL}/repos/{username}/{repo}/issues"

    payload = {
        "title": title,
        "body": body
    }

    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code not in [200, 201]:
        raise Exception(f"GitHub API error: {response.json()}")

    return response.json()

def list_repo_commits(username: str, repo: str, per_page: int, branch: str):
    url = f"{BASE_URL}/repos/{username}/{repo}/commits"
    params = {
        "per_page": per_page
    }
    if branch:
        params["sha"] = branch

    response = requests.get(url,  params=params)
    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.json()}")

    return response.json()

def create_pull_request(username: str, repo: str, title: str, head: str, base: str, body: str):
    url = f"{BASE_URL}/repos/{username}/{repo}/pulls"
    payload = {
        "title": title,
        "head": head,
        "base": base,
        "body": body
    }
    response = requests.post(url=url, headers=HEADERS, json=payload)
    if response.status_code != 201:
         raise Exception(f"GitHub API error: {response.json()}")

    return response.json()