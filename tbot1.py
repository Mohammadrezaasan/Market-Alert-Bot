from telebot import TeleBot
from telebot import types
from markupsafe import Markup
from rsa import PublicKey
import requests
from config import *
from bs4 import BeautifulSoup
from web3 import Web3
import json
from decimal import *
'------------------------------------------------------------------------------------------------------------------------------------'
bot = TeleBot("Token")
api_price_url = "https://api.nobitex.ir/v2/trades/"
etherscan_url = "https://etherscan.io/tx/"
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['start'])
def test2(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    Introducing_the_robot  = types.KeyboardButton('/Introducing the robot 🤖')
    if_you_need_more_information_connecte_us  = types.KeyboardButton('/if you need more information 🗂 \n📨 connect us 📨')
    click_here_to_find_out_what_each_keyword_does = types.KeyboardButton('/Click here to find out what each keyword does 🗝')
    click_here_to_open_the_list_of_keywords_for_you = types.KeyboardButton('/click here to open the list of keywords for you 📓')
    markup.row(Introducing_the_robot)
    markup.row(if_you_need_more_information_connecte_us)
    markup.row(click_here_to_find_out_what_each_keyword_does)
    markup.row(click_here_to_open_the_list_of_keywords_for_you)
    bot.send_message(chat_id, "Hello 🙋🏻‍♂️\nwelcome to the market-alert bot👾", reply_markup=markup)
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['Return'])
def test2(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    Introducing_the_robot  = types.KeyboardButton('/Introducing the robot 🤖')
    if_you_need_more_information_connecte_us  = types.KeyboardButton('/if you need more information 🗂 \n📨 connect us 📨')
    click_here_to_find_out_what_each_keyword_does = types.KeyboardButton('/Click here to find out what each keyword does 🗝')
    click_here_to_open_the_list_of_keywords_for_you = types.KeyboardButton('/click here to open the list of keywords for you 📓')
    markup.row(Introducing_the_robot)
    markup.row(if_you_need_more_information_connecte_us)
    markup.row(click_here_to_find_out_what_each_keyword_does)
    markup.row(click_here_to_open_the_list_of_keywords_for_you)
    bot.send_message(chat_id, "Return to main page was successful ✅", reply_markup=markup)
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['Click'])
def send_message(message):
    bot.reply_to(message,'Introducing the robot 🤖 :\nWith the help of this key 🗝 , you can recognize the robot and a little explanation is given about the robot.\nif you need more information 🗂 \n📨 connecte us 📨 :\nThis key shows you the ways to communicate with us 📡\nclick here to open the list of keywords for you 📓 : \nIt will show you a list of keywords 🗒' )
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['Introducing'])
def send_message(message):
    bot.reply_to(message,"Hello, my name is market alert bot 🤖\nI can tell you the current price of major currencies in the crypto market with just a few simple clicks 🚀\nAnd I can also check with the transaction hash whether your transfer was successful  ✅or not❌. Just a few simple clicks and enter your transaction hash, that's it.\nAnd you can use the information list 📒 to find the right answer to your questions\nAnd if you don't find your answer in that list, you can contact us 📬with just one click 🖱")
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['if'])
def send_message(message):
    bot.reply_to(message,'🟢 WhatsApp : +989906678506\n🔵 Telegram : @marketalertbotsupport\n📧 Email : cryptoandstockmarketalert@gmail.com')
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['click'])
def test2(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    donation   = types.KeyboardButton('/donation 💸')
    List_of_information  = types.KeyboardButton('/List of information 📒')
    price   = types.KeyboardButton('/price 💵')
    tx_hash_check  = types.KeyboardButton('/tx_hash check 👨🏻‍💻')
    send_eth_ERC20  = types.KeyboardButton('/send ETH(ERC20) 💸')
    Return_to_main_page = types.KeyboardButton(' /Return to main page ↩️')
    markup.row(donation,price)
    markup.row(List_of_information,tx_hash_check,send_eth_ERC20)
    markup.row(Return_to_main_page)
    bot.send_message(chat_id, "Keyword list opened successfully ✅", reply_markup=markup)
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['donation'])
def test2(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    BTC  = types.KeyboardButton('/Donation BTC(BTC)💸')
    BUSD = types.KeyboardButton('/Donation BUSD(ETH)\n💸')
    XRP  = types.KeyboardButton('/Donation XRP(XRP)\n💸')
    USDC = types.KeyboardButton('/Donation USDC(MATIC)\n💸')
    BNB  = types.KeyboardButton('/Donation BNB(BNB)💸')
    USDT = types.KeyboardButton('/Donation USDT(ETH)\n💸')
    ETH  = types.KeyboardButton('/Donation ETH(ETH)💸')
    Return_to_main_page = types.KeyboardButton('/Return to main page ↩️')
    Return_to_the_previous_page = types.KeyboardButton('/Return_to the previous page 🔙')
    markup.row(BTC,ETH,BNB)
    markup.row(BUSD,USDT,USDC,XRP)
    markup.row(Return_to_main_page,Return_to_the_previous_page)
    bot.send_message(chat_id, "The list of currencies available for donation .\nopened successfully ✅", reply_markup=markup)
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['Return_to'])
def test2(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    donation   = types.KeyboardButton('/donation 💸')
    List_of_information  = types.KeyboardButton('/List of information 📒')
    price   = types.KeyboardButton('/price 💵')
    tx_hash_check  = types.KeyboardButton('/tx_hash check 👨🏻‍💻')
    send_eth_ERC20  = types.KeyboardButton('/send ETH(ERC20) 💸')
    Return_to_main_page = types.KeyboardButton(' /Return to main page ↩️')
    markup.row(donation,price)
    markup.row(List_of_information,tx_hash_check,send_eth_ERC20)
    markup.row(Return_to_main_page)
    bot.send_message(chat_id, "Return to the previous page successfully ✅", reply_markup=markup)
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['Donation'])
def send_welcome(message):
    
    Addresses = {
'BTC(BTC)💸' :"🔴 Address :\nbc1qwsnghp2nmqytejnf0xv2tlse5hfg3uzpal3868",
'ETH(ETH)💸' :"🔴 Address :\n0x7B075A1c07e05d3542c13e56A61b63Da91125171",
'BNB(BNB)💸' :"🔴 Address :\nbnb16m655nnxxj8vdv08tj74u3v7uazkspqyjnam5r",
'XRP(XRP)\n💸' :"🔴 Address :\nrnqe3zNxe8nkJhDQNyBBnGmVJw7NVmi2dB",
'BUSD(ETH)\n💸' :"🔴 Address :\n0x7B075A1c07e05d3542c13e56A61b63Da91125171",
'USDT(ETH)\n💸' :"🔴 Address :\n0x7B075A1c07e05d3542c13e56A61b63Da91125171",
'USDC(MATIC)\n💸' :"🔴 Address :\n0x7B075A1c07e05d3542c13e56A61b63Da91125171"
}
    photos ={
'BTC(BTC)💸' : open("C:\\Users\\****\\OneDrive\\Desktop\\btc.jpg",'rb'),
'ETH(ETH)💸' : open("C:\\Users\\****\\OneDrive\\Desktop\\eth.jpg",'rb'),
'BNB(BNB)💸' : open("C:\\Users\\****\\OneDrive\\Desktop\\bnb.jpg",'rb'),
'XRP(XRP)\n💸' : open("C:\\Users\\****\\OneDrive\\Desktop\\xrp.jpg",'rb'),
'BUSD(ETH)\n💸' : open("C:\\Users\\****\\OneDrive\\Desktop\\busd.jpg",'rb'),
'USDT(ETH)\n💸' : open("C:\\Users\\****\\OneDrive\\Desktop\\usdt-eth network.jpg",'rb'),
'USDC(MATIC)\n💸' : open("C:\\Users\\****\\OneDrive\\Desktop\\usdc.jpg",'rb')
}
   

    d =message.text.replace('/Donation ','')
    if d in Addresses :
        bot.send_photo(message.chat.id,photos[d] ,caption=Addresses[d])
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['price'])
def test2(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    IRT = types.KeyboardButton('/IRT currency 🇮🇷 ')
    USDT = types.KeyboardButton('/USDT currency 🇺🇸')
    Choose = types.KeyboardButton('👇🏻👇🏻 Choose one of the two options below according to your desired currency 👇🏻👇🏻')
    Return_to_main_page = types.KeyboardButton('/Return to main page ↩️')
    Return_to_the_previous_page = types.KeyboardButton('/Return_to the previous page 🔙')
    markup.row(Choose)
    markup.row(IRT,USDT)
    markup.row(Return_to_main_page,Return_to_the_previous_page)

    bot.send_message(chat_id, "List of currencies opened successfully ✅", reply_markup=markup) 
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['IRT'])
def test2(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    START = types.KeyboardButton('🪙🪙 Available currencies 19 🪙🪙')
    BTCIRT = types.KeyboardButton('/Price BTCIRT')
    ETHIRT = types.KeyboardButton('/Price ETHIRT')
    LTCIRT = types.KeyboardButton('/Price LTCIRT')
    XRPIRT = types.KeyboardButton('/Price XRPIRT')
    BCHIRT = types.KeyboardButton('/Price BCHIRT')
    BNBIRT = types.KeyboardButton('/Price BNBIRT')
    EOSIRT = types.KeyboardButton('/Price EOSIRT')
    XLMIRT = types.KeyboardButton('/Price XLMIRT')
    ETCIRT = types.KeyboardButton('/Price ETCIRT')
    TRXIRT = types.KeyboardButton('/Price TRXIRT')
    DOGIRT = types.KeyboardButton('/Price DOGEIRT')
    UNIIRT = types.KeyboardButton('/Price UNIIRT')
    DAIIRT = types.KeyboardButton('/Price DAIIRT')
    LINKIRT = types.KeyboardButton('/Price LINKIRT')
    DOTIRT = types.KeyboardButton('/Price DOTIRT')
    AAVEIRT = types.KeyboardButton('/Price AAVEIRT')
    ADAIRT = types.KeyboardButton('/Price ADAIRT')
    SHIBIRT = types.KeyboardButton('/Price SHIBIRT')
    USDTIRT = types.KeyboardButton('/Price USDTIRT')
    Return_to_main_page = types.KeyboardButton('/Return to main page ↩️')
    Return_to_the_previous_page = types.KeyboardButton('/Return_to_the previous page 🔙')
    markup.row(START)
    markup.row(USDTIRT,BTCIRT,ETHIRT,BNBIRT)
    markup.row(BCHIRT,EOSIRT,XLMIRT,LTCIRT,ETCIRT) 
    markup.row(TRXIRT,DOGIRT,UNIIRT,DAIIRT,LINKIRT)
    markup.row(XRPIRT,DOTIRT,AAVEIRT,ADAIRT,SHIBIRT)
    markup.row(Return_to_main_page,Return_to_the_previous_page)
    bot.send_message(chat_id, "List of currencies by IRT opened successfully ✅", reply_markup=markup) 
	
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['USDT'])
def test2(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    START = types.KeyboardButton('🪙🪙 Available currencies 18 🪙🪙')
    BTCIRT = types.KeyboardButton('/Price BTCUSDT')
    ETHIRT = types.KeyboardButton('/Price ETHUSDT')
    LTCIRT = types.KeyboardButton('/Price LTCUSDT')
    XRPIRT = types.KeyboardButton('/Price XRPUSDT')
    BCHIRT = types.KeyboardButton('/Price BCHUSDT')
    BNBIRT = types.KeyboardButton('/Price BNBUSDT')
    EOSIRT = types.KeyboardButton('/Price EOSUSDT')
    XLMIRT = types.KeyboardButton('/Price XLMUSDT')
    ETCIRT = types.KeyboardButton('/Price ETCUSDT')
    TRXIRT = types.KeyboardButton('/Price TRXUSDT')
    DOGIRT = types.KeyboardButton('/Price DOGEUSDT')
    UNIIRT = types.KeyboardButton('/Price UNIUSDT')
    DAIIRT = types.KeyboardButton('/Price DAIUSDT')
    LINKIRT = types.KeyboardButton('/Price LINKUSDT')
    DOTIRT = types.KeyboardButton('/Price DOTUSDT')
    AAVEIRT = types.KeyboardButton('/Price AAVEUSDT')
    ADAIRT = types.KeyboardButton('/Price ADAUSDT')
    SHIBIRT = types.KeyboardButton('/Price SHIBUSDT')
   
    Return_to_main_page = types.KeyboardButton('/Return to main page ↩️')
    Return_to_the_previous_page = types.KeyboardButton('/Return_to_the previous page 🔙')
    markup.row(START)
    markup.row(BTCIRT,ETHIRT,BNBIRT)
    markup.row(BCHIRT,EOSIRT,XLMIRT,LTCIRT,ETCIRT) 
    markup.row(TRXIRT,DOGIRT,UNIIRT,DAIIRT,LINKIRT)
    markup.row(XRPIRT,DOTIRT,AAVEIRT,ADAIRT,SHIBIRT)
    markup.row(Return_to_main_page,Return_to_the_previous_page)
    bot.send_message(chat_id, "List of currencies by USDT opened successfully ✅", reply_markup=markup) 
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['Return_to_the'])
def test2(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    IRT = types.KeyboardButton('/IRT currency 🇮🇷 ')
    USDT = types.KeyboardButton('/USDT currency 🇺🇸')
    Choose = types.KeyboardButton('👇🏻👇🏻 Choose one of the two options below according to your desired currency 👇🏻👇🏻')
    Return_to_main_page = types.KeyboardButton('/Return to main page ↩️')
    Return_to_the_previous_page = types.KeyboardButton('/Return_to the previous page 🔙')
    markup.row(Choose)
    markup.row(IRT,USDT)
    markup.row(Return_to_main_page,Return_to_the_previous_page)

    bot.send_message(chat_id, "List of currencies opened successfully ✅", reply_markup=markup) 
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['Price'])
def get_price(message):
	symbol_in = message.text.replace("Price ","")
	

	response = requests.get(api_price_url+symbol_in)
	if response.status_code == 200 :
		response = response.json()
		
		tmp = '🪙🪙' + f'{symbol_in} PRICE : ',response['trades'][0]['price'] +'🪙🪙'
		bot.reply_to(message,str(tmp).strip("(')"))
	else :
		bot.reply_to(message, "server error . try again...")
   
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['List'])
def test2(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    START = types.KeyboardButton('/1-What Is Cryptocurrency? 🤔')
    start1 = types.KeyboardButton('/2-How does cryptocurrency work? 🤯')
    start3 = types.KeyboardButton('/3-How to buy cryptocurrency? 😎')
    start4 =types.KeyboardButton('/4-How to donate? 🤑')
    if_you_need_more_information_connecte_us  = types.KeyboardButton('/if you need more information 🗂 \n📨 connect us 📨')
    Return_to_main_page = types.KeyboardButton('/Return to main page ↩️')
    Return_to_the_previous_page = types.KeyboardButton('/Return_to the previous page 🔙')
    markup.row(START,start1)
    markup.row(start3,start4)
    markup.row(if_you_need_more_information_connecte_us)
    markup.row(Return_to_main_page,Return_to_the_previous_page)
    bot.send_message(chat_id, "List of information opened successfully ✅", reply_markup=markup) 


'------------------------------------------------------------------------------------------------------------------------------------'

@bot.message_handler(commands=['1-What'])
def send_message(message):
    List_of_information = {
'1' :'1-What Is Cryptocurrency?\ncryptocurrency is a digital or virtual currency that is secured by cryptography, which makes it nearly impossible to counterfeit or double-spend. Many cryptocurrencies are decentralized networks based on blockchain technology—a distributed ledger enforced by a disparate network of computers. A defining feature of cryptocurrencies is that they are generally not issued by any central authority, rendering them theoretically immune to government interference or manipulation.'
}
    bot.reply_to(message,List_of_information['1'])   
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['2-How'])
def send_message(message):
    List_of_information = {
'2' :'2-How does cryptocurrency work?\nCryptocurrencies run on a distributed public ledger called blockchain, a record of all transactions updated and held by currency holders.Units of cryptocurrency are created through a process called mining, which involves using computer power to solve complicated mathematical problems that generate coins. Users can also buy the currencies from brokers, then store and spend them using cryptographic wallets.If you own cryptocurrency, you don’t own anything tangible. What you own is a key that allows you to move a record or a unit of measure from one person to another without a trusted third party.Although Bitcoin has been around since 2009, cryptocurrencies and applications of blockchain technology are still emerging in financial terms, and more uses are expected in the future. Transactions including bonds, stocks, and other financial assets could eventually be traded using the technology.'
}
    bot.reply_to(message,List_of_information['2'])
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['3-How'])
def send_message(message):
    List_of_information = {
    '3':'3-How to buy cryptocurrency?\n1- Do thorough research on crypto to better understand crypto.\n2- Choose a reliable exchange where you can buy cryptocurrencies.\n3- After choosing an exchange and creating an account in it, you can deposit the amount of money you want to invest in cryptocurrencies into your account.\n4- To invest in currencies, be sure to do a thorough research on the currency you want to invest in.\n5- And finally, to store your currencies, you can use the digital wallet that you have in your exchange account or use different digital wallets that you install as an application on your device(before using the wallet do enough research on it).',
}
    bot.reply_to(message,List_of_information['3'])
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['4-How'])
def send_message(message):
    List_of_information = {
    '3':'4-How to donate?\n1- Select your desired currency, for example (BTC).\n2- Enter the wallet address to which you want to deposit.\n3- Make sure that the currency network, for example (TRC 20), is similar to the currency network you want to deposit.\n4- Finally, choose the amount of currency you want to deposit and complete the confirmation process.',
}
    bot.reply_to(message,List_of_information['3'])
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['tx_hash'])
def test2(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    START = types.KeyboardButton('👇🏻👇🏻 To check, follow the text below 👇🏻👇🏻')
    start2 = types.KeyboardButton('🔴🔴 Tx_hash Enter Tx_hash here 🔴🔴\nfor example : Tx_hash r5wv5w56bw568n5k85w8m88w67w')
    start1 = types.KeyboardButton('👆🏻👆🏻 Type the above text and put tx_hash in the part where it is written 👆🏻👆🏻')
    Return_to_main_page = types.KeyboardButton('/Return to main page ↩️')
    Return_to_the_previous_page = types.KeyboardButton('/Return_to the previous page 🔙')
    markup.row(START)
    markup.row(start2)
    markup.row(start1)
    markup.row(Return_to_main_page,Return_to_the_previous_page)
    bot.send_message(chat_id, "List of information opened successfully ✅", reply_markup=markup) 
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['Tx_hash'])
def check_transaction(message):
	tx_hash = message.text.replace("/Tx_hash ","") 
    
	response = requests.post(etherscan_url+tx_hash,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
	if response.status_code == 200:
		soup = BeautifulSoup(response.text , 'html.parser')
		status_result = str(soup.find_all("span", {"class": "u-label u-label--sm u-label--value u-label--success rounded"})).count("Success")
		if status_result == 1:
			bot.reply_to(message,("Transaction success"))
		else :
			bot.reply_to(message,("Transaction failed"))
	else :
		bot.reply_to(message,("status code : ",response.status_code))
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['send'])
def send_message(message):
    bot.reply_to(message,'coming soon ....')
'------------------------------------------------------------------------------------------------------------------------------------'
#The project has been completed ✅

bot.infinity_polling()


