from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # model_config replaces the old class Config
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"  # Ignores extra variables in your .env
    )

    # You can provide defaults or use Field for extra metadata
    openai_api_key: str = Field(..., alias="OPENAI_API_KEY")
    openrouter_api_key: str = Field(..., alias="OPENROUTER_API_KEY")

settings = Settings()

# Access them like this:
# print(settings.openai_api_key)