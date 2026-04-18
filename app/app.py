import sys
import utilities.goFetch as fetch

def main():
    if len(sys.argv) != 3:
        print("Usage: python app.py <owner> <repo>")
        print("  owner  — GitHub username or organisation name")
        print("  repo   — Repository name to delete")
        sys.exit(1)

    owner, repo = sys.argv[1], sys.argv[2]

    print(f"Checking if '{owner}/{repo}' exists...")

    if not fetch.repo_exists(owner, repo):
        print(f"Repository '{owner}/{repo}' does not exist or is not accessible.")
        sys.exit(1)

    confirm = input(f"\nAre you sure you want to permanently delete '{owner}/{repo}'? Type 'yes' to confirm: ")

    if confirm.strip().lower() != "yes":
        print("Deletion cancelled.")
        sys.exit(0)

    try:
        fetch.delete_repo(owner, repo)
    except (PermissionError, FileNotFoundError, RuntimeError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
