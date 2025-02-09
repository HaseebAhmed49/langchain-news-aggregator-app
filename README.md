# AI-Powered News Aggregator

## 📌 Project Overview
The **AI-Powered News Aggregator** is a web application that fetches the latest news articles based on user-input keywords. It leverages **FastAPI** for the backend and **Streamlit** for the frontend. The backend integrates **LangChain** and **OpenAI GPT-3.5** to provide AI-powered summaries.

---
## Project Structure

```sh
news-aggregator-app/
│── backend/  
│   ├── main.py       # FastAPI backend with LangChain  
│   ├── .env          # API keys 
│── frontend/  
│   ├── app.py        # Streamlit frontend with AI summaries  
│── requirements.txt  # Dependencies  
│── README.md         # Project documentation
```

---
## Technologies Used
* **FastAPI** for backend API
* **Streamlit** for frontend UI
* **LangChain** for AI-based responses
* **OpenAI GPT-3.5-turbo** for summarization of content

---
## 📌 Prerequisites
Ensure you have the following installed on your system:
- **Python 3.13+**
- **pip** (Python package manager)

---
## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/haseebahmed49/langchain-news-aggregator-app.git
cd langchain-news-aggregator-app
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add your OpenAI API key:
```sh
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
echo "NEWS_API_KEY=your_news_api_key_here" > .env
```

---
## 🖥 Backend (FastAPI)

### 📌 Start the FastAPI Server
Run the backend using:
```sh
uvicorn backend.main:app --reload
```
The API will be available at `http://127.0.0.1`.
## Backend (FastAPI) - main.py

### Functionality:
- Uses FastAPI to create an API that fetches news from EventRegistry.
- Calls OpenAI's GPT-3.5 model via LangChain for AI-based summaries.
- Handles news filtering by location and keyword.

### API Endpoints:
#### 1. Fetch News Articles
**POST /news** - Fetches news articles based on a keyword.


---
## 🎨 Frontend (Streamlit)

### 📌 Run the Streamlit App
```sh
streamlit run app.py
```

### Functionality:
- Accepts user input for keywords and article count.
- Calls the FastAPI backend to fetch articles.
- Displays articles with titles, descriptions, and images.
- Provides a "Read More" link to the full article.

### Key Features:
- Interactive UI with Streamlit.
- Real-time news fetching based on user input.
- Error handling for API failures.

---
## Application View
![Screen Shot 2025-02-09 at 15 12 41 PM](https://github.com/user-attachments/assets/1b0992e3-5f0d-4a24-a1bd-80e2909c60f5)
![Screen Shot 2025-02-09 at 15 13 30 PM](https://github.com/user-attachments/assets/c94dad27-77b7-4da5-b350-bf4b110f4a66)
![Screen Shot 2025-02-09 at 15 13 44 PM](https://github.com/user-attachments/assets/45be4f34-e87b-4bbb-b152-71faeed1fa5f)


## 📜 License
This project is licensed under the MIT License.

---
## Contact
For any queries or issues, feel free to reach out:
* Email: haseebahmed02@gmail.com
* GitHub: https://github.com/HaseebAhmed49

💡 **Happy Coding!** 🚀

