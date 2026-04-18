'''
@Author: Ingluvious
@Description:
    Utility for interacting with the GitHub API.
    Handles repo existence checks and deletion for orgs or personal accounts.
'''
from __future__ import annotations

import os
import requests
from dotenv import load_dotenv
from pathlib import Path

SHARED_ENV_FILE = Path.home() / ".config" / ".env"
load_dotenv(dotenv_path=SHARED_ENV_FILE, override=False)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ENV_FILE = PROJECT_ROOT / ".env"
load_dotenv(dotenv_path=PROJECT_ENV_FILE, override=True)

GITHUB_API = "https://api.github.com"


def _token() -> str:
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise EnvironmentError("GITHUB_TOKEN is not set in your environment or .env file.")
    return token


def _headers() -> dict:
    return {
        "Authorization": f"Bearer {_token()}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def repo_exists(owner: str, repo: str) -> bool:
    url = f"{GITHUB_API}/repos/{owner}/{repo}"
    response = requests.get(url, headers=_headers())
    return response.status_code == 200


def delete_repo(owner: str, repo: str) -> None:
    url = f"{GITHUB_API}/repos/{owner}/{repo}"
    response = requests.delete(url, headers=_headers())

    if response.status_code == 204:
        print(f"Repo '{owner}/{repo}' has been deleted.")
    elif response.status_code == 403:
        raise PermissionError("You do not have permission to delete this repository.")
    elif response.status_code == 404:
        raise FileNotFoundError(f"Repository '{owner}/{repo}' not found.")
    else:
        raise RuntimeError(f"Unexpected response {response.status_code}: {response.text}")
