import json
import os
import re 

# Load raw jobs
with open("data/jobs_raw.json", "r", encoding="utf-8") as f:
    raw_jobs = json.load(f)

cleaned_jobs = []

for job in raw_jobs:
    # Extract fields safely
    title = job.get("job_title", "N/A")
    company = job.get("employer_name", "N/A")
    location = job.get("job_city", "N/A")
    description = job.get("job_description", "")

    # Remove HTML/special characters
    clean_description = re.sub(r"<[^>]+>", "", description)
    clean_description = re.sub(r"[^a-zA-Z0-9.,!?()$%\- ]+", " ", clean_description)

    cleaned_jobs.append({
        "title": title,
        "company": company,
        "location": location,
        "description": clean_description.strip()
    })

# Save cleaned output
os.makedirs("data", exist_ok=True)
with open("data/jobs_cleaned.json", "w", encoding="utf-8") as f:
    json.dump(cleaned_jobs, f, indent=2)

print(f"Cleaned {len(cleaned_jobs)} job listings -> data/jobs_cleaned.json")