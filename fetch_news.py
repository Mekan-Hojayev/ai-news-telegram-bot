import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def fetch_ai_news():
    # URL to scrape
    url = "https://www.artificialintelligence-news.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract news articles
    articles = soup.find_all('article', class_='item')[:15]  # Top 15 articles
    news_list = []

    for article in articles:
        try:
            title = article.find('h3').text.strip()
            link = article.find('a')['href']
            summary = article.find('div', class_='post-excerpt').text.strip()
            news_list.append(f"**{title}**\n{summary}\n[Read more]({link})")
        except AttributeError:
            continue

    return news_list
