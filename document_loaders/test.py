from langchain_community.document_loaders import TextLoader

data = TextLoader("document_loaders/Notes.txt")

docs = data.load()

print(len(docs))