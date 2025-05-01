from agents.base.agent import IAgent
from agents.github.api import get_issues

class GithubAgent(IAgent):
    def run(self, data=None):
        print("[GithubAgent] Consultando issues do GitHub...")

        try:
            issues = get_issues("enhancement")

            if not issues:
                print("[GithubAgent] Nenhuma issue encontrada.")
                return self.fallback()

            print(f"[GithubAgent] {len(issues)} issues encontradas.")
            return issues

        except Exception as e:
            print(f"[GithubAgent] Erro ao consultar issues: {e}")
            return self.fallback()

    def fallback(self, data=None):
        print("[GithubAgent] Fallback: Nenhuma issue disponível.")
        return []
