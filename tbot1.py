from click import command
import telebot
import requests
from bs4 import BeautifulSoup
bot = telebot.TeleBot("")
api_price_url = "https://api.nobitex.ir/v2/trades/"
etherscan_url = "https://etherscan.io/tx/"
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, '''Hello\nwelcome to the crypto-and-stock-market-alert bot\nAvailable options\n \nOptions available in the future\n''')

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, '''Popular questions list ?\n''')


# get price from nobitex api
@bot.message_handler(commands=['price'])
def get_price(message):
	symbol_in = message.text.replace("/price ","")
	

	response = requests.get(api_price_url+symbol_in)
	if response.status_code == 200 :
		response = response.json()
		
		tmp =  + f'{symbol_in} PRICE : ',response['trades'][0]['price']
		bot.reply_to(message,str(tmp).strip("()"))
	else :
		bot.reply_to(message, "server error . try again...")

@bot.message_handler(commands=['tx_hash'])
def check_transaction(message):
	tx_hash = message.text.replace("/tx_hash ","")
	response = requests.post(etherscan_url+tx_hash,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
	if response.status_code == 200:
		soup = BeautifulSoup(response.text , 'html.parser')
		status_result = str(soup.find_all("span", {"class": "u-label u-label--sm u-label--value u-label--success rounded"})).count("Success")
		if status_result == 1:
			print("Transaction success")
		else :
			print("Transaction failed")
	else :
		print(print("status code : ",response.status_code))

bot.infinity_polling()