import numpy as np
import json
import os

# Load embeddings
resume_embedding = np.load("embeddings/resume_embedding.npy")
job_embeddings = np.load("embeddings/jobs_embeddings.npy")

# Load job info
with open("data/jobs_cleaned.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)

# Function to compute cosine similarity
def cosine_similarities(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Compute similarities
similarities = [cosine_similarities(resume_embedding, job_emb) for job_emb in job_embeddings]

# Pair with job info
job_scores = list(zip(similarities, jobs))

# Sort by similarity descending
job_scores.sort(reverse=True, key=lambda x: x[0])
top_matches = [
    {
        "rank": i+1,
        "similarity": float(round(score, 4)),
        "title": job["title"],
        "company": job["company"],
        "location": job["location"],
        "snippet": job["description"][:200]
    }
    for i, (score, job) in enumerate(job_scores[:10])
]

# Save to JSON
os.makedirs("results", exist_ok=True)
with open("results/top_matches.json", "w", encoding="utf-8") as f:
    json.dump(top_matches, f, indent=2)

print("Top 10 matches saved to results/top_matches.json")