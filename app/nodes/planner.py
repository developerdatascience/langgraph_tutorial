from core.llm import get_llm
from schemas.state import AgentState

model = get_llm()

def planner_node(state: AgentState) -> AgentState:
    prompt = f"""
    You are a planner agent.

    User input: {state['user_input']}
    PLAN: calculator
    EXPRESSION: <math expression only, eg., 18 - 20>

    Otherwise:
    PLAN: direct
"""
    response = model.invoke(prompt)

    return {
        **state,
        "plan": response.content
    }