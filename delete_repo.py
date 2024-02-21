from github import Github
from datetime import datetime, timedelta

# GitHub Token
github_token = 'token'

# Initialize PyGithub with token
g = Github(github_token)

# Get authenticated user
user = g.get_user()

preservation_day = 0

# List repositories for the authenticated user
for repo in user.get_repos():
    print(repo.name)

# Repository names to delete
repos_to_delete = ['temp_repository1', 'temp_repository2']

# Check last commit date and delete repositories
for repo_name in repos_to_delete:
    try:
        # Get repository object
        repo = user.get_repo(repo_name)
        # Get the last commit date
        last_commit = repo.get_commits()[0].commit.author.date
        # Check if the last commit is within the last 7 days
        if datetime.now() - last_commit < timedelta(days=7):
            print(f"Skipping deletion of repository '{repo_name}'. Recent commits detected.")
        else:
            # Prompt user for confirmation
            confirmation = input(f"WARNING: Repository '{repo_name}' will be deleted. This action is irreversible. "
                                 f"Type 'yes' to confirm: ")
            if confirmation.lower() == 'yes':
                # Delete the repository
                repo.delete()
                print(f"Repository '{repo_name}' deleted successfully.")
            else:
                print(f"Deletion of repository '{repo_name}' canceled.")
    except Exception as e:
        print(f"Error deleting repository '{repo_name}': {e}")
