from langchain_community.document_loaders import PyPDFLoader
pdfdoc=PyPDFLoader('samplepdf.pdf')
doc=pdfdoc.load()
doc