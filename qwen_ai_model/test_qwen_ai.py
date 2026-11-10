from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama

llm=ChatOllama(model="qwen2.5:1.5b",temparature=0.7)
messages=[
    SystemMessage(content="you are doctor in the medical feild"),
    HumanMessage(content="what is the usage of the tablet Aziom-lb500")
]
result=llm.invoke(messages)
print(result.content)


