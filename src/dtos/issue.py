class IssueDTO:
    def __init__(self, issue_json):
        self.id = issue_json.get("id")
        self.title = issue_json.get("title")
        self.body = issue_json.get("body", "")
        self.url = issue_json.get("html_url")
        self.state = issue_json.get("state")
        self.labels = [label["name"] for label in issue_json.get("labels", [])]
        self.created_at = issue_json.get("created_at")
        self.updated_at = issue_json.get("updated_at")
        self.assignee = issue_json.get("assignee", {}).get("login")
        self.analise = issue_json.get("analise", "Análise não disponível.")
        self.sugestao = issue_json.get("sugestao", "Sugestão não disponível.")

    def __repr__(self):
        return f"<IssueDTO(id={self.id}, title={self.title}, state={self.state})>"
