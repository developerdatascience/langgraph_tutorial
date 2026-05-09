from core.llm import get_llm
from schemas.state import AgentState

llm = get_llm()

def format_messages(messages):
    return "\n".join([f"{m['role']}: {m['content']}" for m in messages])

def planner_node(state: AgentState) -> AgentState:
    history = format_messages(state["messages"])

    prompt = f"""
    You are a planner agent.

    Conversation history:
    {history}

    Current user input:
    {state['user_input']}

    Decide:
    - Should we use a calculator?
    - Or answer directly?

    Output ONLY:
    PLAN: <your plan>
    """

    response = llm.invoke(prompt)

    return {
        **state,
        "plan": response.content
    }