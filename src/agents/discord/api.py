import discord
from settings import DISCORD_TOKEN, CHANNEL_ID

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def send_messages(messages):
    await client.wait_until_ready()
    channel = client.get_channel(int(CHANNEL_ID))

    if channel:
        for message in messages:
            if message.strip():
                await channel.send(message)
                print("[DiscordAPI] Mensagem enviada.")
            else:
                print("[DiscordAPI] Mensagem vazia ignorada.")
    else:
        print("[DiscordAPI] Canal não encontrado.")

    await client.close()

def run_discord_bot(messages):
    @client.event
    async def on_ready():
        await send_messages(messages)

    client.run(DISCORD_TOKEN)