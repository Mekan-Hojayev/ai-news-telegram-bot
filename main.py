from fetch_news import fetch_ai_news
from telegram_bot import publish_to_telegram
import schedule
import time

def job():
    print("Fetching AI news...")
    news = fetch_ai_news()
    if news:
        print(f"Publishing {len(news)} news articles to Telegram...")
        publish_to_telegram(news)
    else:
        print("No news to publish.")

# Schedule the job at midnight
schedule.every().day.at("00:00").do(job)

print("Bot is running...")
while True:
    schedule.run_pending()
    time.sleep(1)
