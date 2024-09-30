# AI Website Scraper

AI Website Scraper is a web-based application that allows you to scrape websites and interact with the content using AI. You can enter a URL to scrape a website, and then use a chatbot interface powered by Ollama to analyze and query the scraped content.

## Features

- Website Scraping: Input a website URL, and the app scrapes the content from the website's body.
- Content Analysis with AI: After scraping, chat with Ollama AI to analyze or extract specific details from the content.
- Interactive UI: View the scraped website content and interact with it in a user-friendly interface.

## Technologies Used
- Python: The core programming language used.
- Streamlit: A fast way to create web apps for machine learning and data science projects.
- Ollama3.2: A conversational AI used to analyze the website content.

## Installation
Make sure you have the following installed on your system:

- Python 3.8+
- pip (Python package installer)

### Steps to Install
Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/AI-Scraper.git
```
Navigate to the project directory:
```bash
cd AI-Scraper
```

Set up a virtual environment (optional but recommended):
```bash
python -m venv ai-scraper-env
source ai-scraper-env/bin/activate  # For Linux/Mac
ai-scraper-env\Scripts\activate     # For Windows
```

Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Usage
Run the application using Streamlit:
```python
streamlit run app.py
```
In the web browser:

- Enter a Website URL: Input the URL of the website you want to scrape.
- Scrape the Website: Click the "Scrape Website" button. The app will scrape the website's content.
- View DOM Content: The scraped content can be viewed in a text area under the "View DOM Content" expander.
- Interact with Ollama: Enter a description of the content you'd like to parse. Click the "Parse Content" button to interact with the AI for content analysis or extraction.
