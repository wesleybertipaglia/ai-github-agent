import requests
from datetime import datetime, timedelta
from dtos.issue import IssueDTO
from settings import GITHUB_TOKEN, GITHUB_USER

def get_issues(label="bug"):
    start_week = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    url = f"https://api.github.com/search/issues?q=assignee:{GITHUB_USER}+state:open+label:{label}+created:>={start_week}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    # response = requests.get(url, headers=headers)
    response = requests.get(url)
    
    print("[GithubAPI] Response status:", response.status_code)

    if response.status_code != 200:
        raise Exception(f"Erro na consulta: {response.status_code} - {response.text}")

    data = response.json()
    issues = [IssueDTO(issue) for issue in data.get("items", [])]
    return issues