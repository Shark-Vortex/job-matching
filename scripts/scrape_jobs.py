import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")

url = "https://jsearch.p.rapidapi.com/search"
querystring = {"query": "computer science, St. Louis", "page": "1", "num_pages": "2"}

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    jobs = response.json().get("data", [])
    os.makedirs("data", exist_ok=True)
    with open("data/jobs_raw.json", "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2)
    print(f"Saved {len(jobs)} job listings to data/jobs_raw.json")
else:
    print(f"Request failed: {response.status_code}")
    print(response.text)