import uuid
from graphs.agent_graph import build_graph
from memory.store import init_db
from memory.service import MemoryService

def run():
    init_db()

    graph = build_graph()

    session_id = str(uuid.uuid4())
    print(f"Session ID: {session_id}")

    while True:
        user_input = input("User: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        history = MemoryService.get_history(session_id)

        result = graph.invoke({
            "session_id": session_id,
            "user_input": user_input,
            "messages": history,
            "plan": None,
            "tool_result": None,
            "final_answer": None
        })

        print("Agent:", result["final_answer"])

if __name__ == "__main__":
    run()