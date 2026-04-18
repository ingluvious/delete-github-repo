# 🗑️ Delete GitHub Repo

A Python CLI tool that deletes a GitHub repository via the GitHub API and removes the corresponding local project folder from your machine.

---

## 🎯 Purpose

Managing leftover repositories can be tedious — this tool handles it in one command. Provide an owner alias and a repo name, and it will:

1. Verify the repository exists on GitHub
2. Ask for confirmation before doing anything destructive
3. Delete the repository via the GitHub API
4. Remove the corresponding local project folder from your machine

---

## 📁 Project Structure

```
delete-github-repo/
│
├── app/
│   ├── delete-repo.py          # Main entrypoint — argument parsing, confirmation prompt, orchestration
│   └── utilities/
│       ├── goFetch.py          # Loads .env files, defines REPOS and LOCAL_FOLDERS maps
│       └── api.py              # GitHub API layer — repo_exists() and delete_repo() calls
│
├── scripts/                    # Per-owner shell scripts (installed to /usr/local/bin)
│   ├── delete-personal-repo    # Targets the ingluvious GitHub account
│   ├── delete-apatite-repo     # Targets the Apatite organisation
│   └── delete-tindangpinoy-repo # Targets the Tindang Pinoy organisation
│
├── .env                        # Project-level environment variables (gitignored)
├── requirements.txt            # Python dependencies
└── setup.py                    # Package setup
```

---

## ⚙️ How It Works

### Owner Aliases

The `REPOS` map in `goFetch.py` maps an alias to a `(github_owner, default_repo)` pair:

| Alias | GitHub Owner |
|---|---|
| `ingluvious` | ingluvious |
| `apatite` | ingluvious (Apatite org) |
| `tindangpinoy` | ingluvious (Tindang Pinoy org) |

### Local Folder Mapping

The `LOCAL_FOLDERS` map in `goFetch.py` maps the same aliases to local base directories, sourced from your `~/.config/.env`:

| Alias | Local Folder |
|---|---|
| `ingluvious` | `$ROOT_INGLUVIOUS_FOLDER/$GITHUB_FOLDER_PERSONAL` |
| `apatite` | `$ROOT_INGLUVIOUS_FOLDER/$GITHUB_FOLDER_APATITE` |
| `tindangpinoy` | `$ROOT_INGLUVIOUS_FOLDER/$GITHUB_FOLDER_TINDANGPINOY` |

---

## 🛠️ Prerequisites

### 1. Install dependencies

```bash
brew install uv
uv pip install -r requirements.txt
```

### 2. Configure environment variables

Add the following to your `~/.config/.env`:

```bash
# GitHub
GITHUB_PERSONAL_ACCESS_TOKEN="your_token_here"
GITHUB_DELETE_REPO_URL="https://api.github.com/repos"

# Local folder roots
ROOT_INGLUVIOUS_FOLDER="/Users/yourname"
GITHUB_FOLDER_PERSONAL="Dev - Personal"
GITHUB_FOLDER_APATITE="Dev - Apatite"
GITHUB_FOLDER_TINDANGPINOY="Dev - Tingdang Pinoy"

# Path to app entrypoint (used by shell scripts)
DELETE_APP_PATH="/path/to/delete-github-repo/app/delete-repo.py"
```

> ⚠️ Your GitHub Personal Access Token requires the `delete_repo` scope.

---

## 🚀 Usage

### Via shell scripts (recommended)

Each script has the owner pre-configured — just pass the repo name:

```bash
delete-personal-repo <repo>
delete-apatite-repo <repo>
delete-tindangpinoy-repo <repo>
```

**Example:**
```bash
delete-personal-repo my-old-project
```

### Directly via Python

```bash
# Using an alias
python delete-repo.py <alias> <repo>

# Using explicit owner and repo
python delete-repo.py <owner> <repo>
```

**Example:**
```bash
python delete-repo.py ingluvious my-old-project
```

---

## 📦 Installing the Shell Scripts

Copy the scripts to `/usr/local/bin` so they are available system-wide:

```bash
cp scripts/delete-personal-repo /usr/local/bin/delete-personal-repo
cp scripts/delete-apatite-repo /usr/local/bin/delete-apatite-repo
cp scripts/delete-tindangpinoy-repo /usr/local/bin/delete-tindangpinoy-repo
chmod +x /usr/local/bin/delete-personal-repo
chmod +x /usr/local/bin/delete-apatite-repo
chmod +x /usr/local/bin/delete-tindangpinoy-repo
```

---

## ✅ TO DO

- [ ] Add support for additional owner aliases
- [ ] Add dry-run mode to preview what would be deleted
- [ ] Add logging to a file for audit trail
