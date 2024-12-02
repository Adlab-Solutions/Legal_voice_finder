import os
import numpy as np
import faiss
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_community.document_loaders import Docx2txtLoader
import openai
from glob import glob
import re
import sys

sys.path.append(os.path.abspath("Lib"))

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_KEY")

def load_multiple_docx_files(directory_path):
    # Get all .docx files in the directory
    docx_files = glob(f"{directory_path}/*.docx")
    
    # List to store all the loaded documents
    documents = []
    
    # Load each .docx file and extend the list of documents
    for file in docx_files:
        loader = Docx2txtLoader(file)
        documents.extend(loader.load())
    
    return documents

# Initialize OpenAIEmbeddings
openai_embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002",  # Use the correct embedding model
    openai_api_key=openai.api_key
)


def extract_n_files(query):
    # Load your documents
    docs = load_multiple_docx_files('word_placeholder/')

    # Generate embeddings for the documents
    embedding_vectors = np.array([openai_embeddings.embed_query(doc.page_content) for doc in docs]).astype('float32')

    # Create a FAISS index using L2 distance
    index = faiss.IndexFlatL2(embedding_vectors.shape[1])  # L2 index

    # Add the embeddings to the index
    index.add(embedding_vectors)

    # Define a function to search the FAISS index
    def search_faiss_index(query, index, embeddings, top_k=6):
        # Generate the embedding for the query
        query_vector = np.array(embeddings.embed_query(query)).astype('float32').reshape(1, -1)  # Reshape for FAISS
        # Perform the search
        distances, indices = index.search(query_vector, top_k)  # Search for the top K nearest neighbors
        
        results = []
        for i in range(len(indices[0])):
            doc_index = indices[0][i]
            if doc_index != -1:  # Check if the index is valid
                file_name = docs[doc_index].metadata.get("source", "Unknown source")
                results.append((file_name, docs[doc_index].page_content))
        
        return results

    # Example usage of the search function
    
    top_k_results = search_faiss_index(query, index, openai_embeddings, top_k=6)

    list_filename=[re.search(r'[^\\]+$', _).group(0) for _,file_name in top_k_results]
    # Print the results

    return list_filename
