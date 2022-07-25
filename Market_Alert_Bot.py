from telebot import TeleBot
from telebot import types
import telebot
from telebot import types
from markupsafe import Markup
from rsa import PublicKey
import requests
from bs4 import BeautifulSoup
from web3 import Web3
import json
from decimal import *
from config import *
'------------------------------------------------------------------------------------------------------------------------------------'
bot = telebot.TeleBot("Token")
api_price_url = "https://api.nobitex.ir/v2/trades/"
etherscan_url = "https://etherscan.io/tx/"
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['start'])
def handle_start(message):
   chat_id = message.chat.id 
   markup = telebot.types.ReplyKeyboardMarkup(True, False)
   markup.row('🤖 Introducing the robot 🤖')
   markup.row('🗂 if you need more information 🗂 \n📨 contact us 📨')
   markup.row('🗝 Click here to find out what each keyword does 🗝')
   markup.row('📓 click here to open the list of keywords for you 📓')
   bot.send_message(chat_id,'Hello 🙋🏻‍♂️\nwelcome to the market-alert bot👾', reply_markup=markup)
   
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == '🤖 Introducing the robot 🤖':
        bot.reply_to(message,"Hello, my name is market alert bot 🤖\nI can tell you the current price of major currencies in the crypto market with just a few simple clicks 🚀\nAnd I can also check with the transaction hash whether your transfer was successful  ✅or not❌. Just a few simple clicks and enter your transaction hash, that's it.\nAnd you can use the information list 📒 to find the right answer to your questions\nAnd if you don't find your answer in that list, you can contact us 📬with just one click 🖱")
       
    elif message.text == '🗂 if you need more information 🗂 \n📨 contact us 📨':
        bot.reply_to(message,'🟢 WhatsApp : +989906678506\n🔵 Telegram : @marketalertbotsupport\n📧 Email : cryptoandstockmarketalert@gmail.com')
    
    elif message.text == '🗝 Click here to find out what each keyword does 🗝':
        bot.reply_to(message,"🤖 Introducing the robot 🤖 :\nWith the help of this key 🗝 , you can recognize the robot and a little explanation is given about the robot.\n🗂 if you need more information 🗂 \n📨 connecte us 📨 :\nThis key shows you the ways to communicate with us 📡\n📓 click here to open the list of keywords for you 📓 : \nIt will show you a list of keywords 🗒\n💸 donation 💸 : With the help of this key, a list of available currencies for donation will be opened, and by clicking on the desired currency, you will receive its address and QR code.\nReturn to the previous page 🔙 : You can go back to the previous page using this key .\nReturn to main page ↩️ : You can return to the main page using this key.\n💵 Cryptocurrency price 💵 : By clicking on this button, a list will open for you in which two options will be displayed for you, you can choose one according to your desired currency and then click on the desired option from the two options. Choose one. Click on the currency you want and a list of available currencies will open for you to request a price. Click on any of them and you will get the price of the currency you want.\n📒 List of information 📒 : When you click on this button, a list of information will open for you, and you will get the answer to your question by clicking on the question you want.\n👨🏻‍💻 tx_hash check(ERC20) 👨🏻‍💻 : By using this key and following the instructions, you can enter your address and check it and make sure that the operation is done correctly.\n💸 send ETH(ERC20) 💸 : coming soon .... ")
        
    elif message.text == '📓 click here to open the list of keywords for you 📓' : 
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('💸 donation 💸','💵 Cryptocurrency price 💵')
        markup.row('📒 List of information 📒','👨🏻‍💻 tx_hash check(ERC20) 👨🏻‍💻','💸 send ETH(ERC20) 💸')
        markup.row('Return to main page ↩️')
        bot.send_message(chat_id,'Keyword list opened successfully ✅', reply_markup=markup )
    
    elif message.text == 'Return to main page ↩️' : 
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('🤖 Introducing the robot 🤖')
        markup.row('🗂 if you need more information 🗂 \n📨 contact us 📨')
        markup.row('🗝 Click here to find out what each keyword does 🗝')
        markup.row('📓 click here to open the list of keywords for you 📓')
        bot.send_message(chat_id,'Return to main page was successful ✅', reply_markup=markup)

    elif message.text == '💸 donation 💸' : 
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('Donation BTC(BTC)💸','Donation ETH(ETH)💸','Donation BNB(BNB)💸')
        markup.row('Donation BUSD(ETH)\n💸','Donation XRP(XRP)\n💸','Donation USDC(MATIC)\n💸','Donation USDT(ETH)\n💸')
        markup.row('Return to main page ↩️','Return to the previous page 🔙')
        bot.send_message(chat_id,'The list of currencies available for donation .\nopened successfully ✅', reply_markup=markup)
    
    elif message.text == 'Return to the previous page 🔙' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('💸 donation 💸','💵 Cryptocurrency price 💵')
        markup.row('📒 List of information 📒','👨🏻‍💻 tx_hash check(ERC20) 👨🏻‍💻','💸 send ETH(ERC20) 💸')
        markup.row('Return to main page ↩️')
        bot.send_message(chat_id,'Return to the previous page was successfully ✅', reply_markup=markup )

    elif 'Donation' in message.text : 
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
        d = message.text.replace('Donation ','')
        if d in Addresses : 
            bot.send_photo(message.chat.id,photos[d],caption=Addresses[d])
        else : 
            bot.reply_to('The words entered are incorrect. Make sure the words are correct')
    
    elif message.text == '💵 Cryptocurrency price 💵' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('👇🏻👇🏻 Choose one of the two options below according to your desired currency 👇🏻👇🏻')
        markup.row('IRT currency 🇮🇷','USDT currency 🇺🇸')
        markup.row('Return to main page ↩️','Return to the previous page 🔙')
        bot.send_message(chat_id,'List of currencies opened successfully ✅', reply_markup=markup )

    elif message.text == 'IRT currency 🇮🇷' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('🪙🪙 Available currencies 19 🪙🪙')
        markup.row('Price USDTIRT','Price BTCIRT','Price ETHIRT','Price BNBIRT')
        markup.row('Price LTCIRT','Price XRPIRT','Price BCHIRT','Price EOSIRT','Price XLMIRT')
        markup.row('Price ETCIRT','Price TRXIRT','Price DOGEIRT','Price UNIIRT','Price DAIIRT')
        markup.row('Price LINKIRT','Price DOTIRT','Price AAVEIRT','Price ADAIRT','Price SHIBIRT')
        markup.row('Return to main page ↩️','Return To The Previous Page 🔙')
        bot.send_message(chat_id,'List of currencies by IRT opened successfully ✅', reply_markup=markup )

    elif message.text == 'USDT currency 🇺🇸' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('🪙🪙 Available currencies 18 🪙🪙')
        markup.row('Price BTCUSDT','Price ETHUSDT','Price BNBUSDT')
        markup.row('Price LTCUSDT','Price XRPUSDT','Price BCHUSDT','Price EOSUSDT','Price XLMUSDT')
        markup.row('Price ETCUSDT','Price TRXUSDT','Price DOGEUSDT','Price UNIUSDT','Price DAIUSDT')
        markup.row('Price LINKUSDT','Price DOTUSDT','Price AAVEUSDT','Price ADAUSDT','Price SHIBUSDT')
        markup.row('Return to main page ↩️','Return To The Previous Page 🔙')
        bot.send_message(chat_id,'List of currencies by USDT opened successfully ✅', reply_markup=markup )

    elif message.text == 'Return To The Previous Page 🔙' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('👇🏻👇🏻 Choose one of the two options below according to your desired currency 👇🏻👇🏻')
        markup.row('IRT currency 🇮🇷','USDT currency 🇺🇸')
        markup.row('Return to main page ↩️','Return to the previous page 🔙')
        bot.send_message(chat_id,'Return to the previous page successfully ✅', reply_markup=markup )

    elif 'Price' in message.text :
        symbol_in = message.text.replace('Price ','')
        response = requests.get(api_price_url+symbol_in)
        if response.status_code == 200 :
            response = response.json()
            tmp =  '🪙🪙' + f'{symbol_in} PRICE : ',response['trades'][0]['price'] +'🪙🪙'
            bot.reply_to(message,str(tmp).strip("(')"))
        else :
            bot.reply_to(message,'server error . try again...')

    elif message.text == '📒 List of information 📒'  :
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('1-What Is Cryptocurrency? 🤔') 
        markup.row('2-How does cryptocurrency work? 🤯')
        markup.row('3-How to buy cryptocurrency? 😎')
        markup.row('4-How to donate? 🤑')
        markup.row('🗂 if you need more information 🗂 \n📨 contact us 📨')
        markup.row('Return to main page ↩️','Return to the previous page 🔙')
        bot.send_message(chat_id,'List of information opened successfully ✅', reply_markup=markup )

    elif message.text == '1-What Is Cryptocurrency? 🤔' : 
        bot.reply_to(message,'1-What Is Cryptocurrency?\ncryptocurrency is a digital or virtual currency that is secured by cryptography, which makes it nearly impossible to counterfeit or double-spend. Many cryptocurrencies are decentralized networks based on blockchain technology—a distributed ledger enforced by a disparate network of computers. A defining feature of cryptocurrencies is that they are generally not issued by any central authority, rendering them theoretically immune to government interference or manipulation.')

    elif message.text == '2-How does cryptocurrency work? 🤯' :
        bot.reply_to(message,'2-How does cryptocurrency work?\nCryptocurrencies run on a distributed public ledger called blockchain, a record of all transactions updated and held by currency holders.Units of cryptocurrency are created through a process called mining, which involves using computer power to solve complicated mathematical problems that generate coins. Users can also buy the currencies from brokers, then store and spend them using cryptographic wallets.If you own cryptocurrency, you don’t own anything tangible. What you own is a key that allows you to move a record or a unit of measure from one person to another without a trusted third party.Although Bitcoin has been around since 2009, cryptocurrencies and applications of blockchain technology are still emerging in financial terms, and more uses are expected in the future. Transactions including bonds, stocks, and other financial assets could eventually be traded using the technology.')

    elif message.text == '3-How to buy cryptocurrency? 😎' :
        bot.reply_to(message,'3-How to buy cryptocurrency?\n1- Do thorough research on crypto to better understand crypto.\n2- Choose a reliable exchange where you can buy cryptocurrencies.\n3- After choosing an exchange and creating an account in it, you can deposit the amount of money you want to invest in cryptocurrencies into your account.\n4- To invest in currencies, be sure to do a thorough research on the currency you want to invest in.\n5- And finally, to store your currencies, you can use the digital wallet that you have in your exchange account or use different digital wallets that you install as an application on your device(before using the wallet do enough research on it).')

    elif message.text == '4-How to donate? 🤑' : 
        bot.reply_to(message,'4-How to donate?\n1- Select your desired currency, for example (BTC).\n2- Enter the wallet address to which you want to deposit.\n3- Make sure that the currency network, for example (TRC 20), is similar to the currency network you want to deposit.\n4- Finally, choose the amount of currency you want to deposit and complete the confirmation process.')

    elif message.text == '👨🏻‍💻 tx_hash check(ERC20) 👨🏻‍💻':
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('🔴🔴 Tx_hash Enter Tx_hash here 🔴🔴\nfor example : Tx_hash r5wv5w56bw568n5k85w8m88w67w')
        markup.row('Return to main page ↩️','Return to the previous page 🔙')
        bot.send_message(chat_id,'Guide',reply_markup=markup)

    elif 'Tx_hash' in message.text : 
        tx_hash = message.text.replace('Tx_hash ','')

        response = requests.post(etherscan_url+tx_hash,headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
        if response.status_code == 200 : 
            soup = BeautifulSoup(response.text , 'html.parser')
            status_result = str(soup.find_all("span", {"class": "u-label u-label--sm u-label--value u-label--success rounded"})).count("Success")
            if status_result == 1 : 
                bot.reply_to(message,('Transaction success'))
            else :
                bot.reply_to(message,("Transaction failed"))
        else :
            bot.reply_to(message,("status code : ",response.status_code))
    
    elif message.text == '💸 send ETH(ERC20) 💸' : 
        bot.reply_to(message,'coming soon ....')

bot.polling(none_stop=True)

#The project has been completed ✅