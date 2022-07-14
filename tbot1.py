import telebot
bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, '''Hello\nwelcome to the crypto-and-stock-market-alert bot\nAvailable options\n \nOptions available in the future\n''')

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, '''Popular questions list ?\n''')



bot.infinity_polling()

