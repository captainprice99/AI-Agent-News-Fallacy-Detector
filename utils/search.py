from langchain_community.utilities import GoogleSerperAPIWrapper
from config.settings import serper_api_key

search = GoogleSerperAPIWrapper(
    type="news",
    tbs="qdr:m1",
    serper_api_key=serper_api_key
)