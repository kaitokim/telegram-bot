import telebot

# Ganti token ni dengan token bot Telegram hang
API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello bossku! Bot ni dah ready guna Python.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Hang hantar: {message.text}")

print("Bot sedang berjalan...")
bot.polling()
