from github import Github
from datetime import datetime, timedelta, timezone

# GitHub Token
github_token = 'token'

# Initialize PyGithub with token
g = Github(github_token)

# Get authenticated user
user = g.get_user()
preservation_day = 7    

# Repository names to delete
repos_to_delete = ['temp_repository1', 'temp_repository2']



def check_deletion(repo_name, repo):
    if repo.size == 0:  # Check if the repository is empty
        print(f"레포지토리 '{repo_name}'는 비어 있습니다.")
        confirm_deletion()
        return

    commits = repo.get_commits()
    commit_count = commits.totalCount
    if commit_count > 0:
        last_commit = commits[0]
        most_recent_commit_date = last_commit.commit.author.date
        recent_activity = most_recent_commit_date.strftime("%Y-%m-%d %H:%M:%S")
    else:
        commit_count = "None"
        recent_activity = "None"
 
    print(f"레포지토리 정보 :")
    print(f"이름: {repo_name}")
    print(f"커밋 횟수: {commit_count}")
    print(f"최근 커밋: {recent_activity}")

# Check if the last commit is within N days
    if commit_count > 0 and datetime.now(timezone.utc) - most_recent_commit_date < timedelta(days=preservation_day):
        print(f"최근의 기록이 남아있습니다. '{repo_name}' 레포지토리 삭제를 건너뜁니다.")
    else:
        confirm_deletion()

def confirm_deletion():
    confirmation = input(f"주의: 원격저장소(깃허브)의 레포지토리 '{repo_name}'가 삭제됩니다. 이는 돌이킬 수 없습니다. "
                        f"확인하셨다면 'yes'라고 치세요 : ")
    if confirmation.lower() == 'yes':
        # Delete the repository
        repo.delete()
        print(f"레포지토리 '{repo_name}'는 성공적으로 삭제했습니다.")
    else:
        print(f"레포지토리 '{repo_name}' 삭제를 취소합니다.")


# Check last commit date and delete repositories
for repo_name in repos_to_delete:
    try:
        # Get repository object
        repo = user.get_repo(repo_name)
        check_deletion(repo_name, repo)  
    except Exception as e:
        print(f"레포지토리 '{repo_name}' 삭제 에러 : {e}")
