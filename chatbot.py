from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama
llm=ChatOllama(model="qwen2.5:1.5b")
messages=[
    SystemMessage(content="Your are a ai assistant")
]
while True:
    user_input=input()
    if user_input.lower()=="exist":
        break
    messages.append(HumanMessage(content=user_input))
    result=llm.invoke(messages)
    messages.append(result.content)
    print(result.content)
print(messages)

