from fastapi import FastAPI
from dotenv import load_dotenv
import requests
import os
from pydantic import BaseModel
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI app
app = FastAPI()

# Initialize LangChain LLM
llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)

# Base URL for NewsAPI
NEWS_API_URL = "https://eventregistry.org/api/v1/article/getArticles"


# Request Model
class NewsRequest(BaseModel):
    keyword: str
    articlesPage: int = 1
    articlesCount: int = 10


@app.post("/news")
def get_news(request: NewsRequest):
    """Fetches news articles based on a keyword search using NewsAPI."""
    payload = {
        "action": "getArticles",
        "keyword": request.keyword,
        "sourceLocationUri": [
            "http://en.wikipedia.org/wiki/United_States",
            "http://en.wikipedia.org/wiki/Canada",
            "http://en.wikipedia.org/wiki/United_Kingdom"
        ],
        "ignoreSourceGroupUri": "paywall/paywalled_sources",
        "articlesPage": request.articlesPage,
        "articlesCount": request.articlesCount,
        "articlesSortBy": "date",
        "articlesSortByAsc": False,
        "dataType": ["news", "pr"],
        "forceMaxDataTimeWindow": 31,
        "resultType": "articles",
        "apiKey": NEWS_API_KEY
    }

    response = requests.post(NEWS_API_URL, json=payload)

    if response.status_code == 200:
        news_data = response.json()

        # Debugging: Log the entire response to check its structure
        print("News API Response:", news_data)

        # Ensure that we have valid articles in the response
        if "articles" in news_data and isinstance(news_data["articles"], dict):
            articles = news_data["articles"].get("results", [])
        else:
            return {"error": "No articles found or response format is invalid"}

        all_articles = []

        # Process each article
        for article in articles:
            # Check if the article is a dictionary and has the expected keys
            if isinstance(article, dict):
                title = article.get("title", "No title available")
                body = article.get("body", "No content available")
                url = article.get("url", "#")
                image = article.get("image", None)

                # Optional: Summarize the article body
                summary = llm.invoke(f"Summarize the following article: {body}")

                # Add the article with summary, URL, and image to the list
                all_articles.append({
                    "title": title,
                    "summary": summary,
                    "url": url,
                    "image": image
                })

        # Return the list of all articles
        return {"articles": all_articles}

    else:
        return {"error": "Failed to fetch news from API"}