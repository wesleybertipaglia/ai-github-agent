from agents.base.agent import IAgent
from agents.template.issue import template_issue
from dtos.issue import IssueDTO

class TemplateAgent(IAgent):
    def run(self, issue_dto: IssueDTO):

        if not isinstance(issue_dto, IssueDTO):
            print("[TemplateAgent] Erro: Dados não estão no formato esperado (IssueDTO).")
            return self.fallback(issue_dto)

        print("[TemplateAgent] Gerando template para o Discord...")
        return template_issue(issue_dto)

    def fallback(self, issue_dto):
        print("[TemplateAgent] Fallback: template simples.")
        return template_issue(issue_dto)
