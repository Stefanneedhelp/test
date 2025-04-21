import os
from telegram import Bot

print("✅ Test skripta pokrenuta")

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("🔐 BOT_TOKEN:", BOT_TOKEN)
print("🔐 CHAT_ID:", CHAT_ID)

if not BOT_TOKEN or not CHAT_ID:
    raise ValueError("❌ BOT_TOKEN ili CHAT_ID nisu postavljeni!")

bot = Bot(token=BOT_TOKEN)

try:
    bot.send_message(chat_id=CHAT_ID, text="✅ Test poruka je uspešno poslata sa Render-a!")
    print("📤 Poruka je poslata!")
except Exception as e:
    print("❌ GREŠKA PRI SLANJU:", e)
