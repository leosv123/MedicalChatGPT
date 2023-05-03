import os
import textwrap
import chromadb
import langchain
import openai

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader, UnstructuredPDFLoader, YoutubeLoader
from langchain.embeddings import HuggingFaceEmbeddings, OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

import re


os.environ['OPENAI_API_KEY'] = "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"


def run_query(query, mode):
    model = OpenAI(temperature=0)
    result = model(query)
    clean_result = re.sub(r"\n", "", result)
    return clean_result


if __name__ == '__main__':
    query = input("enter your query")
    ans = run_query(query, 'accurate')
    print(ans)
