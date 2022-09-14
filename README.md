![D6437C96-6E84-4179-AB76-CBBA557A3146](https://user-images.githubusercontent.com/108104864/189918473-367d4289-7609-49d9-829d-c38750d40980.jpeg)



## <p align="center">A simple bot that with a few clicks you can get the price of any cryptocurrency and any stock in the stock market and you can check if the transaction you made was successful or not. <a href="https://t.me/marketalertrobot">Market Alert Bot</a>.</p>

## <p align="center">Bot API Source : <a href="https://nobitex.ir/">Nobitex Exchange</a> & <a href="https://www.google.com/finance/?hl=en">Google Finance</a>

## Contents

* [Getting started](#getting-started)

* [Next step](#next-step)
	
* [Codes docs](#codes-docs)
	
* [Keyword guide](#keyword-guide)
	
* [How does the bot respond to keywords?](#how-does-the-bot-respond-to-keywords)

## Getting started


* To start the project, we need to build a robot that was built with the help of the <a href="https://t.me/BotFather">Bot Father</a> 

* When your bot is built, the Bot Father will give you a token at the end { You put that token in the token variable in the config file } 

```
bot = telebot.TeleBot(Bot_Token)
```
 ## Next step
 * To get the information you need, you must apply to the source site to receive the information you need after the request { Currently, I am using the prepared and edited source of <a href="https://rapidapi.com/Glavier/api/google-finance4/">Rapid Api</a> site because you waste less time and it makes your work faster. }
 ```
 url = "https://google-finance4.p.rapidapi.com/search/"
```
  
## Codes docs



* The following code is related to the important parts
```
elif message.text == 'irt currency 🇮🇷' : 
        text_1 = "`"+"Enter the name of the desired cryptocurrency : "+"`"
        global currency_type
        currency_type = message.text # In this section, we save the type of currency he/she has chosen {to specify whether the price (for example, BTC) is in dollars or Iranian Tomans}

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
```
 
 * The following code is a continuation of the above code
 ```
 elif 'enter the name of the desired cryptocurrency' in  message.text : 
        try :
	    # Get currency name
            stock_name = message.text.replace('enter the name of the desired cryptocurrency','')
            stock_name = stock_name.replace(":",'')
            querystring = {"q":stock_name,"hl":"en","gl":"US"}
            headers = {
	     "X-RapidAPI-Key": RapidAPI_Key,
	     "X-RapidAPI-Host": "google-finance4.p.rapidapi.com"
        }
            response = requests.request("GET", stock_market_url, headers=headers, params=querystring)
	    # In this section, we edit the information received from the source
	    Bot_Market_Info = response.text
            Bot_Market_Info = str(Bot_Market_Info).strip('[]')
            Bot_Market_Info = list(Bot_Market_Info)
            Bot_Market_info_Edit = json.loads(response.text)
            Bot_Market_info_Edit_2 = Bot_Market_info_Edit[0]
            Bot_Market_info_Edit_2 = str(Bot_Market_info_Edit_2)
            Bot_Market_info_Edit_3 = ast.literal_eval(Bot_Market_info_Edit_2)
            crypto_check = str(Bot_Market_info_Edit_3['price']['currency'])

            if  currency_type == 'irt currency 🇮🇷' : 
                if crypto_check == "None" : 
                    try :
                        Bot_Market_Info = response.text
                        Bot_Market_Info = str(Bot_Market_Info).strip('[]')
                        Bot_Market_Info = list(Bot_Market_Info)
                        Bot_Market_info_Edit = json.loads(response.text)
                        Bot_Market_info_Edit_2 = Bot_Market_info_Edit[0]
                        Bot_Market_info_Edit_2 = str(Bot_Market_info_Edit_2)
                        Bot_Market_info_Edit_3 = ast.literal_eval(Bot_Market_info_Edit_2)
                        crypto_price = str(Bot_Market_info_Edit_3['price']['last']['value'])
                        change_irt = str(Bot_Market_info_Edit_3['price']['last']['today_change'])
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
                        crypto_price = float(crypto_price)
                        tmp = float(tmp)
                        change_irt = float(change_irt)
                        change_irt_fi = change_irt * tmp
                        crypto_price_all = tmp * crypto_price
                        bot.reply_to(message,'🌍 The country where the company is located 🌍 : '+str(Bot_Market_info_Edit_3['info']['country_code'])+'\n🪙 Full name of the currency 🪙 : '+str(Bot_Market_info_Edit_3['info']['title'])+'\n🪙 CURRENCY 🪙 : '+str(Bot_Market_info_Edit_3['price']['currency'])+'\n🌋 '+stock_name.upper()+" PRICE 🌋 : " + str(crypto_price_all) +" 🇮🇷"+"\n⏳ "+stock_name.upper()+"  TODAY CHANGE ⏳ : " + str(change_irt_fi)+" 🇮🇷"+'\n⏳ '+stock_name.upper()+' TODAY CHANGE PERCENT ⏳ : '+ str(Bot_Market_info_Edit_3['price']['last']['today_change_percent'])+'%')
                    except : 
                       bot.reply_to(message,"🔴🔴 Make sure the name of the currency you entered is correct or it is in the cryptocurrency list 🔴🔴")
                else: 
                    bot.reply_to(message,"🔴🔴 Make sure the name of the currency you entered is correct or it is in the cryptocurrency list 🔴🔴")
            elif  currency_type == 'usdt currency 🇺🇸' :   
                if crypto_check == "None" : 
                    try:
                        
                        Bot_Market_Info = response.text
                        Bot_Market_Info = str(Bot_Market_Info).strip('[]')
                        Bot_Market_Info = list(Bot_Market_Info)
                        Bot_Market_info_Edit = json.loads(response.text)
                        Bot_Market_info_Edit_2 = Bot_Market_info_Edit[0]
                        Bot_Market_info_Edit_2 = str(Bot_Market_info_Edit_2)
                        Bot_Market_info_Edit_3 = ast.literal_eval(Bot_Market_info_Edit_2)
                        crypto_price = str(Bot_Market_info_Edit_3['price']['last']['value'])
                        bot.reply_to(message,'🌍 The country where the company is located 🌍 : '+str(Bot_Market_info_Edit_3['info']['country_code'])+'\n🪙 Full name of the currency 🪙 : '+str(Bot_Market_info_Edit_3['info']['title'])+'\n🪙 CURRENCY 🪙 : '+str(Bot_Market_info_Edit_3['price']['currency'])+'\n🌋 '+stock_name.upper()+"  PRICE 🌋 :💲" + crypto_price +"\n⏳ "+stock_name.upper()+"  TODAY CHANGE ⏳ :💲" + str(Bot_Market_info_Edit_3['price']['last']['today_change'])+'\n⏳ '+stock_name.upper()+' TODAY CHANGE PERCENT ⏳ : '+ str(Bot_Market_info_Edit_3['price']['last']['today_change_percent'])+'%')      
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
            bot.reply_to(message,"🇮🇷 "+"USDT/IRT PRICE : "+tmp+" 🇮🇷")
        except : 
            bot.reply_to(message,'Server Error...')
 ```
 * Check the transaction hash
 ```
 elif 'tx hash' in message.text : 
        tx_hash = message.text.replace('tx hash ','')
        tx_hash = tx_hash.replace(":","")
        response = requests.post(etherscan_url+tx_hash,headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
        if response.status_code == 200 : 
            soup = BeautifulSoup(response.text , 'html.parser')
            status_result = str(soup.find_all("span", {"class": "u-label u-label--sm u-label--value u-label--success rounded"})).count("Success")
            if status_result == 1 : 
                bot.reply_to(message,('Transaction success ✅'))
            else :
                bot.reply_to(message,("Transaction failed ❌"))
        else :
            bot.reply_to(message,("status code : ",response.status_code))
 
 ```
 
 * <a href="https://github.com/Mohammadrezaasan/Market-Alert-Bot/blob/main/Main.py">Click here to get the full code</a>
 
 * <a href="https://github.com/Mohammadrezaasan/Market-Alert-Bot/blob/main/config.py">Click here to get the config file</a>
 
 ## Keyword guide
	
|Keyword names|What can they do?|
|:---:|------|
|🤖 Introducing The Robot 🤖|This key will help you get to know the bot and understand what it can do.|
|📓 Click here to open the list of keywords for you 📓|You can use this key to open the keyword list.|
|🗂 if you need more information 🗂,📨 contact us 📨|This key shows you the ways to communicate with us 📡.|
|💸 donation 💸|With the help of this key, a list of available currencies for donation will be opened, and by clicking on the desired currency, you will receive its address and QR code.|
|💵 Cryptocurrency price 💵|By clicking on this button, a list will open for you in which two options will be displayed for you, you can choose one according to your desired currency and then click on the desired option from the two options. Choose one. Click on the currency you want and a list of available currencies will open for you to request a price. Click on any of them and you will get the price of the currency you want.|
|📊 Stock Market price 📊|With the help of this key, you can get the current price of any stock with a few simple clicks.|
|👨🏻‍💻 tx_hash check(ERC20) 👨🏻‍💻|By using this key and following the instructions, you can enter your address and check it and make sure that the operation is done correctly.|
|📒 List of information 📒|When you click on this button, a list of information will open for you, and you will get the answer to your question by clicking on the question you want.|
 
 ## How does the bot respond to keywords?
 
 |<p align="center"><video src="https://user-images.githubusercontent.com/108104864/190086229-9091d470-27ff-409f-8e33-41ccd8bd2849.MOV" width="250" height="500"/><p align="center"><video src="https://user-images.githubusercontent.com/108104864/190086349-34e660c7-dd47-44a6-921e-b79b3f8641ad.MOV" width="250" height="500"/>|
|:---:|
|!!Keywords used in the video!!|
|🤖 Introducing The Robot 🤖|
|📓 Click here to open the list of keywords for you |
|🗂 if you need more information 🗂,📨 contact us 📨|
|💸 donation 💸|
|💵 Cryptocurrency price 💵|
|📊 Stock Market price 📊|
|👨🏻‍💻 tx_hash check(ERC20) 👨🏻‍💻|
|📒 List of information 📒 |
 
 
 
 
 
