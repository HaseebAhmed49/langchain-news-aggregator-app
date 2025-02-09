import streamlit as st
import requests

# Streamlit page configuration
st.set_page_config(page_title="AI-Powered News Aggregator", layout="wide")

# App title
st.title("📰 AI-Powered News Aggregator")

# User inputs keyword and number of articles
keyword = st.text_input("Enter a keyword (e.g., Tesla Inc):")
if not keyword:
    st.error("Enter Keyword for News you're looking for")
articles_count = st.slider("Select number of articles:", 1, 50, 10)

# Button to fetch news
if st.button("Get News"):
    response = requests.post("http://127.0.0.1:8000/news", json={"keyword": keyword, "articlesCount": articles_count})

    if response.status_code == 200:
        # Correctly access the article response
        news_data = response.json()
        articles = news_data["articles"]

        # Check if response contains an error message
        if "error" in news_data:
            st.error(news_data["error"])
            st.stop()

        # If no articles found, show a warning
        if not news_data:
            st.warning("No news articles found.")
        else:
            for article in articles:
                title = article.get("title", "No title available")
                summary = article.get("summary", "No summary available")  # Get the summary
                url = article.get("url", "#")
                image = article.get("image", None)

                # Display title, summary, and URL
                st.subheader(title)
                st.write(f"**Summary**: {summary['content']}")
                st.write(f"[Read more]({url})")

                if image:
                    st.image(image, width=600)

                st.markdown("---")
    else:
        st.error("Failed to fetch news. Check API status.")