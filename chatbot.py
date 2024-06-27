import os

from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
from pinecone import Pinecone

load_dotenv()

loader = DirectoryLoader('./site_data', loader_cls=TextLoader)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=20,
    length_function=len
)

texts = text_splitter.split_documents(documents)

pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))

vector_store = pc.from_documents(
    texts, embeddings, index_name="chat-with-text-file"
)

qa = RetrievalQA.from_chain_type(
    llm=OpenAI(), chain_type="stuff", retriever=vector_store.as_retriever(), return_source_documents=True
)

question = "What is the general overview of the UM safe computing site?"
result = qa({"query": question})

print(result)