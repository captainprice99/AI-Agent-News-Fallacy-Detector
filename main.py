from utils.search import search
from utils.loader import load_article_content
from config.settings import fallacies_df
from chains.chain1_summary import chain1
from chains.chain2_review import chain2

def main():
    topic = "global trade"
    search_results = search.results(f"site:whitehouse.gov {topic}")
    article_url = search_results['news'][0]['link']
    article_title = search_results['news'][0]['title']

    article_text = load_article_content(article_url)

    summary = chain1.run(content=article_text, fallacies_df=fallacies_df)
    analysis = chain2.run(summary=summary, fallacies_df=fallacies_df)

    print("Title:", article_title)
    print("URL:", article_url)
    print("\nAnalysis Results:")
    print(analysis)

if __name__ == "__main__":
    main()