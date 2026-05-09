from typing import List
from memory.store import save_message, load_messages

class MemoryService:

    @staticmethod
    def get_history(session_id: str) -> List[str]:
        return load_messages(session_id)
    
    @staticmethod
    def append(session_id: str, role: str, content: str):
        save_message(session_id, role,  content)