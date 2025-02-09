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
        return response.json()
    return {"error": "Failed to fetch news"}