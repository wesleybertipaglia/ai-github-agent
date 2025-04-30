from agents.base.agent import IAgent
from agents.ai.api import resumir_issues

class AiAgent(IAgent):
    def run(self, data: str) -> str:
        if not data:
            print("[AiAgent] Nenhuma issue recebida. Executando fallback.")
            return self.fallback()

        print("[AiAgent] Resumindo issues...")
        try:
            resumo = resumir_issues(data)
            print(f"[AiAgent] Resumo gerado:\n{resumo}")
            return resumo
        except Exception as e:
            print(f"[AiAgent] Erro ao resumir: {e}. Executando fallback.")
            return self.fallback()

    def fallback(self, data=None) -> str:
        print("[AiAgent] Fallback: Nenhuma issue para resumir ou erro na IA.")
        return "Sem resumo disponível."