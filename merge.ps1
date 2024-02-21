# Define an array of repository names
$repos = @(
  "repo1",
  "repo2"

  # Add more repository names here if needed
)

$github_id = "GulSam00"
# Loop through each repository and execute the git subtree command
foreach ($repo_name in $repos) {
  $repo_url = "https://github.com/$github_id/$repo_name.git"
  git subtree add --prefix="$repo_name" "$repo_url" main
}