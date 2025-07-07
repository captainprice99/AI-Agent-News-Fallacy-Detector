import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_fallacies"

# Make the request and parse the HTML
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

fallacies = []

# Find all sections that contain fallacy definitions
for header in soup.find_all(['h2', 'h3']):
    ul = header.find_next_sibling("ul")
    if not ul:
        continue

    for li in ul.find_all("li", recursive=False):
        text = li.get_text().strip()
        if not text:
            continue

        # Split on the dash or colon if present
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

# Create and save DataFrame
df = pd.DataFrame(fallacies)
df.to_csv("data/fallacies.csv", index=False)

print(f"✅ Scraped {len(df)} fallacies.")