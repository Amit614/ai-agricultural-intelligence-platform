class ConversationSession:
    def __init__(self,session_id:str):
        self.session_id=session_id
        self.history=[]
    def add(self,role,content):
        self.history.append({'role':role,'content':content})
