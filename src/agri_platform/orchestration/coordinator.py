class AgentCoordinator:
    def __init__(self,agents=None):
        self.agents=agents or []
    def register(self,agent):
        self.agents.append(agent)
    def run(self,context):
        results=[]
        for a in self.agents:
            if hasattr(a,'advise'):
                results.extend(a.advise(context))
        return sorted(results,key=lambda x:x.get('priority',99))
