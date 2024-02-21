from github import Github
import subprocess

# GitHub Token
github_token = 'token'

# Initialize PyGithub with token
g = Github(github_token)

# Get authenticated user
user = g.get_user()

# Create a new repository
be_integrated_repo_name = 'temp'
be_integrated_repo = user.get_repo(be_integrated_repo_name)


# Define a list of repository names to subtree
repos = [
    "temp_repository1",
    "temp_repository2",
    "temp_repository3",
    # Add more repository names here
]

# Define the branch name
branch_name = "main"  # Change this to "master" or "dev" if needed

# Define the prefix (subdirectory) to use for each subtree
prefix = "subtrees"  # Change this to your desired prefix

# Get the URL of the newly created repository
repo_url = be_integrated_repo.clone_url

# Loop through each repository and execute the git subtree command
for repo_name in repos:
    try:
        cur_rep = user.get_repo(repo_name)
        cur_rep_url = cur_rep.clone_url

        subprocess.run(["git", "reset", "--hard"], cwd=f"{prefix}/{repo_name}", check=True)
        subprocess.run(["git", "clean", "-df"], cwd=f"{prefix}/{repo_name}", check=True)

        # Execute git subtree add command
        subprocess.run(["git", "subtree", "add", "--prefix", f"{prefix}/{repo_name}", cur_rep_url, f"{branch_name}"], check=True)
        print(f"Repository '{repo_name}' added as subtree successfully.")

       # Push changes to remote
        subprocess.run(["git", "push", "origin", f"{branch_name}"], cwd=f"{prefix}/{repo_name}", check=True)
        print(f"Changes pushed to remote for repository '{repo_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error adding or pushing repository '{repo_name}': {e}")