from telegram import Bot
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')

def publish_to_telegram(news_list):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    for news in news_list:
        bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=news, parse_mode='Markdown')
