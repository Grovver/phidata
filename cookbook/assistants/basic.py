from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
import openai

# Directly pass the API key
api_key = "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"

openai.api_key = 'api_key'

# List available models
models = openai.Model.list()

for model in models['data']:
    print(model['id'])

    
assistant = Assistant(
    llm=OpenAIChat(model="gpt-4", api_key=api_key),
    description="You help people with their health and fitness goals.",
    instructions=["Recipes should be under 5 ingredients"]
)

# Print a response to the CLI
assistant.print_response("Share a breakfast recipe.", markdown=True)
