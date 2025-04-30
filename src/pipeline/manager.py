class PipelineManager:
    def __init__(self):
        self.steps = []

    def add_step(self, agent):
        self.steps.append(agent)

    def run(self, initial_data=None):
        data = initial_data
        for agent in self.steps:
            try:
                data = agent.run(data)
            except Exception as e:
                print(f"[Erro em {agent.__class__.__name__}] {e}")
                data = agent.fallback(data)
        return data
