import numpy as np
import json

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

# Print top 10
print("\nTop 10 matched jobs:\n")
for i, (score, job) in enumerate(job_scores[:10], start=1):
    print(f"{i}. {job['title']} at {job['company']} in {job['location']}")
    print(f"   Similarity: {score:.4f}")
    print(f"   Description: {job['description'][:100]}...")
    print()