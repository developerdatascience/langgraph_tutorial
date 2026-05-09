from langchain_openai import ChatOpenAI
from core.config import settings

def get_llm():
    return ChatOpenAI(
    model="gpt-4o-mini",
    api_key=settings.openrouter_api_key, #type: ignore
    base_url="https://openrouter.ai/api/v1",
    temperature=0,
    max_completion_tokens=3000)