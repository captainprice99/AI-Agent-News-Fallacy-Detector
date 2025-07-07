from langchain_community.document_loaders import WebBaseLoader

def load_article_content(url, max_chars=3000):
    loader = WebBaseLoader(url)
    content = loader.load()[0].page_content
    return ' '.join(content[:max_chars].split())