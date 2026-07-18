from agri_platform.conversation.session import ConversationSession
from agri_platform.conversation.advisor import ConversationalAdvisor
def test_response():
 s=ConversationSession('1')
 r=ConversationalAdvisor().respond(s,'hello')
 assert 'Found' in r
