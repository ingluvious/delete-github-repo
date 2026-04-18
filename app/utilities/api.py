'''
@Author: Ingluvious
@Description:
    GitHub API layer. Handles all HTTP calls for repo operations.
'''
from __future__ import annotations
import utilities.goFetch as fetch

import os
import requests

GITHUB_API = os.getenv("GITHUB_DELETE_REPO_URL")

def _headers() -> dict:
    return {
        "Authorization": f"Bearer {fetch._token()}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

def repo_exists(owner: str, repo: str) -> bool:
    url = f"{GITHUB_API}/{owner}/{repo}"
    response = requests.get(url, headers=_headers())
    return response.status_code == 200

def delete_repo(owner: str, repo: str) -> None:
    url = f"{GITHUB_API}/{owner}/{repo}"
    response = requests.delete(url, headers=_headers())

    if response.status_code == 204:
        print(f"Repo '{owner}/{repo}' has been deleted.")
    elif response.status_code == 403:
        raise PermissionError("You do not have permission to delete this repository.")
    elif response.status_code == 404:
        raise FileNotFoundError(f"Repository '{owner}/{repo}' not found.")
    else:
        raise RuntimeError(f"Unexpected response {response.status_code}: {response.text}")
