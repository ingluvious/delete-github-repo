'''
@Author: Ingluvious
@Description:
    Loads environment variables and exposes the API layer.
'''
from __future__ import annotations
import os
from pathlib import Path

REPOS = {
    "ingluvious":   "ingluvious",
    "apatite":      "apatite",
    "tindangpinoy": "tindangpinoy"
}

_root = Path(os.getenv("ROOT_INGLUVIOUS_FOLDER", str(Path.home())))

LOCAL_FOLDERS = {
    "ingluvious":   _root / os.getenv("GITHUB_FOLDER_PERSONAL", "Dev - Personal"),
    "apatite":      _root / os.getenv("GITHUB_FOLDER_APATITE", "Dev - Apatite"),
    "tindangpinoy": _root / os.getenv("GITHUB_FOLDER_TINDANGPINOY", "Dev - Tingdang Pinoy"),
}

def _token() -> str:
    token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
    if not token:
        raise EnvironmentError("GITHUB_PERSONAL_ACCESS_TOKEN is not set in your environment or .env file.")
    return token

