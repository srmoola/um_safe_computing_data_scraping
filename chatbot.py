import logging
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Chatbot:
    def __init__(self, folder):
        load_dotenv()
        self.folder = folder
        self.vectorstore = None
        self.qa_chain = None
        self._initialize_vectorstore()

    def _initialize_vectorstore(self):
        try:
            logging.info("Loading documents from the directory...")
            loader = DirectoryLoader(self.folder, loader_cls=TextLoader)
            data = loader.load()
            logging.info("Documents loaded successfully.")
        except Exception as e:
            logging.error("Error loading documents from the folder.", exc_info=True)
            raise ValueError("Folder could not be read") from e

        logging.info("Splitting documents into chunks...")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=300)
        all_splits = text_splitter.split_documents(data)
        logging.info("Document splitting completed.")

        logging.info("Creating vector store...")
        self.vectorstore = Chroma.from_documents(
            documents=all_splits,
            embedding=OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
        )
        logging.info("Vector store created successfully.")

        try:
            logging.info("Loading prompt template from file...")
            with open("prompt.txt", "r") as f:
                template = f.read()
            logging.info("Prompt template loaded.")
        except Exception as e:
            logging.error("Error loading prompt template from file.", exc_info=True)
            raise

        QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
        llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k", temperature=0.5)

        logging.info("Initializing the QA chain...")
        self.qa_chain = RetrievalQA.from_chain_type(
            llm,
            retriever=self.vectorstore.as_retriever(),
            chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
        )
        logging.info("QA chain initialized successfully.")

    def query(self, user_input, language):
        if not self.qa_chain:
            logging.error("The QA chain has not been initialized.")
            raise ValueError("The QA chain has not been initialized.")

        question = f"{user_input}; Give the answer in {language}"
        logging.info(f"Processing query: {question}")
        result = self.qa_chain({"query": question})
        logging.info("Query processed successfully.")
        return result
