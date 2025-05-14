
from langchain_community.document_loaders import DirectoryLoader
loader = DirectoryLoader("files", glob="**/*.txt")
docs = loader.load()
docs