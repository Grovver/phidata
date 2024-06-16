# basic.py
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
import json

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You help people with their health and fitness goals and need to make them healthy.",
    instructions=["Recipes should be under 5 ingredients, look for recipes in Hebrew language"],
)
# Generate a response and print it in JSON format
response = assistant.respond("Share a breakfast recipe.")
print(json.dumps({"response": response}, ensure_ascii=False))