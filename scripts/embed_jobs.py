import os
import json
import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load job descriptions
with open("data/jobs_cleaned.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)

# Embed each job description
job_embeddings = [model.encode([job["description"]])[0] for job in jobs]

# Save embeddings
np.save("embeddings/jobs_embeddings.npy", np.array(job_embeddings))

print("Job embeddings saved.")
