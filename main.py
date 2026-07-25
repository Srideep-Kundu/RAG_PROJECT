from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

data = PyPDFLoader("document_loaders/GRU.pdf")
docs = data.load()

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI that summarizes the text"),
        ("human", "{data}")
    ]
)



model = ChatMistralAI(model = "mistral-medium-latest")

prompt = template.format_messages(data = docs)

result = model.invoke(prompt)

print(result.content)