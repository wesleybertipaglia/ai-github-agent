from agents.github.agent import GithubAgent
from agents.ai.agent import AiAgent
from agents.discord.agent import DiscordAgent
from pipeline.manager import PipelineManager

pipeline = PipelineManager()
pipeline.add_step(GithubAgent())
pipeline.add_step(AiAgent())
pipeline.add_step(DiscordAgent())

result = pipeline.run()
