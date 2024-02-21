from github import Github

github_token = 'token'

# Initialize PyGithub with token
g = Github(github_token)

# Get authenticated user
user = g.get_user()

# Create a new repository
repo_name = 'temp_repository'
repo_description = 'Temporary repository for testing'
new_repo = user.create_repo(repo_name, description=repo_description)

# Create README.md file
readme_content = "# Temporary Repository\n\nThis is a temporary repository created for testing purposes."
new_repo.create_file("README.md", "Initial commit", readme_content)

print(f"Temporary repository '{repo_name}' created successfully with README.md file.")