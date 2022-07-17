import telebot
import requests
from bs4 import BeautifulSoup
bot = telebot.TeleBot("")
api_price_url = "https://api.nobitex.ir/v2/trades/"
etherscan_url = "https://etherscan.io/tx/"
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message,'''Hello\nwelcome to the crypto-and-stock-market-alert bot\nAvailable options\n \nOptions available in the future\n!!Type the word help for more information!! ''')

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, '''List of information\n !!!  Enter the sentence number to get complete information  !!!\n1-What Is Cryptocurrency?\n2-How does cryptocurrency work?\n3-How to buy cryptocurrency?\n4-How to donate?\n5-Donation addresses\n6-Contact us\n7-live price\n!!!  Contact us for more information  !!!''')

@bot.message_handler(commands=['Donation'])
def send_welcome(message):
	bot.reply_to(message,'''Donation addresses\nUSDT\n(ERC20) 0x2b86081520296021c95577b8ef67463c2875bda6\n(TRC20) TDXNo3ipuVVR8NaQ177HAEqHaeCi6nvdFm\nBTC\n(BTC) 3QRT2gF4jRYcwSnbKpWuQ55hMUoZX9XSLS\nETH\n(ERC20) 0xaf4cc4b431f740fb04325c481af328d7dcd05596\nXRP\n(XRP) rNFugeoj3ZN8Wv6xhuLegUBBPXKCyWLRkB''')

@bot.message_handler(commands=['List'])
def List_of_information1(message):
    List_of_information = {
'1' :'1-What Is Cryptocurrency?\ncryptocurrency is a digital or virtual currency that is secured by cryptography, which makes it nearly impossible to counterfeit or double-spend. Many cryptocurrencies are decentralized networks based on blockchain technology—a distributed ledger enforced by a disparate network of computers. A defining feature of cryptocurrencies is that they are generally not issued by any central authority, rendering them theoretically immune to government interference or manipulation.',

'2':'2-How does cryptocurrency work?\nCryptocurrencies run on a distributed public ledger called blockchain, a record of all transactions updated and held by currency holders.Units of cryptocurrency are created through a process called mining, which involves using computer power to solve complicated mathematical problems that generate coins. Users can also buy the currencies from brokers, then store and spend them using cryptographic wallets.If you own cryptocurrency, you don’t own anything tangible. What you own is a key that allows you to move a record or a unit of measure from one person to another without a trusted third party.Although Bitcoin has been around since 2009, cryptocurrencies and applications of blockchain technology are still emerging in financial terms, and more uses are expected in the future. Transactions including bonds, stocks, and other financial assets could eventually be traded using the technology.',

'3':'3-How to buy cryptocurrency?\n1- Do thorough research on crypto to better understand crypto.\n2- Choose a reliable exchange where you can buy cryptocurrencies.\n3- After choosing an exchange and creating an account in it, you can deposit the amount of money you want to invest in cryptocurrencies into your account.\n4- To invest in currencies, be sure to do a thorough research on the currency you want to invest in.\n5- And finally, to store your currencies, you can use the digital wallet that you have in your exchange account or use different digital wallets that you install as an application on your device(before using the wallet do enough research on it).',

'4':'4-How to donate?\n1- Select your desired currency, for example (BTC).\n2- Enter the wallet address to which you want to deposit.\n3- Make sure that the currency network, for example (TRC 20), is similar to the currency network you want to deposit.\n4- Finally, choose the amount of currency you want to deposit and complete the confirmation process.',

'5':'5-Donation addresses\nUSDT\n(ERC20) 0x2b86081520296021c95577b8ef67463c2875bda6\n(TRC20) TDXNo3ipuVVR8NaQ177HAEqHaeCi6nvdFm\nBTC\n(BTC) 3QRT2gF4jRYcwSnbKpWuQ55hMUoZX9XSLS\nETH\n(ERC20) 0xaf4cc4b431f740fb04325c481af328d7dcd05596\nXRP\n(XRP) rNFugeoj3ZN8Wv6xhuLegUBBPXKCyWLRkB',

'6':'6-Contact us\nWhatsApp : +989906678506\nTelegram : @marketalertbotsupport\nEmail : cryptoandstockmarketalert@gmail.com\nEducation and News channel : ',

'7':'7-live price\nTo get the current price of the desired currency, enter the word price and the name of the desired currency, such as (price btcusd).',

'8':'8-tx_hash\nReview of successful and unsuccessful transactions (ERC20).',
}

    a = message.text.replace('/List ','')
    if a in List_of_information :
        bot.reply_to(message,List_of_information[a]) 
	


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