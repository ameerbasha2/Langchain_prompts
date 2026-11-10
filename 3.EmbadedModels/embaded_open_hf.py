from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents=[
    "i am the god god is grate ",
    "pigs come in croud and the lion comes sing to fight",
    "even i tell one time it sound like hunderd times"
    
]
vector=embedding.embed_documents(documents)
print(str(vector))
