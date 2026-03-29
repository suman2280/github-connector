Quickstart
----------

First, clone this repo:

```bash
git clone https://github.com/suman2280/github-connector.git
cd github-connector.git
pip install -r requirements.txt
```

Then create ``.env`` file (or rename and modify ``.env.example``) in project root and set GitHub PAT([Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)) for application:

```bash
touch .env
echo GITHUB_TOKEN=your_github_PAT >> .env
```
To run the web application in debug use:

```bash
uvicorn app.main:app --reload
```

Web routes
----------

Once running, access:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

----------

- `GET /repos/{username}` - List all repos of user
- `GET /list-issues/{owner}/{repo}` - List all issues of a repo
- `POST /create-issue` - Creates a issue on a repo

Project structure
-----------------

Files related to application are in the ``app`` directory.
Application parts are:


    app
    ├── routes         - web related stuff.
    │   └── handler    - web routes.
    ├── client         - service layer handling authentication and GitHub API actions.
    ├── config         - loads .env file.
    └── main.py        - FastAPI application creation.