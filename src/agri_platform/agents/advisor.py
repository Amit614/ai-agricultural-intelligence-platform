from .base import BaseAgent
from .tools import KnowledgeTool
class FarmAdvisorAgent(BaseAgent):
    def __init__(self, registry):
        self.tool=KnowledgeTool(registry)
    def run(self, query:str):
        q=query.lower()
        if "rice" in q:
            r=self.tool.lookup("crop","rice")
            return r.content if r else "No knowledge found."
        return "No recommendation available."
