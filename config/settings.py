import os
import pandas as pd
from langchain_openai import ChatOpenAI

openai_api_key = os.environ["OPENAI_API_KEY"]
serper_api_key = os.environ["SERPER_API_KEY"]

# Load fallacies
fallacies_df = pd.read_csv('data/fallacies.csv')

# Model setup
llm = ChatOpenAI(
    temperature=0,
    model='gpt-4.1-mini',
    max_tokens=16000,
    openai_api_key=openai_api_key
)