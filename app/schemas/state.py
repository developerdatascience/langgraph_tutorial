from typing import TypedDict, List, Optional

class Message(TypedDict):
    role: str
    content: str


class AgentState(TypedDict):
    session_id: str
    user_input: str

    messages: List[Message]

    plan: Optional[str]
    total_result: Optional[str]
    final_answer: Optional[str]
    