from agents.base.agent import IAgent
from agents.github.api import get_issues

class GithubAgent(IAgent):
    def run(self, data=None):
        print("[GithubAgent] Consultando issues no GitHub...")

        try:
            issues = get_issues()

            if not issues:
                print("[GithubAgent] Nenhuma issue encontrada.")
                return self.fallback()

            titles = "\n".join([f"- {issue['title']}" for issue in issues])
            print(f"[GithubAgent] Issues encontradas:\n{titles}")
            return titles

        except Exception as e:
            print(f"[GithubAgent] Erro ao consultar issues: {e}")
            return self.fallback()

    def fallback(self, data=None):
        print("[GithubAgent] Fallback: Nenhuma issue disponível.")
        return "Nenhuma issue encontrada."
