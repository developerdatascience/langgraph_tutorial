from schemas.state import AgentState
from tools.calculator import calculator

def executor_node(state: AgentState) -> AgentState:
    plan = state.get("plan", "")

    if "calculator" in plan.lower():
        expression = state["user_input"]
        result = calculator(expression=expression)

        return {
            **state,
            "tool_result": result,
            "final_answer": f"Calculated results: {result}"
        }
    
    return {
        **state,
        "final_answer": f"LLM Response: {state['user_input']}"
    }