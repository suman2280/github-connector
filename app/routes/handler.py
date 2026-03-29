from fastapi import APIRouter, HTTPException
from app.client import (
    get_user_repos,
    list_repo_issues,
    create_issue
)

router = APIRouter()


@router.get("/repos/{username}")
def get_repos(username: str):
    try:
        return get_user_repos(username)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/list-issues/{owner}/{repo}")
def get_issues(owner: str, repo: str):
    try:
        return list_repo_issues(owner, repo)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/create-issue")
def create_issue(owner: str, repo: str, title: str, body: str):
    try:
        return create_issue(owner, repo, title, body)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))