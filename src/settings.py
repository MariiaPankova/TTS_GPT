from pydantic_settings import BaseSettings
from pydantic import Field


class AppSettings(BaseSettings):
    api_key: str = Field(alias="OPENAI_API_KEY")
    model: str = "gpt-3.5-turbo"
    context: str = "You are a philosophy teacher."


settings = AppSettings(_env_file=".env")
