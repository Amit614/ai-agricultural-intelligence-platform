from evaluation.agent_eval import evaluate_agent
def test_eval():
    assert evaluate_agent(0.9)["passed"]
