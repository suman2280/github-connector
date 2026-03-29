from fastapi import APIRouter, HTTPException
from app.client import (
    get_user_repos,
    list_repo_issues,
    create_issue,
    list_repo_commits,
    create_pull_request
)

router = APIRouter()

@router.get("/repos/{username}")
def get_repos(username: str):
    try:
        return get_user_repos(username)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/list-issues/{username}/{repo}")
def get_issues(username: str, repo: str):
    try:
        return list_repo_issues(username, repo)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/create-issue")
def create_issue_route(username: str, repo: str, title: str, body: str):
    try:
        return create_issue(username, repo, title, body)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/commits/{username}/{repo}")
def get_commits(username: str, repo: str, per_page: int = 10, branch: str = "main"):
    try:
        return list_repo_commits(username, repo, per_page, branch)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/create-pr")
def create_pr(username: str, repo: str, title: str, head: str, base: str, body: str):
    try:
        return create_pull_request(username, repo, title, head, base, body)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))