from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You   help people with their health and fitness goals and need make them healty .",
    instructions=["Recipes should be under 5 ingredients, look for recipes in hebrew language"],
)
# -*- Print a response to the cli
assistant.print_response("Share a breakfast recipe.", markdown=True)



assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You help people with their health and fitness goals.",
    instructions=["Recipes should be under 5 ingredients"],
)




assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You help people with their health and fitness goals.",
    instructions=["Recipes should be under 5 ingredients"],
)