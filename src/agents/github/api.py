import requests
from settings import GITHUB_OWNER, GITHUB_REPO

def get_issues():
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/issues"
    response = requests.get(url)

    print("[GithubAPI] Response status:", response.status_code)

    if response.status_code != 200:
        raise Exception(f"Erro na consulta: {response.status_code} - {response.text}")

    return response.json()
