from agents.base.agent import IAgent
from agents.discord.api import run_discord_bot

class DiscordAgent(IAgent):
    def run(self, data=None):
        print("[DiscordAgent] Preparando mensagem para envio...")

        if not data:
            print("[DiscordAgent] Nenhuma mensagem para enviar, acionando fallback.")
            return self.fallback()

        try:
            run_discord_bot(data)
            return "Mensagem enviada com sucesso."
        except Exception as e:
            print(f"[DiscordAgent] Erro ao enviar mensagem: {e}")
            return self.fallback()

    def fallback(self, data=None):
        print("[DiscordAgent] Fallback: Nenhuma notificação enviada.")
        return "Nenhuma notificação enviada."
