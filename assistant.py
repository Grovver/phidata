from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo

assistant = Assistant(tools=[DuckDuckGo()], show_tool_calls=True)
assistant.print_response("Whats happening in France?", markdown=True)


import openai 

openai.api_key = "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"