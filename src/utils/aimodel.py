from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd
from transformers import pipeline

class RAGQuoteAgent:
    def __init__(self, quotes_csv_path, embedding_model_name="all-MiniLM-L6-v2", llm_model_name="mistralai/Mistral-7B-Instruct-v0.2"):
        # Load quotes
        self.quotes_df = pd.read_csv(quotes_csv_path)
        self.texts = self.quotes_df["quote_2"].tolist()
        # Load embedding model
        self.embedder = SentenceTransformer(embedding_model_name)
        # Compute or load embeddings
        self.embeddings = self.embedder.encode(self.texts, convert_to_numpy=True)
        # Build FAISS index
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)
        # Load LLM pipeline
        self.llm = pipeline("text-generation", model=llm_model_name, device_map="auto", trust_remote_code=True)
    
    def retrieve(self, query, top_k=3):
        query_emb = self.embedder.encode([query], convert_to_numpy=True)
        D, I = self.index.search(query_emb, top_k)
        return [self.texts[i] for i in I[0]]
    
    def generate(self, query, top_k=3):
        retrieved_quotes = self.retrieve(query, top_k=top_k)
        context = "\n".join(retrieved_quotes)
        prompt = f"User: {query}\nRelevant Quotes:\n{context}\n\nBased on the above, provide a motivational response:"
        response = self.llm(prompt, max_new_tokens=100, do_sample=True)[0]["generated_text"]
        return response, retrieved_quotes