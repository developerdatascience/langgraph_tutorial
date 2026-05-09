from graphs.agent_graph import build_graph

def main():
    print("Hello from langgraph-tutorial!")

    graph = build_graph()

    while True:
        user_input = input("User: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        result = graph.invoke({
            "user_input": user_input,
            "plan": None,
            "tool_result": None,
            "final_answer": None
        })

        print("Agent:", result["final_answer"])


if __name__ == "__main__":
    main()
