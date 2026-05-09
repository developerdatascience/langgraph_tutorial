from schemas.state import AgentState
from tools.calculator import calculator
from memory.service import MemoryService
from core.llm import get_llm

llm = get_llm()


def format_messages(messages):
    return "\n".join([f"{m['role']}: {m['content']}" for m in messages])


def executor_node(state: AgentState) -> AgentState:
    session_id = state["session_id"]
    user_input = state["user_input"]
    messages = state["messages"]
    plan = state.get("plan", "")

    # Save user input
    MemoryService.append(session_id, "user", user_input)

    # CASE 1: Tool execution
    if "calculator" in plan.lower():
        result = calculator(user_input)
        answer = f"Calculated result: {result}"

    # CASE 2: LLM response (FIXED)
    else:
        history = format_messages(messages)

        prompt = f"""
        You are a helpful AI assistant.

        Conversation history:
        {history}

        User question:
        {user_input}

        Answer the question based on conversation history.
        """

        response = llm.invoke(prompt)
        answer = response.content
        result = None

    # Save assistant response
    MemoryService.append(session_id, "assistant", answer)

    updated_messages = messages + [
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": answer}
    ]

    return {
        **state,
        "messages": updated_messages,
        "tool_result": result,
        "final_answer": answer
    }