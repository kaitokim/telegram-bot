import telebot

# Ganti token ni dengan token bot Telegram hang
API_TOKEN = '7698894838:AAE30Z3gxc_ZSEbeva_E gQi7oHbqBtDeP-E'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello bossku! Bot ni dah ready guna Python.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Hang hantar: {message.text}")

print("Bot sedang berjalan...")
bot.polling()
