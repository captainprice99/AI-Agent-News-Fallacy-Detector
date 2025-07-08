import pandas as pd
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")

if not openai_api_key or not serper_api_key:
    raise ValueError("Missing API keys in .env")

fallacies_df = pd.read_csv("data/fallacies.csv")

llm = ChatOpenAI(
    temperature=0,
    model="gpt-4.1-mini",
    max_tokens=16000,
    openai_api_key=openai_api_key
)