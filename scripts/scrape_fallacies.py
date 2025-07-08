import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = "https://en.wikipedia.org/wiki/List_of_fallacies"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

fallacies = []

content = soup.find('div', {'class': 'mw-parser-output'})

for ul in content.find_all("ul"):
    for li in ul.find_all("li", recursive=False):
        text = li.get_text().strip()

        if not text or len(text.split()) < 2:
            continue

        if ":" in text:
            name, desc = text.split(":", 1)
        elif "–" in text:
            name, desc = text.split("–", 1)
        else:
            name, desc = text, ""
        
        fallacies.append({
            "fallacy_name": name.strip(),
            "description": desc.strip()
        })
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
csv_path = os.path.join(DATA_DIR, "fallacies.csv")
df = pd.DataFrame(fallacies)
df.to_csv(csv_path, index=False)

print(f"✅ Scraped {len(df)} fallacies.")