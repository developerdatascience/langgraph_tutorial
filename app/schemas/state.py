from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    user_input: str
    plan: Optional[str]
    total_result: Optional[str]
    final_answer: Optional[str]
    