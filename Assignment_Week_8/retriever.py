import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class Retriever:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.texts = []
        self.index = None

    def preprocess_csv(self, path):
        df = pd.read_csv(path)
        self.texts = [
            f"Applicant {i + 1}: Gender={row['Gender']}, Married={row['Married']}, "
            f"Education={row['Education']}, Self_Employed={row['Self_Employed']}, "
            f"Income={row['ApplicantIncome']}, LoanAmount={row['LoanAmount']}, "
            f"Loan Status={row['Loan_Status']}"
            for i, row in df.iterrows()
        ]

    def build_index(self):
        embeddings = self.model.encode(self.texts)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings))

    def get_top_k(self, query, k=5):
        query_vec = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_vec), k)
        return [self.texts[i] for i in indices[0]]
