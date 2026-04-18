import sys
import shutil
import utilities.api as api
from utilities.goFetch import REPOS, LOCAL_FOLDERS

def main():
    if len(sys.argv) == 2:
        alias = sys.argv[1]
        if alias not in REPOS:
            print(f"Unknown alias '{alias}'. Available: {', '.join(REPOS)}")
            sys.exit(1)
        owner, repo = REPOS[alias]
    elif len(sys.argv) == 3:
        alias = sys.argv[1]
        owner, repo = sys.argv[1], sys.argv[2]
    else:
        print("Usage: python app.py <alias>")
        print("       python app.py <owner> <repo>")
        print(f"  Aliases: {', '.join(REPOS)}")
        sys.exit(1)

    print(f"Checking if '{owner}/{repo}' exists...")

    if not api.repo_exists(owner, repo):
        print(f"Repository '{owner}/{repo}' does not exist or is not accessible.")
        sys.exit(1)

    confirm = input(f"\nAre you sure you want to permanently delete '{owner}/{repo}'? Type 'yes' to confirm: ")

    if confirm.strip().lower() != "yes":
        print("Deletion cancelled.")
        sys.exit(0)

    try:
        api.delete_repo(owner, repo)
    except (PermissionError, FileNotFoundError, RuntimeError) as e:
        print(f"Error: {e}")
        sys.exit(1)

    local_base = LOCAL_FOLDERS.get(alias)
    if local_base:
        local_path = local_base / repo
        if local_path.exists():
            shutil.rmtree(local_path)
            print(f"Local folder '{local_path}' has been deleted.")
        else:
            print(f"No local folder found at '{local_path}'.")

if __name__ == "__main__":
    main()
