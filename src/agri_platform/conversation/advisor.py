from .session import ConversationSession
class ConversationalAdvisor:
    def __init__(self,rag=None):
        self.rag=rag
    def respond(self,session:ConversationSession,query:str):
        docs=self.rag.retrieve(query) if self.rag else []
        session.add('user',query)
        answer=f'Found {len(docs)} relevant knowledge documents.'
        session.add('assistant',answer)
        return answer
