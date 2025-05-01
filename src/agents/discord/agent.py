from agents.base.agent import IAgent
from agents.discord.api import run_discord_bot

class DiscordAgent(IAgent):
    def __init__(self):
        super().__init__()
        self.processes_multiple = True

    def run(self, messages):
        print("[DiscordAgent] Preparando mensagem para envio...")
        
        valid_messages = [msg for msg in messages if msg.strip()]

        if valid_messages:
            print(f"[DiscordAgent] Enviando {len(valid_messages)} mensagens para o Discord.")
            run_discord_bot(valid_messages)
        else:
            print("[DiscordAgent] Nenhuma mensagem válida para enviar. Fallback acionado.")
            return self.fallback(messages)

    def fallback(self, messages):
        print("[DiscordAgent] Fallback: Nenhuma mensagem enviada.")
        return ["Nenhuma mensagem válida para envio."]
