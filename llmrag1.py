import pandas as pd
import faiss
import numpy as np
import openai
from openai import OpenAI # for calling the OpenAI API
import os

# Load clinical data from CSV
data = pd.read_csv('/Users/bolttoday/Downloads/cdata1.csv')
apikey = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>"))


# Initialize OpenAI API key
openai.api_key = apikey

# Function to generate embeddings using OpenAI
def generate_embeddings(texts):
    response = openai.Embedding.create(
        input=texts,
        model="text-embedding-ada-002"  # Example embedding model
    )
    embeddings = [r['embedding'] for r in response['data']]
    return np.array(embeddings)

# Generate embeddings for the clinical data
texts = data['text'].tolist()
embeddings = generate_embeddings(texts)

# Initialize FAISS index
dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)

# Add embeddings to the FAISS index
index.add(embeddings)

# Function to perform retrieval
def retrieve(query, k=3):
    query_embedding = generate_embeddings([query])
    D, I = index.search(query_embedding, k)  # D: distances, I: indices
    return data.iloc[I[0]].to_dict(orient='records')

# Function to generate a response using OpenAI GPT
def generate_response(retrieved_texts, query):
    context = "\n".join([f"Context {i+1}: {text['text']}" for i, text in enumerate(retrieved_texts)])
    prompt = f"{context}\n\nQuestion: {query}\nAnswer:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Main function to handle the RAG process
def rag_model(query):
    retrieved_texts = retrieve(query)
    response = generate_response(retrieved_texts, query)
    return response

# Example usage
query = "What should be monitored in a patient with hypertension?"
response = rag_model(query)
print("Response:", response)
