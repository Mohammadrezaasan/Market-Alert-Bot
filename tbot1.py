import telebot
import requests
bot = telebot.TeleBot("")
api_price_url = "https://api.nobitex.ir/v2/trades/"
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, '''Hello\nwelcome to the crypto-and-stock-market-alert bot\nAvailable options\n \nOptions available in the future\n''')

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, '''Popular questions list ?\n''')


# get price from nobitex api
@bot.message_handler(commands=['price'])
def send_welcome(message):
	symbol_in = message.text.replace("/price ","")
	

	response = requests.get(api_price_url+symbol_in)
	if response.status_code == 200 :
		response = response.json()
		
		tmp =  + f'{symbol_in} PRICE : ',response['trades'][0]['price']
		bot.reply_to(message,str(tmp).strip("()"))
	else :
		bot.reply_to(message, "server error . try again...")

bot.infinity_polling()