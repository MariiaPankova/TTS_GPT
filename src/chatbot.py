import openai
from settings import settings

openai.api_key = settings.api_key

messages = [{"role": "system", "content": settings.context}]


def chatbot(message: str):
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model=settings.model, messages=messages)
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply
