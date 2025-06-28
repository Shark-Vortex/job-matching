# AI-Powered Job Matching System
This project builds a complete pipeline to recommend jobs matching a given resume.
It was created for my CS325 final project.

## How it Works
1. **Data Acquisition:**
    - Uses the JSearch API to collect job postings from multiple sources.
    - Focuses on matching jobs to the profile in `mock_resume.txt` (Jane Doe).
    - Raw data saved to `data/jobs_raw.json`.
2. **Data Preprocessing:**
    - Cleans job descriptions and extracts key fields.
    - Saves to `data/jobs_cleaned.json`.
3. **Embedding Information:**
    - Uses `sentence-transformers` (`all-MiniLM-L6-v2`) to embed:
        - Each job posting → `embeddings/jobs_embeddings.npy`
        - The resume → `embeddings/resume_embedding.npy`
4. **Similarity Calculation:**
    - Computes cosine similarity between the resume and each job.
    - Outputs the top 10 matches to `results/top_matches.json`.

## File Overview
- `scripts/scrape_jobs.py` → Gets job data from JSearch API.
- `scripts/preprocess.py` → Cleans and structures the data.
- `scripts/embed_resume.py` → Generates embedding for the resume.
- `scripts/embed_jobs.py` → Computes cosine similarity and saves top matches.
- `.env` → Stores sensitive API keys (excluded from Git).

## Output Files
- `data/jobs_cleaned.json` → Preprocessed job data.
- `embeddings/` → Contains `.npy` embedding files for jobs & resume.
- `results/top_matches.json` → JSON listing top 10 job matches.

## How to Run
```bash
pip install -r requirements.txt
# or at a minimum
pip install requests sentence-transformers numpy python-dotenv
```
Then run each stage:
`python scripts/scrape_jobs.py`
`python scripts/preprocess.py`
`python scripts/embed_resume.py`
`python scripts/embed_jobs.py`
`python scripts/match_jobs.py`