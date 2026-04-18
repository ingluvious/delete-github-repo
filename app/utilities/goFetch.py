'''
@Author: Ingluvious
@Description:
    A simple utility to fetch data from an API and print the response.
    This is a placeholder function to demonstrate how to structure your code.
    You can replace the URL and logic with your actual data fetching needs.
'''
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

import os
from dotenv import load_dotenv
from pathlib import Path

# Shared env (global across projects file)
SHARED_ENV_FILE = Path.home() / ".config" / ".env"
load_dotenv(dotenv_path = SHARED_ENV_FILE, override = False)

# Project specific env file
PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ENV_FILE = PROJECT_ROOT / ".env"
load_dotenv(dotenv_path = PROJECT_ENV_FILE, override = True)

def print_hello_world():
    print("Hello World!")