from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

class Chatbot:
  def __init__(self, folder):
    load_dotenv()
    self.folder = folder
    self.vectorstore = None
    self.qa_chain = None
    self._initialize_vectorstore()

  def _initialize_vectorstore(self):
    try:
      loader = DirectoryLoader(self.folder, loader_cls=TextLoader)
      data = loader.load()
    except Exception as e:
      raise ValueError("Folder could not be read") from e

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=300)
    all_splits = text_splitter.split_documents(data)
    self.vectorstore = Chroma.from_documents(
      documents=all_splits,
      embedding=OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    )

    with open("prompt.txt", "r") as f:
      template = f.read()

    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k", temperature=0.5)

    self.qa_chain = RetrievalQA.from_chain_type(
      llm,
      retriever=self.vectorstore.as_retriever(),
      chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    )

  def query(self, user_input, language):
    if not self.qa_chain:
      raise ValueError("The QA chain has not been initialized.")

    question = f"{user_input}; Give the answer in {language}"
    result = self.qa_chain({"query": question})
    return result
