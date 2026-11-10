
from langchain_ollama import ChatOllama

# 1. Connect to our local Qwen model
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.7
)

# 2. Send a question to the model
response = llm.invoke("who is the capital of america ")

# 3. Display the response
print(response.content)
