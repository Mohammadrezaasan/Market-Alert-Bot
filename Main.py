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
import ast
from Market_alert_config import * 
'------------------------------------------------------------------------------------------------------------------------------------'
stock_market_url = "https://google-finance4.p.rapidapi.com/search/"
bot = telebot.TeleBot(Bot_Token)
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
    message.text = message.text.lower()
    if message.text in Bot_Info:
        bot.reply_to(message,Bot_Info[message.text])
    
    elif message.text == '📓 click here to open the list of keywords for you 📓' : 
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('💸 donation 💸','💵 Cryptocurrency price 💵','📊 Stock Market price 📊')
        markup.row('📒 List of information 📒','👨🏻‍💻 tx_hash check(ERC20) 👨🏻‍💻','💸 send ETH(ERC20) 💸')
        markup.row('Return to main page ↩️')
        bot.send_message(chat_id,'Keyword list opened successfully ✅', reply_markup=markup )
    
    elif message.text == 'return to main page ↩️' : 
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
        markup.row('Return to main page ↩️','Return to the keywords list page 🔙')
        bot.send_message(chat_id,'The list of currencies available for donation .\nopened successfully ✅', reply_markup=markup)
    
    elif message.text == 'return to the keywords list page 🔙' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('💸 donation 💸','💵 Cryptocurrency price 💵','📊 Stock Market price 📊')
        markup.row('📒 List of information 📒','👨🏻‍💻 tx_hash check(ERC20) 👨🏻‍💻','💸 send ETH(ERC20) 💸')
        markup.row('Return to main page ↩️')
        bot.send_message(chat_id,'Return to the previous page was successfully ✅', reply_markup=markup )

    elif message.text in Addresses  : 
        d = message.text
        if d in Addresses :
            bot.send_photo(message.chat.id,photos[d],caption=Addresses[d])
        
    
    elif message.text == '💵 cryptocurrency price 💵' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('👇🏻👇🏻 Choose one of the two options below according to your desired currency 👇🏻👇🏻')
        markup.row('IRT currency 🇮🇷','USDT currency 🇺🇸')
        markup.row('Return to main page ↩️','Return to the keywords list page 🔙')
        bot.send_message(chat_id,'List of currencies opened successfully ✅', reply_markup=markup )

    elif message.text == 'irt currency 🇮🇷' : 
        text_1 = "`"+"Enter the name of the desired cryptocurrency : "+"`"
        global currency_type
        currency_type = message.text
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('🔴🔴 To do the steps correctly, pay attention to the example below 🔴🔴')
        markup.row('Click here to get the USDT/IRT price')
        markup.row('Enter the name of the desired cryptocurrency : BTC')
        markup.row('Return to main page ↩️','Return to the previous page 🔙')
        bot.send_message(chat_id,'🔴🔴 Important 🔴🔴\n To enter the name of your desired cryptocurrency, click on the text below and add the name of your desired cryptocurrency to the end of the text.', reply_markup=markup )
        bot.send_message(chat_id,text_1,parse_mode='MarkdownV2')
   
    elif message.text == 'usdt currency 🇺🇸' : 
        currency_type = message.text
        text_2 = "`"+"Enter the name of the desired cryptocurrency : "+"`"
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('🔴🔴 To do the steps correctly, pay attention to the example below 🔴🔴')
        markup.row('Enter the name of the desired cryptocurrency : BTC')
        markup.row('Return to main page ↩️','Return to the previous page 🔙')
        bot.send_message(chat_id,'🔴🔴 Important 🔴🔴\n To enter the name of your desired cryptocurrency, click on the text below and add the name of your desired cryptocurrency to the end of the text.', reply_markup=markup )
        bot.send_message(chat_id,text_2,parse_mode='MarkdownV2')

    elif message.text == 'return to the previous page 🔙' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('👇🏻👇🏻 Choose one of the two options below according to your desired currency 👇🏻👇🏻')
        markup.row('IRT currency 🇮🇷','USDT currency 🇺🇸')
        markup.row('Return to main page ↩️','Return to the keywords list page 🔙')
        bot.send_message(chat_id,'Return to the previous page successfully ✅', reply_markup=markup )

    
    elif message.text == '📒 list of information 📒'  :
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('What Is Cryptocurrency? 🤔') 
        markup.row('How does cryptocurrency work? 🤯')
        markup.row('How to buy cryptocurrency? 😎')
        markup.row('How to donate? 🤑')
        markup.row('🗂 if you need more information 🗂 \n📨 contact us 📨')
        markup.row('Return to main page ↩️','Return to the keywords list page 🔙')
        bot.send_message(chat_id,'List of information opened successfully ✅', reply_markup=markup )

    elif message.text in crypto_info :
        bot.reply_to(message,crypto_info[message.text])

    elif message.text == '👨🏻‍💻 tx_hash check(erc20) 👨🏻‍💻':
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('🔴🔴 Tx_hash Enter Tx_hash here 🔴🔴\nfor example : Tx_hash r5wv5w56bw568n5k85w8m88w67w')
        markup.row('Return to main page ↩️','Return to the keywords list page 🔙')
        bot.send_message(chat_id,'Guide',reply_markup=markup)

    elif 'Tx_Hash' in message.text.title() : 
        tx_hash = message.text.replace('tx_hash ','')

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
    
    elif message.text == '💸 send eth(erc20) 💸' : 
        bot.reply_to(message,'coming soon ....')

    elif message.text == '📊 stock market price 📊' :
        text = "`"+"Enter the name of the desired stock : "+"`"
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('🔴🔴 To do the steps correctly, pay attention to the example below 🔴🔴')
        markup.row('Enter the name of the desired stock : AAPL')
        markup.row('Return to main page ↩️','Return to the keywords list page 🔙')
        bot.send_message(chat_id,'🔴🔴 Important 🔴🔴\n To enter the name of your desired stock, click on the text below and add the name of your desired stock to the end of the text.', reply_markup=markup )
        bot.send_message(chat_id,text,parse_mode='MarkdownV2')
   

    elif 'enter the name of the desired stock : ' in  message.text : 
        try :
            stock_name = message.text.replace('enter the name of the desired stock','')
            stock_name = stock_name.replace(":",'')
            querystring = {"q":stock_name,"hl":"en","gl":"US"}
            headers = {
	     "X-RapidAPI-Key": "0e8e253caamsh7a1a1074f48f079p1bb0ccjsn9f19ea425e08",
	     "X-RapidAPI-Host": "google-finance4.p.rapidapi.com"
        }
            response = requests.request("GET", stock_market_url, headers=headers, params=querystring)
            
            if  response.status_code == 200 :   
                    info1 = response.text
                    info1 = str(info1).strip('[]')
                    info1 = list(info1)
                    info2 = json.loads(response.text)
                    info3 = info2[0]
                    info3 = str(info3)
                    res = ast.literal_eval(info3)
                    stock_price = str(res['price']['last']['value'])
                    bot.reply_to(message,'🌍 The country where the company is located 🌍 : '+str(res['info']['country_code'])+'\n🏢 Full name of the company 🏢 : '+str(res['info']['title'])+'\n🪙 CURRENCY 🪙 : '+str(res['price']['currency'])+'\n🌋 '+stock_name.upper()+" STOCK PRICE 🌋 :💲" + stock_price +"\n⏳ "+stock_name.upper()+" STOCK TODAY CHANGE ⏳ :💲" + str(res['price']['last']['today_change'])+'\n⏳ '+stock_name.upper()+' TODAY CHANGE PERCENT ⏳ : '+ str(res['price']['last']['today_change_percent'])+'%')
        except :
            bot.reply_to(message,'🔴🔴 Make sure your sentence is spelled correctly 🔴🔴')
        

    elif 'enter the name of the desired cryptocurrency' in  message.text : 
        try :
            stock_name = message.text.replace('enter the name of the desired cryptocurrency','')
            stock_name = stock_name.replace(":",'')
            querystring = {"q":stock_name,"hl":"en","gl":"US"}
            headers = {
	     "X-RapidAPI-Key": RapidAPI_Key,
	     "X-RapidAPI-Host": "google-finance4.p.rapidapi.com"
        }
            response = requests.request("GET", stock_market_url, headers=headers, params=querystring)
            info1 = response.text
            info1 = str(info1).strip('[]')
            info1 = list(info1)
            info2 = json.loads(response.text)
            info3 = info2[0]
            info3 = str(info3)
            res = ast.literal_eval(info3)
            crypto_check = str(res['price']['currency'])

            if  currency_type == 'irt currency 🇮🇷' : 
                if crypto_check == "None" : 
                    try :
                        info1 = response.text
                        info1 = str(info1).strip('[]')
                        info1 = list(info1)
                        info2 = json.loads(response.text)
                        info3 = info2[0]
                        info3 = str(info3)
                        res = ast.literal_eval(info3)
                        stock_price = str(res['price']['last']['value'])
                        response = requests.get(api_price_url+"USDTIRT")
                        response = response.json()
                        tmp =  response['trades'][0]['price'] 
                        tmp = str(tmp).replace("'",'')
                        tmp = str(tmp).strip("( )").replace(",",'')
                        tmp = tmp.replace(""," ")
                        tmp = tmp.split()
                        tmp.pop(-1)
                        tmp = str(tmp)
                        tmp = tmp.replace("'",'')
                        tmp = tmp.replace(",","")
                        tmp = tmp.strip("[ ]")
                        tmp = tmp.replace(" ",'')
                        stock_price = float(stock_price)
                        tmp = float(tmp)
                        stock_price_all = tmp * stock_price
                        bot.reply_to(message,'🌍 The country where the company is located 🌍 : '+str(res['info']['country_code'])+'\n🪙 Full name of the currency 🪙 : '+str(res['info']['title'])+'\n🪙 CURRENCY 🪙 : '+str(res['price']['currency'])+'\n🌋 '+stock_name.upper()+" STOCK PRICE 🌋 :💲" + str(stock_price_all) +"\n⏳ "+stock_name.upper()+" STOCK TODAY CHANGE ⏳ :💲" + str(res['price']['last']['today_change'])+'\n⏳ '+stock_name.upper()+' TODAY CHANGE PERCENT ⏳ : '+ str(res['price']['last']['today_change_percent'])+'%')
                    except : 
                       bot.reply_to(message,"🔴🔴 Make sure the name of the currency you entered is correct or it is in the cryptocurrency list 🔴🔴")
                else: 
                    bot.reply_to(message,"🔴🔴 Make sure the name of the currency you entered is correct or it is in the cryptocurrency list 🔴🔴")
            elif  currency_type == 'usdt currency 🇺🇸' :   
                if crypto_check == "None" : 
                    try:
                        
                        info1 = response.text
                        info1 = str(info1).strip('[]')
                        info1 = list(info1)
                        info2 = json.loads(response.text)
                        info3 = info2[0]
                        info3 = str(info3)
                        res = ast.literal_eval(info3)
                        stock_price = str(res['price']['last']['value'])
                        bot.reply_to(message,'🌍 The country where the company is located 🌍 : '+str(res['info']['country_code'])+'\n🪙 Full name of the currency 🪙 : '+str(res['info']['title'])+'\n🪙 CURRENCY 🪙 : '+str(res['price']['currency'])+'\n🌋 '+stock_name.upper()+" STOCK PRICE 🌋 :💲" + stock_price +"\n⏳ "+stock_name.upper()+" STOCK TODAY CHANGE ⏳ :💲" + str(res['price']['last']['today_change'])+'\n⏳ '+stock_name.upper()+' TODAY CHANGE PERCENT ⏳ : '+ str(res['price']['last']['today_change_percent'])+'%')      
                    except : 
                        bot.reply_to(message,"🔴🔴 Make sure the name of the currency you entered is correct or it is in the cryptocurrency list 🔴🔴")
                else :
                    bot.reply_to(message,"🔴🔴 Make sure the name of the currency you entered is correct or it is in the cryptocurrency list 🔴🔴")

        except :
             bot.reply_to(message,'🔴🔴 Make sure your sentence is spelled correctly 🔴🔴')
        
    elif message.text == "click here to get the usdt/irt price" : 
        try :
            response = requests.get(api_price_url+"USDTIRT")
            response = response.json()
            tmp =  response['trades'][0]['price'] 
            tmp = str(tmp).replace("'",'')
            tmp = str(tmp).strip("( )").replace(",",'')
            tmp = tmp.replace(""," ")
            tmp = tmp.split()
            tmp.pop(-1)
            tmp = str(tmp)
            tmp = tmp.replace("'",'')
            tmp = tmp.replace(",","")
            tmp = tmp.strip("[ ]")
            tmp = tmp.replace(" ",'')
            bot.reply_to(message,"USDT/IRT PRICE : "+tmp)
        except : 
            bot.reply_to(message,'Server Error...')

bot.polling(none_stop=True)

#The project has been completed ✅