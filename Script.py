import requests
from datetime import datetime, timedelta

def get_new_commits(username, repository, token, since):
    url = f'https://api.github.com/repos/{username}/{repository}/commits'
    headers = {'Authorization': f'token {token}'}
    params = {'since': since}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        commits = response.json()
        return commits
    else:
        print(f"Failed to fetch commits. Status code: {response.status_code}")
        return None

def main():
    username = 'AAR777'
    repository = 'CICD_Project'
    token = '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'
    
    # Set the datetime for the last check (e.g., one day ago)
    since_datetime = (datetime.now() - timedelta(hours=1)).isoformat()

    commits = get_new_commits(username, repository, token, since_datetime)

    if commits:
        print(f"New commits in {username}/{repository}:")
        for commit in commits:
            print(f"Commit: {commit['sha'][:7]} by {commit['commit']['author']['name']}: {commit['commit']['message']}")
    else:
        print("No new commits.")

if __name__ == "__main__":
    main()
