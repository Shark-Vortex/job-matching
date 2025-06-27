import os
import json
import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load resume
with open("data/mock_resume.txt", "r", encoding="utf-8") as f:
    resume_text = f.read()

# Embed and save
resume_embedding = model.encode([resume_text])[0]
np.save("embeddings/resume_embedding.npy", np.array(resume_embedding))

print("Resume embedding saved.")
