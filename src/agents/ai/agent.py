from agents.base.agent import IAgent
from agents.ai.api import analisar_issue

class AiAgent(IAgent):
    def run(self, issue):
        print("[AiAgent] Gerando análise da issue...")
        try:
            analise, sugestao = analisar_issue(issue)
            return self.return_issue(issue, analise, sugestao)
        except Exception as e:
            print(f"[AiAgent] Erro na IA: {e}. Fallback.")
            return self.fallback(issue)

    def fallback(self, issue):
        print("[AiAgent] Fallback: utilizando dados padrão.")
        return self.return_issue(issue)

    def return_issue(self, issue, analise=None, sugestao=None):
        return {
            "issue": issue,
            "analise": analise or "Análise não disponível.",
            "sugestao": sugestao or "Sugestão não disponível."
        }
