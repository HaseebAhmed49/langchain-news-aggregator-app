import streamlit as st
import requests

# Streamlit page configuration
st.set_page_config(page_title="AI-Powered News Aggregator", layout="wide")

# App title
st.title("📰 AI-Powered News Aggregator")

# User inputs keyword and number of articles
keyword = st.text_input("Enter a keyword (e.g., Tesla Inc):", "Tesla Inc")
articles_count = st.slider("Select number of articles:", 1, 50, 10)

# Button to fetch news
if st.button("Get News"):
    response = requests.post("http://127.0.0.1:8000/news", json={"keyword": keyword, "articlesCount": articles_count})

    if response.status_code == 200:
        # Correctly access the articles list inside "results"
        news_data = response.json()

        # Check if response contains "articles" and "results"
        if isinstance(news_data, dict) and "articles" in news_data and "results" in news_data["articles"]:
            articles = news_data["articles"]["results"]  # Correct way to access articles
        else:
            st.error("Unexpected response format. No 'articles' found.")
            st.stop()

        # If no articles found, show a warning
        if not articles:
            st.warning("No news articles found.")
        else:
            for article in articles:
                title = article.get("title", "No title available")
                description = article.get("body", "No content available")[:500]
                url = article.get("url", "#")
                image = article.get("image", None)

                st.subheader(title)
                st.write(description)
                st.write(f"[Read more]({url})")

                if image:
                    st.image(image, width=600)

                st.markdown("---")
    else:
        st.error("Failed to fetch news. Check API status.")