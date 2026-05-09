from langgraph.graph import StateGraph, END
from schemas.state import AgentState
from nodes.planner import planner_node
from nodes.executor import executor_node

def build_graph():
    graph = StateGraph(AgentState)

    # Nodes
    graph.add_node("planner", planner_node)
    graph.add_node("executor", executor_node)

    # Edges
    graph.set_entry_point("planner")
    graph.add_edge("planner", "executor")
    graph.add_edge("executor", END)

    return graph.compile()

