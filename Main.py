from telebot import TeleBot
from telebot import types
import telebot
from telebot import types
from markupsafe import Markup
from rsa import PublicKey
import requests
from bs4 import BeautifulSoup
import json
from decimal import *
from live_information_en_config import * 
from live_information_fa_config import * 


'------------------------------------------------------------------------------------------------------------------------------------'
bot = telebot.TeleBot(Bot_Token)
api_price_url = "https://api.nobitex.ir/v2/trades/"
etherscan_url = "https://etherscan.io/tx/"
'------------------------------------------------------------------------------------------------------------------------------------'
@bot.message_handler(commands=['start'])
def handle_start(message):
   chat_id = message.chat.id 
   markup = telebot.types.ReplyKeyboardMarkup(True, False)
   markup.row('برای شروع نسخه فارسی کلیک کنید')
   markup.row('Click to start the English version'.title())
   bot.send_message(chat_id,'سلام 🙋🏻‍♂️\nبه ربات Yahoo Finance Bot خوش آمدید👾\n\nHello 🙋🏻‍♂️\nWelcome to Yahoo Finance Bot👾'.title(), reply_markup=markup)
   
@bot.message_handler(content_types=['text'])
def handle_text(message):
        global problem
        problem = ''
        message.text = message.text.lower()

        if message.text in Bot_Info:
            bot.reply_to(message,Bot_Info[message.text])
        elif message.text == "click to start the english version" :
            chat_id = message.chat.id 
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('🤖 Introducing the robot 🤖'.title())
            markup.row('🗂 if you need more information 🗂 \n📨 contact us 📨'.title())
            markup.row('🗝 What can each key do? 🗝'.title())
            markup.row('📓 list of keywords 📓'.title())
            markup.row('Return to version selection page 🔙')
            bot.send_message(chat_id,'English version started .'.title(), reply_markup=markup)

        elif message.text == 'return to version selection page 🔙' : 
            chat_id = message.chat.id 
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('برای شروع نسخه فارسی کلیک کنید')
            markup.row('Click to start the English version'.title())
            bot.send_message(chat_id,'Return successfully to version selection page ✅'.title(), reply_markup=markup)

        elif   message.text == '🗝 what can each key do? 🗝'  : 
            bot.reply_to(message,bot_kaywords)

        
        elif message.text == '📓 list of keywords 📓' : 
            chat_id = message.chat.id 
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('📊 Stock Market price 📊'.title())
            markup.row('💵 Cryptocurrency price 💵'.title())
            markup.row('📒 List of information 📒'.title())
            markup.row('👨🏻‍💻 Tx_Hash Check 👨🏻‍💻')
            markup.row('Return to main page ↩️'.title())
            bot.send_message(chat_id,'Keyword list opened successfully ✅', reply_markup=markup )
        
        elif message.text == 'return to main page ↩️' : 
            chat_id = message.chat.id 
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('🤖 Introducing the robot 🤖'.title())
            markup.row('🗂 if you need more information 🗂 \n📨 contact us 📨'.title())
            markup.row('🗝 What can each key do? 🗝'.title())
            markup.row('📓 list of keywords 📓'.title())
            markup.row('Return to version selection page 🔙')
            bot.send_message(chat_id,'Return to main page was successful ✅', reply_markup=markup)

        
        elif message.text == 'return to the keywords list page 🔙' : 
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('📊 Stock Market price 📊'.title())
            markup.row('💵 Cryptocurrency price 💵'.title())
            markup.row('📒 List of information 📒'.title())
            markup.row('👨🏻‍💻 Tx_Hash Check 👨🏻‍💻')
            markup.row('Return to main page ↩️'.title())
            bot.send_message(chat_id,'Return to the keywords list page was successfully ✅'.title(), reply_markup=markup )

        elif message.text == '💵 cryptocurrency price 💵' : 
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('👇🏻Choose one of the Nine options👇🏻\nbelow according to your desired currency'.title())
            markup.row('UNITED STATES(USD)')
            markup.row('JAPAN(JPY)','england(gbp)'.upper())
            markup.row('CHINA(CNH)','GERMANY(EUR)')
            markup.row('INDIA(INR)','SOUTH KOREA(KRW)')
            markup.row('IRAN(IRT)','RUSSIA(RUB)')
            markup.row('Return to main page ↩️'.title(),'Return to the keywords list page 🔙'.title())
            bot.send_message(chat_id,'List of currencies opened successfully ✅'.title(), reply_markup=markup )

        elif message.text in curences_list_from_config : 
            text_1 = "`"+"Cryptocurrency Name : "+"`"
            global currency_type
            currency_type = message.text
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            
            if currency_type == 'united states(usd)' :
                markup.row('🔴 To do the steps correctly, pay attention 🔴\nto the example below'.title())
                markup.row('Cryptocurrency Name : BTC')
                markup.row('Return to main page ↩️'.title(),'Return to the previous page 🔙'.title())
                bot.send_message(chat_id,'🔴Important🔴\n'.upper()+' To enter the name of your desired cryptocurrency, click on the text below and add the symbol of your desired cryptocurrency to the end of the text.'.title(), reply_markup=markup )
                bot.send_message(chat_id,text_1,parse_mode='MarkdownV2')
            
            elif currency_type != 'united states(usd)' :
                markup.row('🔴 To do the steps correctly, pay attention 🔴\nto the example below'.title())
                markup.row(f'Click here to get the USDT/{curences_list_from_config[currency_type]} Price'.replace('=X',''))
                markup.row('Cryptocurrency Name : BTC')
                markup.row('Return to main page ↩️'.title(),'Return to the previous page 🔙'.title())
                bot.send_message(chat_id,'🔴Important🔴\n'.upper()+' To enter the name of your desired cryptocurrency, click on the text below and add the symbol of your desired cryptocurrency to the end of the text.'.title(), reply_markup=markup )
                bot.send_message(chat_id,text_1,parse_mode='MarkdownV2')
    
        elif message.text == 'return to the previous page 🔙' : 
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('👇🏻Choose one of the Nine options👇🏻\nbelow according to your desired currency'.title())
            markup.row('UNITED STATES(USD)')
            markup.row('JAPAN(JPY)','england(gbp)'.upper())
            markup.row('CHINA(CNH)','GERMANY(EUR)')
            markup.row('INDIA(INR)','SOUTH KOREA(KRW)')
            markup.row('IRAN(IRT)','RUSSIA(RUB)')
            markup.row('Return to main page ↩️'.title(),'Return to the keywords list page 🔙'.title())
            bot.send_message(chat_id,'Return to the previous page successfully ✅'.title(), reply_markup=markup )

        
        elif message.text == '📒 list of information 📒'  :
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('What Is Cryptocurrency? 🤔'.title()) 
            markup.row('How does cryptocurrency work? 🤯'.title())
            markup.row('How to buy cryptocurrency? 😎'.title())
            markup.row('How to donate? 🤑'.title())
            markup.row('🗂 if you need more information 🗂 \n📨 contact us 📨'.title())
            markup.row('Return to main page ↩️'.title(),'Return to the keywords list page 🔙'.title())
            bot.send_message(chat_id,'List of information opened successfully ✅'.title(), reply_markup=markup )

        elif message.text in crypto_info :
            bot.reply_to(message,crypto_info[message.text])

        elif message.text == '👨🏻‍💻 tx_hash check 👨🏻‍💻':
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True,False)
            markup.row('👇🏻Choose one of the two options👇🏻\naccording to your desired Currency network'.title())
            markup.row('TRON(TRC20)','Ethereum(ERC20)'.upper())
            markup.row('Return to main page ↩️'.title(),'Return to the keywords list page 🔙'.title())
            bot.send_message(chat_id,'List of Currency network opened successfully ✅'.title(), reply_markup=markup)

        elif  message.text ==  'tron(trc20)' or message.text == 'ethereum(erc20)' : 
            global tx_hash_type
            tx_hash_type = message.text
            text_3 = "`"+"Tx Hash : "+"`"
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True,False)
            markup.row('🔴 To do the steps correctly, pay attention 🔴\nto the example below'.title())
            markup.row('Tx Hash : 0xe91024d715804721cc22e4b')
            markup.row('Return to main page ↩️'.title(),'Return to the Currency network list page 🔙'.title())

            bot.send_message(chat_id,'🔴Important🔴\n'.upper()+' Copy the following text to your clipboard and add your Transaction hash at the end.'.title()+'', reply_markup=markup )
            bot.send_message(chat_id,text_3,parse_mode='MarkdownV2')

        elif message.text == 'return to the currency network list page 🔙' :
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True,False)
            markup.row('👇🏻Choose one of the two options👇🏻\naccording to your desired Currency network'.title())
            markup.row('TRON(TRC20)','Ethereum(ERC20)'.upper())
            markup.row('Return to main page ↩️'.title(),'Return to the keywords list page 🔙'.title())
            bot.send_message(chat_id,'Return to the Currency network page successfully ✅'.title(), reply_markup=markup)



        elif str(message.text.replace(":"," ").split()[0 : -1]).replace("'",'').replace(",","").strip("[ ]") == 'tx hash' : 
            tx_hash = message.text.replace('tx hash','')
            tx_hash = tx_hash.replace(':','').replace(" ",'')
            tx_hash_type_status = ''
            keyboard = types.InlineKeyboardMarkup()
            chat_id = message.chat.id
            try : 
                if tx_hash_type == tx_hash_type:
                    tx_hash_type_status = 'ok'
            except:
                chat_id = message.chat.id
                markup = telebot.types.ReplyKeyboardMarkup(True,False)
                markup.row('👇🏻Choose one of the two options👇🏻\naccording to your desired Currency network'.title())
                markup.row('TRON(TRC20)','Ethereum(ERC20)'.upper())
                markup.row('Return to main page ↩️'.title(),'Return to the keywords list page 🔙'.title())
                bot.send_message(chat_id,'Please specify your cryptocurrency network first .'.title(), reply_markup=markup)
            
            
            if tx_hash_type_status == 'ok' :
                if tx_hash_type == 'ethereum(erc20)':
                    try:   
                        global contract_confirmed_or_not_status_erc20
                        contract_confirmed_or_not_status_erc20 = ''
                        response = requests.post(etherscan_url+tx_hash,headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
                        if response.status_code == 200 : 
                            soup = BeautifulSoup(response.text , 'html.parser')
                            status_result = str(soup.find_all("span", {"class": "u-label u-label--sm u-label--value u-label--success rounded"})).count("Success")
                            contract_confirmed_or_not_status_erc20 = ''
                            if status_result == 1 : 
                                contract_confirmed_or_not_status_erc20 = 'Transaction CONFIRMED ✅'
                            elif status_result != 1 :
                                contract_confirmed_or_not_status_erc20 = 'Transaction UNCONFIRMED ❌\nor not found ❌'
                            tg_message_to_send_hash_erc20 = contract_confirmed_or_not_status_erc20.upper()+'\n'+"--------------------------------------------------------------------"+'\n'
                            tg_message_to_send_hash_erc20 += f"<a href='https://etherscan.io/tx/{tx_hash}'>Click To Get More Information</a>"
                            tg_message_to_send_hash_erc20 += '\n'+"--------------------------------------------------------------------"
                                

                            bot.send_message(chat_id, tg_message_to_send_hash_erc20, parse_mode = 'HTML', disable_web_page_preview=False, reply_markup=keyboard)

                            

                    except : 
                        problem ='Please make sure your transaction number is correct.'
                        bot.reply_to(message,problem)

            if tx_hash_type_status == 'ok' :

                if tx_hash_type == 'tron(trc20)' : 
                    
                        agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
                        headers = {'User-Agent': agent}

                        url_tx_hash = f"https://apilist.tronscanapi.com/api/transaction-info?hash={tx_hash}"

                        response_for_trx = requests.get(url_tx_hash, headers=headers)
                        if response_for_trx.status_code == 200 :
                            try :

                                response_for_trx = (response_for_trx.text)

                                response_for_trx = (json.loads(response_for_trx))

                                contract_confirmed = response_for_trx['confirmed']

                                if str(contract_confirmed) ==  'True' : 
                                    contract_confirmed = 'Transaction CONFIRMED ✅'.upper()
                                elif str(contract_confirmed) != 'True' : 
                                    contract_confirmed = 'Transaction UNCONFIRMED ❌\nor not found ❌'
                                tg_message_to_send_hash_trc20 = contract_confirmed.upper()+'\n'+"--------------------------------------------------------------------"+'\n'
                                tg_message_to_send_hash_trc20 += f"<a href='https://tronscan.org/#/transaction/{tx_hash}'>Click To Get More Information</a>"
                                tg_message_to_send_hash_trc20 += '\n'+"--------------------------------------------------------------------"
                                bot.send_message(chat_id, tg_message_to_send_hash_trc20, parse_mode = 'HTML', disable_web_page_preview=False, reply_markup=keyboard)
                            except :
                                problem ='Please make sure your transaction number is correct.'
                                bot.reply_to(message,problem)
                        else :
                            problem ='Please make sure your transaction number is correct.'
                            bot.reply_to(message,problem)


        elif message.text == '📊 stock market price 📊' :
            text = "`"+"Stock Name : "+"`"
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True,False)
            markup.row('🔴 To do the steps correctly, pay attention 🔴\nto the example below'.title())
            markup.row('Stock Name : AAPL')
            markup.row('Return to main page ↩️'.title(),'Return to the keywords list page 🔙'.title())
            bot.send_message(chat_id,'🔴Important🔴\n'.upper()+' To enter the name of your desired stock, click on the text below and add the symbol of your desired stock to the end of the text.'.title(), reply_markup=markup )
            bot.send_message(chat_id,text,parse_mode='MarkdownV2')
    

        elif str(message.text.replace(":"," ").split()[0 : -1]).replace("'",'').replace(",","").strip("[ ]") == 'stock name' : 
            try :
                stock_name = message.text.replace('stock name','')
                stock_name = stock_name.replace(":",'').replace(" ",'')
                global symbol
                symbol = stock_name.upper()
                agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
                headers = {'User-Agent': agent}
                url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}'
                response = requests.get(url, headers=headers)
                response = (response.text)
                soup = BeautifulSoup( response , 'html.parser')
                global stock_price_global
                global stock_change_percent_global
                global stock_change_usd_global


                stock_price_global = ""
                stock_change_usd_global = ""
                stock_change_percent_global = ""
                # FOR LIVE STOCK
                global live_stock_changes
                live_stock_changes = soup.find(class_ = "Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)")
                global color_status
                color_status = ""
                if str(live_stock_changes) != "None" : 
                    try :
                        market_price_for_live_stokc = str(live_stock_changes.find(class_="C($primaryColor) Fz(24px) Fw(b)"))
                        market_price_for_live_stokc = market_price_for_live_stokc.replace(">",' ').split()[-1].replace("</fin-streamer",'')
                        stock_price_global = market_price_for_live_stokc

                        if "C($negativeColor)" in str(live_stock_changes):
                            color_status = color_status = "C($negativeColor)"
                        elif "C($positiveColor)" in str(live_stock_changes) :
                            color_status = color_status ="C($positiveColor)"
                        elif "C($negativeColor)" and  "C($positiveColor)" not in str(live_stock_changes):
                            color_status = color_status =""

                        live_stock_changes = live_stock_changes.find_all(class_ = color_status)

                        market_price_change_usd_for_live_stokc = str(live_stock_changes[0]).replace(f'<span class="{color_status}">','').replace("</span>",'').strip("[ ]")
                        stock_change_usd_global = market_price_change_usd_for_live_stokc

                        market_price_change_percent_for_live_stokc = str(live_stock_changes[1]).replace(f'<span class="{color_status}">','').replace("</span>",'').strip("( )")
                        
                        stock_change_percent_global = market_price_change_percent_for_live_stokc

                    except:
                        'ok'
                elif str(live_stock_changes) == "None" :

                    try:

                        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        when_live_stock_changes_is_none = soup.find(class_ = "D(ib) Mend(20px)")
                        # get live price
                        price = when_live_stock_changes_is_none.find( class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)" )
                        price = str(price).split()
                        price = price[-1].replace("</fin-streamer>",'')
                        price_index = price.index(">")
                        price = price[price_index : ].replace(">",'')
                        stock_price_global = price
                        # get change usd
                        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        color_status = ("")

                        if "C($negativeColor)" in str(when_live_stock_changes_is_none):
                            color_status = color_status = "C($negativeColor)"
                        elif "C($positiveColor)" in str(when_live_stock_changes_is_none) :
                            color_status = color_status ="C($positiveColor)"
                        elif "C($negativeColor)" and  "C($positiveColor)" not in str(when_live_stock_changes_is_none):
                            color_status = color_status =""
                        
                        market_changes_when_live_stock_is_none = when_live_stock_changes_is_none.find_all (class_ = color_status )

                        change_usd = (str(market_changes_when_live_stock_is_none[0]).replace(f"""<span class="{color_status}">""",'').replace("</span>",'').strip("[ ]"))
                        stock_change_usd_global = change_usd
                        # get change percent
                        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        change_percent = (str(market_changes_when_live_stock_is_none[1]).replace(f"""<span class="{color_status}">""",'').replace("</span>",'').strip("( )"))
                        stock_change_percent_global = change_percent                
                    except : 
                        'ok'
                    # for market status
            
                try :
                    ## for stokc holders
                    ## for stokc holders



                    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
                    headers = {'User-Agent': agent}
                    ## for stokc holders
                    url_for_holders = f'https://finance.yahoo.com/quote/{symbol}/holders?p={symbol}'

                    response_holders = requests.get(url_for_holders, headers=headers)
                    response_holders = (response_holders.text)
                    soup_holders = BeautifulSoup( response_holders , 'html.parser')
                    ## for holders

                    top_one_holder_for_edit = (soup_holders.find(class_ = "Mt(25px) Ovx(a) W(100%)").find(class_ = "BdT Bdc($seperatorColor) Bgc($hoverBgColor):h Whs(nw) H(36px)"))

                    top_one_name = (top_one_holder_for_edit.find(class_ = "Ta(start) Pend(10px)"))
                    top_one_name =(str(top_one_name).replace('<td class="Ta(start) Pend(10px)">','').replace("</td>",''))

                    top_one_holder_for_edit_by_class = top_one_holder_for_edit.find_all(class_= "Ta(end) Pstart(10px)")

                    top_one_shares = (str(top_one_holder_for_edit_by_class[0]).replace('<td class="Ta(end) Pstart(10px)">','').replace("</td>",''))

                    top_one_shares_date_reported = (str(top_one_holder_for_edit_by_class[1:2]).replace('<td class="Ta(end) Pstart(10px)"><span>','').replace("</span></td>",'').strip("[ ]"))
                    top_one_shares_date_reported=top_one_shares_date_reported.replace(",",'').replace(" ",'/')

                    top_one_shares_usd_va = (str(top_one_holder_for_edit_by_class[-1]).replace('<td class="Ta(end) Pstart(10px)">','').replace("</td>",''))

                    #----------------------------------------------------------------------------------------------
                except : 
                    top_one_name = 'N/A'
                    top_one_shares = 'N/A'
                    top_one_shares_date_reported = 'N/A'
                    top_one_shares_usd_va = 'N/A'
                try: 
                    code_for_last_news_edit_for_all_types = ''
                    code_for_last_news_edit_just_text = (soup.find(class_="Ov(h) Pend(14%) Pend(44px)--sm1024"))
                
                    if str(code_for_last_news_edit_just_text).lower() == 'none':
                        code_for_last_news_edit_for_all_types = "Ov(h) Pend(44px) Pstart(25px)"
                    elif str(code_for_last_news_edit_just_text).lower() != 'none':
                        code_for_last_news_edit_for_all_types = "Ov(h) Pend(14%) Pend(44px)--sm1024"
                    
                    try :     
                        test = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="C(#959595) Fz(11px) D(ib) Mb(6px)")
                    except: 
                        code_for_last_news_edit_for_all_types = 'js-stream-content Pos(r)'


                    
                    last_news_agency = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="C(#959595) Fz(11px) D(ib) Mb(6px)")
                    last_news_agency = (str(last_news_agency).replace('<div class="C(#959595) Fz(11px) D(ib) Mb(6px)">','').replace("</div>",''))
                    
                    last_news_title = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="Mb(5px)")
                    last_news_title = (str(last_news_title).replace(">",' ').replace("<"," "))
                    last_news_title_index = (last_news_title.split().index('/u'))
                    last_news_title =  last_news_title.split()[last_news_title_index+1 : -2]
                    last_news_title = (str(last_news_title).replace("'","").replace(",",'').strip("[ ]")+".")


                    last_news_link = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="Mb(5px)").find(class_="js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled")
                    last_news_link_index = (str(last_news_link).replace("js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled",'').replace(">",' ').replace('"',' ').split().index("href="))
                    last_news_link = (str(last_news_link).replace("js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled",'').replace(">",' ').replace('"',' ').split()[last_news_link_index+1])
                    last_news_link = ("https://finance.yahoo.com"+last_news_link)

                    
                except : 
                    last_news_agency = 'N/A'
                    last_news_title = 'N/A'
                    last_news_link = 'N/A'
                    

                try : 
                    market_status_time = soup.find(class_ = "D(ib) Fl(end) Pb(6px) Fz(xs) Fw(b) fin-update-style").find(class_ = "C($c-fuji-orange-b)")
                    market_status_time = (str(market_status_time).replace('<span class="C($c-fuji-orange-b)" data-id="mk-msg">','').replace("</span>",''))
                    market_status_time = market_status_time.replace(".",'')
                    if str(market_status_time).lower() == "none" :
                        market_status_time = market_status_time = "US markets closed"
                except:
                    market_status_time = "N/A"

                try :
                    info = info_stock(symbol)

                    market_cap=info['market_cap']
                    countre_campone = info['country']
                    comeny_site = info["site"]
                    comeny_name = info['name']
                except : 
                    'ok'
                chat_id = message.chat.id
                
                global tg_message_to_send
                tg_message_to_send = market_status_time+"❗️"+"\n"+"--------------------------------------------------------------------"+'\nCountry 🌍 :\n'+str(countre_campone)+"\n"+"-------------------------------------------------------------------"+'\nCompany full name 🏢 :\n'
                tg_message_to_send += f"<a href='{comeny_site}'>{comeny_name}</a>"
                tg_message_to_send += "\n"+"--------------------------------------------------------------------"+'\nCURRENCY 🪙 :\n'+'USD 🇺🇸\n'+"--------------------------------------------------------------------"+'\n'+stock_name.upper()+" STOCK PRICE 🌋 :\n" + str(stock_price_global) +' 💲\n'+"--------------------------------------------------------------------"+"\n"+stock_name.upper()+" 24H CHANGE ⏳ :\n" +str(stock_change_usd_global)+' 💲\n'+"--------------------------------------------------------------------"+'\n'+stock_name.upper()+' 24H CHANGE PERCENT ⏳ :\n'+str(stock_change_percent_global)+" \n"+"--------------------------------------------------------------------"+"\n"+stock_name.upper()+" MARKET CAP 🏦 :\n"+str(market_cap)+"\n"+"--------------------------------------------------------------------"+'\nLargest Institutional Holder 🌐 :\n'+str(top_one_name).title()+'\n'+"--------------------------------------------------------------------"+'\n'+str(top_one_name).title()+' Date Reported 📆 :\n'+str(top_one_shares_date_reported)+'\n'+'--------------------------------------------------------------------'+f'\n{top_one_name.title()} Shares 💠 :\n'+str(top_one_shares)+'\n'+'--------------------------------------------------------------------'+f"\nShares value USD 💰 :\n"+str(top_one_shares_usd_va)+'\n'+'--------------------------------------------------------------------'                                                                                                                                            
                
                global tg_message_to_send_sort
                tg_message_to_send_sort =market_status_time+"❗️"+"\n"+"--------------------------------------------------------------------"+'\n'+stock_name.upper()+" STOCK PRICE 🌋 :\n" + str(stock_price_global) +' 💲\n'+"--------------------------------------------------------------------"+"\n"+stock_name.upper()+" 24H CHANGE ⏳ :\n" +str(stock_change_usd_global)+' 💲\n'+"--------------------------------------------------------------------"+'\n'+stock_name.upper()+' 24H CHANGE PERCENT ⏳ :\n'+str(stock_change_percent_global)
                global tg_message_to_send_news
                tg_message_to_send_news = f'The latest news about {comeny_name} ❗️'+"\n"+"--------------------------------------------------------------------"+'\nName of the news agency ✒️ :\n'.title()+str(last_news_agency)+"\n"+"-------------------------------------------------------------------"+'\nNews title 🗞 :\n'.title()+str(last_news_title)+'\n'+"-------------------------------------------------------------------"+'\n'
                tg_message_to_send_news += f"<a href='{last_news_link}'>Click To Read Full Details 📰</a>"
                tg_message_to_send_news += "\n"+"--------------------------------------------------------------------"

                button_bar = types.InlineKeyboardButton('📚Click to get more information📚'.title(), callback_data='click get more information for stock market')
                button_bar2 = types.InlineKeyboardButton('🗞Click to get the latest news🗞'.title(), callback_data='click to get the latest news for stock market')
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(button_bar)
                keyboard.add(button_bar2)
                global message_for_edit
                message_for_edit = message
                bot.send_message(chat_id, tg_message_to_send_sort, parse_mode = 'HTML', disable_web_page_preview=False, reply_markup=keyboard)
            except :
                problem ='Make sure you enter the company name symbol correctly.'
                bot.reply_to(message,problem)



        elif str(message.text.replace(":"," ").split()[0 : -1]).replace("'",'').replace(",","").strip("[ ]")  == 'cryptocurrency name':
            try :
                cryptocurrency_name = message.text.replace('cryptocurrency name','')
                cryptocurrency_name = cryptocurrency_name.replace(":",'')
                symbol_crypto = (cryptocurrency_name).upper().replace(" ",'')
                crypto_currency_type_status = ''
                keyboard = types.InlineKeyboardMarkup()
                chat_id = message.chat.id
                try : 
                    if  currency_type != 'united states(usd)' and currency_type != 'iran(irt)' :
                                
                                currence_countery_price_to_usdt = curences_list_from_config[currency_type]
                                agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
                                headers = {'User-Agent': agent}
                                url = f'https://finance.yahoo.com/quote/{currence_countery_price_to_usdt}?p={currence_countery_price_to_usdt}'
                                response_price_to_usdt  = requests.get(url, headers=headers)
                                if response_price_to_usdt.status_code == 200 :
                                    response_price_to_usdt = (response_price_to_usdt.text)
                                    soup = BeautifulSoup( response_price_to_usdt , 'html.parser')
                                    when_live_stock_changes_is_none = soup.find(class_ = "D(ib) Mend(20px)")
                                    # FOR LIVE price
                                    live_stock_changes = soup.find(class_ = "Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)")
                                    when_live_stock_changes_is_none = soup.find(class_ = "D(ib) Mend(20px)")
                                    # get live price
                                    price = when_live_stock_changes_is_none.find( class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)" )
                                    price = str(price).split()
                                    price = price[-1].replace("</fin-streamer>",'')
                                    price_index = price.index(">")
                                    price = price[price_index : ].replace(">",'')
                                    price=str(price).replace(',','')
                                    currence_price_to_usdt = float(price)
                                    currence_price_to_usdt = "%.2f" % currence_price_to_usdt
                                    crypto_currency_type_status = 'ok'

                                    currence_price_to_usdt = float(currence_price_to_usdt)

                                else : 
                                    problem ='The problem is with the source servers and we are trying to fix it.'
                                    bot.reply_to(message,problem)
                    elif currency_type == 'united states(usd)' or currency_type == 'iran(irt)' : 
                                crypto_currency_type_status = 'ok'

                except:
                    chat_id = message.chat.id
                    markup = telebot.types.ReplyKeyboardMarkup(True,False)
                    markup.row('👇🏻Choose one of the two options👇🏻\nbelow according to your desired currency'.title())
                    markup.row('UNITED STATES(USD)')
                    markup.row('JAPAN(JPY)','england(gbp)'.upper())
                    markup.row('CHINA(CNH)','GERMANY(EUR)')
                    markup.row('INDIA(INR)','SOUTH KOREA(KRW)')
                    markup.row('IRAN(IRT)','RUSSIA(RUB)')
                    markup.row('Return to main page ↩️'.title(),'Return to the keywords list page 🔙'.title())
                    bot.send_message(chat_id,'🛑 Please select your currency first to receive the prices according to that currency .\n'.title(), reply_markup=markup)
                if crypto_currency_type_status == 'ok' : 
                    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
                    headers = {'User-Agent': agent}
                    url = f'https://finance.yahoo.com/quote/{symbol_crypto}-USD?p={symbol_crypto}-USD'
                    response = requests.get(url, headers=headers)
                    response = (response.text)
                    soup = BeautifulSoup( response , 'html.parser')
                    # get live price
                    live_crypto_changes = soup.find(class_ = "D(ib) Mend(20px)")
                    # get live price
                    price_for_crypto = live_crypto_changes.find( class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)" )
                    price_for_crypto = str(price_for_crypto).split()
                    price_for_crypto = price_for_crypto[-1].replace("</fin-streamer>",'')
                    price_index = price_for_crypto.index(">")
                    price_for_crypto = price_for_crypto[price_index : ].replace(">",'')
                    cryptocurrency_price = price_for_crypto
                    # get change usd
                    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    color_status = ("")

                    if "C($negativeColor)" in str(live_crypto_changes):
                            color_status = color_status = "C($negativeColor)"
                    elif "C($positiveColor)" in str(live_crypto_changes) :
                            color_status = color_status ="C($positiveColor)"
                    elif "C($negativeColor)" and  "C($positiveColor)" not in str(live_crypto_changes):
                            color_status = color_status =""
                            
                    crypto_changes = live_crypto_changes.find_all (class_ = color_status )
                    change_usd = (str(crypto_changes[0]).replace(f"""<span class="{color_status}">""",'').replace("</span>",'').strip("[ ]"))
                    cryptocurrency_change_usd = change_usd
                    # get change percent
                    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                    change_percent = (str(crypto_changes[1]).replace(f"""<span class="{color_status}">""",'').replace("</span>",'').strip("( )"))
                    cryptocurrency_change_percent = change_percent
                    try : 
                        code_for_last_news_edit_for_all_types = ''
                        code_for_last_news_edit_just_text = (soup.find(class_="Ov(h) Pend(14%) Pend(44px)--sm1024"))
                        if str(code_for_last_news_edit_just_text).lower() == 'none':
                            code_for_last_news_edit_for_all_types = "Ov(h) Pend(44px) Pstart(25px)"
                        elif str(code_for_last_news_edit_just_text).lower() != 'none':
                            code_for_last_news_edit_for_all_types = "Ov(h) Pend(14%) Pend(44px)--sm1024"
                        
                        try :     
                            test = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="C(#959595) Fz(11px) D(ib) Mb(6px)")
                        except: 
                            code_for_last_news_edit_for_all_types = 'js-stream-content Pos(r)'


                        try :

                            last_news_agency = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="C(#959595) Fz(11px) D(ib) Mb(6px)")
                            last_news_agency = (str(last_news_agency).replace('<div class="C(#959595) Fz(11px) D(ib) Mb(6px)">','').replace("</div>",''))
                            
                            last_news_title = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="Mb(5px)")
                            last_news_title = (str(last_news_title).replace(">",' ').replace("<"," "))
                            last_news_title_index = (last_news_title.split().index('/u'))
                            last_news_title =  last_news_title.split()[last_news_title_index+1 : -2]
                            last_news_title = (str(last_news_title).replace("'","").replace(",",'').strip("[ ]")+".")


                            last_news_link = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="Mb(5px)").find(class_="js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled")
                            last_news_link_index = (str(last_news_link).replace("js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled",'').replace(">",' ').replace('"',' ').split().index("href="))
                            last_news_link = (str(last_news_link).replace("js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled",'').replace(">",' ').replace('"',' ').split()[last_news_link_index+1])
                            last_news_link = ("https://finance.yahoo.com"+last_news_link)
                        except:
                            last_news_title = 'N/A'  
                            last_news_agency = 'N/A'
                            last_news_link = 'N/A'
                    except : 
                        'ok'
                    try : 
                        info = info_crypto(str(symbol_crypto).replace(' ',''))
                        # info for crypto
                        market_cap_for_crypto = info['market_cap']
                        currency_site = info['site']
                        currency_name = info['name']
                    except : 
                        'ok'
                    if  currency_type == 'iran(irt)' : 

                            try :
                                
                                
                                # nobitx status = no edit
                                response = requests.get(api_price_url+"USDTIRT")
                                response = response.json()
                                irt_to_usdt_price =  response['trades'][0]['price'] 
                                irt_to_usdt_price = str(irt_to_usdt_price).replace("'",'')
                                irt_to_usdt_price = str(irt_to_usdt_price).strip("( )").replace(",",'')
                                irt_to_usdt_price = irt_to_usdt_price.replace(""," ")
                                irt_to_usdt_price = irt_to_usdt_price.split()
                                irt_to_usdt_price.pop(-1)
                                irt_to_usdt_price = str(irt_to_usdt_price)
                                irt_to_usdt_price = irt_to_usdt_price.replace("'",'')
                                irt_to_usdt_price = irt_to_usdt_price.replace(",","")
                                irt_to_usdt_price = irt_to_usdt_price.strip("[ ]")
                                irt_to_usdt_price = irt_to_usdt_price.replace(" ",'')
                                cryptocurrency_price = float(cryptocurrency_price.replace(',','')) 
                                irt_to_usdt_price = float(irt_to_usdt_price)
                                change_irt_fi = float(cryptocurrency_change_usd.replace(',','')) * irt_to_usdt_price
                                crypto_price_irt = irt_to_usdt_price * cryptocurrency_price
                                
                                if int(float(str(crypto_price_irt).replace("-",''))) == 0 :
                                    crypto_price_irt = str(f'{(float(crypto_price_irt)):,}')
                                elif int(float(str(crypto_price_irt).replace("-",''))) > 0 :
                                    crypto_price_irt = "%.2f" % crypto_price_irt
                                    crypto_price_irt = str(f'{(float(crypto_price_irt)):,}')

                                if int(float(str(change_irt_fi).replace("-",''))) == 0 :
                                    change_irt_fi = str(f'{(float(change_irt_fi)):,}')
                                elif int(float(str(change_irt_fi).replace("-",''))) > 0 :
                                    change_irt_fi = "%.2f" % change_irt_fi
                                    change_irt_fi = str(f'{(float(change_irt_fi)):,}')
                                
                                
                                
                    
                                
                                global tg_message_to_send_sort_irt
                                global tg_message_to_send_irt
                                tg_message_to_send_irt = '\ncrypto currency full name 🏢 :\n'.upper()
                                tg_message_to_send_irt += f"<a href='{currency_site}'>{currency_name.upper()}</a>"
                                tg_message_to_send_irt += "\n"+"--------------------------------------------------------------------"+'\nCURRENCY 🪙 :\n'+'IRT\n'+"--------------------------------------------------------------------"+'\n'+symbol_crypto.upper()+" crypto currency PRICE 🌋 :\n".upper() +str(crypto_price_irt)  +'\n'+"--------------------------------------------------------------------"+"\n"+symbol_crypto.upper()+" 24H CHANGE ⏳ :\n" + str(change_irt_fi)+' \n'+"--------------------------------------------------------------------"+'\n'+symbol_crypto.upper()+' 24H CHANGE PERCENT ⏳ :\n'+str(cryptocurrency_change_percent)+" \n"+"--------------------------------------------------------------------"+"\n"+symbol_crypto.upper()+" MARKET CAP 🏦 :\n"+str(market_cap_for_crypto)+'\n'+'--------------------------------------------------------------------'
                                
                                tg_message_to_send_sort_irt = symbol_crypto.upper()+" crypto currency PRICE 🌋 :\n".upper() + str(crypto_price_irt) +'\n'+"--------------------------------------------------------------------"+"\n"+symbol_crypto.upper()+" 24H CHANGE ⏳ :\n" +str(change_irt_fi)+'\n'+"--------------------------------------------------------------------"+'\n'+symbol_crypto.upper()+' 24H CHANGE PERCENT ⏳ :\n'+str(cryptocurrency_change_percent)
                            except : 
                                'ok'
                    elif  currency_type == 'united states(usd)' :   
                            try:
                                
                                global tg_message_to_send_sort_usd
                                global tg_message_to_send_usd
                                tg_message_to_send_usd = '\ncrypto currency full name 🏢 :\n'.upper()
                                tg_message_to_send_usd += f"<a href='{currency_site}'>{currency_name.upper()}</a>"
                                tg_message_to_send_usd += "\n"+"--------------------------------------------------------------------"+'\nCURRENCY 🪙 :\n'+'USD 🇺🇸\n'+"--------------------------------------------------------------------"+'\n'+symbol_crypto.upper()+" Crypto Currency PRICE 🌋 :\n".upper() + str(cryptocurrency_price) +' 💲\n'+"--------------------------------------------------------------------"+"\n"+symbol_crypto.upper()+" 24H CHANGE ⏳ :\n" +str(cryptocurrency_change_usd)+' 💲\n'+"--------------------------------------------------------------------"+'\n'+symbol_crypto.upper()+' 24H CHANGE PERCENT ⏳ :\n'+str(cryptocurrency_change_percent)+" \n"+"--------------------------------------------------------------------"+"\n"+symbol_crypto.upper()+" MARKET CAP 🏦 :\n"+str(market_cap_for_crypto)+"\n"+"--------------------------------------------------------------------"
                                
                                tg_message_to_send_sort_usd =symbol_crypto.upper()+" crypto currency PRICE 🌋 :\n".upper() + str(cryptocurrency_price) +' 💲\n'+"--------------------------------------------------------------------"+"\n"+symbol_crypto.upper()+" 24H CHANGE ⏳ :\n" +str(cryptocurrency_change_usd)+' 💲\n'+"--------------------------------------------------------------------"+'\n'+symbol_crypto.upper()+' 24H CHANGE PERCENT ⏳ :\n'+str(cryptocurrency_change_percent)
                            except : 
                                'ok'
                    elif currency_type != 'iran(irt)' and currency_type != 'united states(usd)' : 
                            try:
                                global tg_message_to_send_sort_glob
                                global tg_message_to_send_glob
                                cryptocurrency_price = float(cryptocurrency_price.replace(',','')) * currence_price_to_usdt 
                                if int(float(str(cryptocurrency_price).replace("-",''))) == 0 :
                                    cryptocurrency_price = str(f'{(float(cryptocurrency_price)):,}')
                                elif int(float(str(cryptocurrency_price).replace("-",''))) > 0 :
                                    cryptocurrency_price = "%.2f" % cryptocurrency_price
                                    cryptocurrency_price = str(f'{(float(cryptocurrency_price)):,}')

                                cryptocurrency_change_usd = float(cryptocurrency_change_usd.replace(',','')) * currence_price_to_usdt
                                if int(float(str(cryptocurrency_change_usd).replace("-",''))) == 0 :
                                    cryptocurrency_change_usd = str(f'{(float(cryptocurrency_change_usd)):,}')
                                
                                elif int(float(str(cryptocurrency_change_usd).replace("-",''))) > 0 :
                                    cryptocurrency_change_usd = "%.2f" % cryptocurrency_change_usd
                                    cryptocurrency_change_usd = str(f'{(float(cryptocurrency_change_usd)):,}')



                                tg_message_to_send_glob = '\ncrypto currency full name 🏢 :\n'.upper()
                                tg_message_to_send_glob += f"<a href='{currency_site}'>{currency_name.upper()}</a>"
                                tg_message_to_send_glob += "\n"+"--------------------------------------------------------------------"+'\nCURRENCY 🪙 :\n'+f'{curences_list_from_config[currency_type]}\n'+"--------------------------------------------------------------------"+'\n'+symbol_crypto.upper()+" Crypto Currency PRICE 🌋 :\n".upper() + str(cryptocurrency_price) +'\n'+"--------------------------------------------------------------------"+"\n"+symbol_crypto.upper()+" 24H CHANGE ⏳ :\n" +str(cryptocurrency_change_usd)+'\n'+"--------------------------------------------------------------------"+'\n'+symbol_crypto.upper()+' 24H CHANGE PERCENT ⏳ :\n'+str(cryptocurrency_change_percent)+" \n"+"--------------------------------------------------------------------"+"\n"+symbol_crypto.upper()+" MARKET CAP 🏦 :\n"+str(market_cap_for_crypto)+"\n"+"--------------------------------------------------------------------"
                                
                                tg_message_to_send_sort_glob =symbol_crypto.upper()+" crypto currency PRICE 🌋 :\n".upper() + str(cryptocurrency_price) +'\n'+"--------------------------------------------------------------------"+"\n"+symbol_crypto.upper()+" 24H CHANGE ⏳ :\n" +str(cryptocurrency_change_usd)+'\n'+"--------------------------------------------------------------------"+'\n'+symbol_crypto.upper()+' 24H CHANGE PERCENT ⏳ :\n'+str(cryptocurrency_change_percent)
                            except : 
                                'ok'




                    global tg_message_to_send_news_crypto
                    tg_message_to_send_news_crypto = f'The latest news about {currency_name} ❗️'+"\n"+"--------------------------------------------------------------------"+'\nName of the news agency ✒️ :\n'.title()+str(last_news_agency)+"\n"+"-------------------------------------------------------------------"+'\nNews title 🗞 :\n'.title()+str(last_news_title)+'\n'+"-------------------------------------------------------------------"+'\n'
                    tg_message_to_send_news_crypto += f"<a href='{last_news_link}'>Click To Read Full Details 📰</a>"
                    tg_message_to_send_news_crypto += "\n"+"--------------------------------------------------------------------"
                    chat_id = message.chat.id
                    button_bar = types.InlineKeyboardButton('📚Click to get more information📚'.title(), callback_data='click get more information for crypto currency market')
                    button_bar2 = types.InlineKeyboardButton('🗞Click to get the latest news🗞'.title(), callback_data='click to get the latest news for crypto currency market')
                    keyboard = types.InlineKeyboardMarkup()
                    keyboard.add(button_bar)
                    keyboard.add(button_bar2)
                    message_for_edit = message
                    if currency_type == 'iran(irt)' : 
                        bot.send_message(chat_id, tg_message_to_send_sort_irt, parse_mode = 'HTML', disable_web_page_preview=False, reply_markup=keyboard)
                    elif currency_type == 'united states(usd)' :
                        bot.send_message(chat_id, tg_message_to_send_sort_usd, parse_mode = 'HTML', disable_web_page_preview=False, reply_markup=keyboard)
                    elif currency_type != 'united states(usd)' and currency_type != 'iran(irt)' :
                        bot.send_message(chat_id, tg_message_to_send_sort_glob, parse_mode = 'HTML', disable_web_page_preview=False, reply_markup=keyboard)


            except :
                    problem ='Make sure you enter the currency symbol correctly.'
                    bot.reply_to(message,problem)
            
        elif message.text == "click here to get the usdt/irt price" : 
            try :
                response = requests.get(api_price_url+"USDTIRT")
                response = response.json()
                irt_to_usdt_price =  response['trades'][0]['price'] 
                irt_to_usdt_price = str(irt_to_usdt_price).replace("'",'')
                irt_to_usdt_price = str(irt_to_usdt_price).strip("( )").replace(",",'')
                irt_to_usdt_price = irt_to_usdt_price.replace(""," ")
                irt_to_usdt_price = irt_to_usdt_price.split()
                irt_to_usdt_price.pop(-1)
                irt_to_usdt_price = str(irt_to_usdt_price)
                irt_to_usdt_price = irt_to_usdt_price.replace("'",'')
                irt_to_usdt_price = irt_to_usdt_price.replace(",","")
                irt_to_usdt_price = irt_to_usdt_price.strip("[ ]")
                irt_to_usdt_price = irt_to_usdt_price.replace(" ",'')
                bot.reply_to(message,"USDT/IRT PRICE : "+str(f'{(int(irt_to_usdt_price)):,}')+" TOMAN")
            except : 
                problem ='The problem is with the source servers 🛠.'
                bot.reply_to(message,problem)

        elif "click here to get the usdt" in message.text.replace("/",' '): 
            try:
                if currency_type == currency_type :
                    if message.text == f"click here to get the usdt/{curences_list_from_config[currency_type].lower()} price".replace('=x','') and currency_type != 'iran(irt)':
                                currence_countery_price_to_usdt = curences_list_from_config[currency_type]

                                agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
                                headers = {'User-Agent': agent}
                                url = f'https://finance.yahoo.com/quote/{currence_countery_price_to_usdt}?p={currence_countery_price_to_usdt}'
                                response_price_to_usdt  = requests.get(url, headers=headers)
                                if response_price_to_usdt.status_code == 200 :
                                    response_price_to_usdt = (response_price_to_usdt.text)
                                    soup = BeautifulSoup( response_price_to_usdt , 'html.parser')
                                    when_live_stock_changes_is_none = soup.find(class_ = "D(ib) Mend(20px)")
                                    # FOR LIVE price
                                    live_stock_changes = soup.find(class_ = "Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)")
                                    when_live_stock_changes_is_none = soup.find(class_ = "D(ib) Mend(20px)")
                                    # get live price
                                    price = when_live_stock_changes_is_none.find( class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)" )
                                    price = str(price).split()
                                    price = price[-1].replace("</fin-streamer>",'')
                                    price_index = price.index(">")
                                    price = price[price_index : ].replace(">",'')
                                    price=str(price).replace(',','')

                                    currence_price_to_usdt = float(price)
                                    currence_price_to_usdt = "%.2f" % currence_price_to_usdt
                                    bot.reply_to(message,f"USDT/{curences_list_from_config[currency_type]} PRICE : ".replace('=X','')+str(f'{(float(currence_price_to_usdt)):,}'))
                                else:
                                    problem ='The problem is with the source servers 🛠.'
                                    bot.reply_to(message,problem)




            except:
                    chat_id = message.chat.id
                    markup = telebot.types.ReplyKeyboardMarkup(True,False)
                    markup.row('👇🏻Choose one of the Nine options👇🏻\nbelow according to your desired currency'.title())
                    markup.row('UNITED STATES(USD)')
                    markup.row('JAPAN(JPY)','england(gbp)'.upper())
                    markup.row('CHINA(CNH)','GERMANY(EUR)')
                    markup.row('INDIA(INR)','SOUTH KOREA(KRW)')
                    markup.row('IRAN(IRT)','RUSSIA(RUB)')
                    markup.row('Return to main page ↩️'.title(),'Return to the keywords list page 🔙'.title())
                    bot.send_message(chat_id,'🛑 Please select your currency first to receive the prices according to that currency 🛑\n'.title(), reply_markup=markup)

        elif message.text ==  'برای شروع نسخه فارسی کلیک کنید':   
            chat_id = message.chat.id 
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('🤖 معرفی ربات 🤖')
            markup.row('🗂 اگر اطلاعات بیشتری نیاز دارید 🗂 \n📨 با ما ارتباط برقرار کنید 📨'.title())
            markup.row('🗝 هر کلید چه کاری می تواند انجام دهد؟ 🗝'.title())
            markup.row('📓 لیست کلمات کلیدی 📓'.title())
            markup.row('بازگشت به صفحه انتخاب نسخه 🔙')
            bot.send_message(chat_id,'نسخه فارسی شروع شد.'.title(), reply_markup=markup)

        elif message.text == 'بازگشت به صفحه انتخاب نسخه 🔙' :
            chat_id = message.chat.id 
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('برای شروع نسخه فارسی کلیک کنید')
            markup.row('Click to start the English version'.title())
            bot.send_message(chat_id,'بازگشت به صفحه انتخاب نسخه با موفقیت انجام شد ✅'.title(), reply_markup=markup)

        elif message.text in Bot_Info_fa:
            bot.reply_to(message,Bot_Info_fa[message.text])
        
        elif   message.text == '🗝 هر کلید چه کاری می تواند انجام دهد؟ 🗝'  : 
            bot.reply_to(message,bot_kaywords_fa)

        
        elif message.text == '📓 لیست کلمات کلیدی 📓' : 
            chat_id = message.chat.id 
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('📊 قیمت بورس 📊'.title())
            markup.row('💵 قیمت ارزهای دیجیتال 💵'.title())
            markup.row('📒 فهرست اطلاعات 📒'.title())
            markup.row('👨🏻‍💻 تراکنش های کریپتوای را بررسی کنید 👨🏻‍💻')
            markup.row('بازگشت به صفحه اصلی ↩️'.title())
            bot.send_message(chat_id,'لیست کلمات کلیدی با موفقیت باز شد ✅', reply_markup=markup )
            
        elif message.text == 'بازگشت به صفحه اصلی ↩️' : 
            chat_id = message.chat.id 
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('🤖 معرفی ربات 🤖')
            markup.row('🗂 اگر اطلاعات بیشتری نیاز دارید 🗂 \n📨 با ما ارتباط برقرار کنید 📨'.title())
            markup.row('🗝 هر کلید چه کاری می تواند انجام دهد؟ 🗝'.title())
            markup.row('📓 لیست کلمات کلیدی 📓'.title())
            markup.row('بازگشت به صفحه انتخاب نسخه 🔙')
            bot.send_message(chat_id,'بازگشت به صفحه اصلی با موفقیت انجام شد ✅', reply_markup=markup)

        
        elif message.text == 'بازگشت به صفحه فهرست کلمات کلیدی 🔙' : 
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('📊 قیمت بورس 📊'.title())
            markup.row('💵 قیمت ارزهای دیجیتال 💵'.title())
            markup.row('📒 فهرست اطلاعات 📒'.title())
            markup.row('👨🏻‍💻 تراکنش های کریپتوای را بررسی کنید 👨🏻‍💻')
            markup.row('بازگشت به صفحه اصلی ↩️'.title())
            bot.send_message(chat_id,'بازگشت به صفحه فهرست کلمات کلیدی با موفقیت انجام شد ✅'.title(), reply_markup=markup )

        elif message.text == '💵 قیمت ارزهای دیجیتال 💵' : 
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('👇🏻با توجه به ارز مورد نظر خود👇🏻\nیکی از نه گزینه زیر را انتخاب کنید'.title())
            markup.row('ایالات متحده(دلار)')
            markup.row('ژاپن(ین)','انگلستان(پوند)'.upper())
            markup.row('چین(یوان)','آلمان(یورو)')
            markup.row('هند(روپیه)','کره جنوبی(وون)')
            markup.row('ایران(تومان)','روسیه(روبل)')
            markup.row('بازگشت به صفحه اصلی ↩️'.title(),'بازگشت به صفحه فهرست کلمات کلیدی 🔙'.title())
            bot.send_message(chat_id,'لیست واحد های پولی با موفقیت باز شد ✅'.title(), reply_markup=markup )

        if message.text in curences_list_from_config_fa : 
            text_1 = "`"+"مخفف نام ارز دیجیتال : "+"`"
            global currency_type_fa
            currency_type_fa = message.text
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            
            if currency_type_fa == 'ایالات متحده(دلار)' :
                markup.row('🔴 برای انجام صحیح مراحل 🔴\nبه مثال زیر توجه کنید'.title())
                markup.row('مخفف نام ارز دیجیتال : BTC')
                markup.row('بازگشت به صفحه اصلی ↩️'.title(),'بازگشت به صفحه قبلی 🔙'.title())
                bot.send_message(chat_id,'📌 مهم\n'.upper()+' برای وارد کردن نام ارز دیجیتال مورد نظر خود، روی متن زیر کلیک کنید و مخفف نام ارز دیجیتال مورد نظر خود را به انگلیسی به انتهای متن اضافه کنید.'.title(), reply_markup=markup )
                bot.send_message(chat_id,text_1,parse_mode='MarkdownV2')
                    
            elif currency_type_fa != 'ایالات متحده(دلار)' :
                markup.row('🔴 برای انجام صحیح مراحل 🔴\nبه مثال زیر توجه کنید'.title())
                markup.row(f'برای دریافت قیمت تتر/{curences_list_from_config_fa[currency_type_fa]} اینجا را کلیک کنید')
                markup.row('مخفف نام ارز دیجیتال : BTC')
                markup.row('بازگشت به صفحه اصلی ↩️'.title(),'بازگشت به صفحه قبلی 🔙'.title())
                bot.send_message(chat_id,'📌 مهم\n'.upper()+' برای وارد کردن نام ارز دیجیتال مورد نظر خود، روی متن زیر کلیک کنید و مخفف نام ارز دیجیتال مورد نظر خود را به انگلیسی به انتهای متن اضافه کنید.'.title(), reply_markup=markup )
                bot.send_message(chat_id,text_1,parse_mode='MarkdownV2')
    
        elif message.text == 'بازگشت به صفحه قبلی 🔙' : 
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('👇🏻با توجه به ارز مورد نظر خود👇🏻\nیکی از نه گزینه زیر را انتخاب کنید'.title())
            markup.row('ایالات متحده(دلار)')
            markup.row('ژاپن(ین)','انگلستان(پوند)'.upper())
            markup.row('چین(یوان)','آلمان(یورو)')
            markup.row('هند(روپیه)','کره جنوبی(وون)')
            markup.row('ایران(تومان)','روسیه(روبل)')
            markup.row('بازگشت به صفحه اصلی ↩️'.title(),'بازگشت به صفحه فهرست کلمات کلیدی 🔙'.title())
            bot.send_message(chat_id,'با موفقیت به صفحه قبل بازگشت ✅'.title(), reply_markup=markup )

        
        elif message.text == '📒 فهرست اطلاعات 📒'  :
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True, False)
            markup.row('ارز دیجیتال چیست ؟ 🤔'.title()) 
            markup.row('ارز دیجیتال ها چگونه کار می کنند؟ 🤯'.title())
            markup.row('چگونه ارز دیجیتال بخریم؟ 😎'.title())
            markup.row('نحوه حمایت مالی با استفاده از ارز دیجیتال ؟ 🤑'.title())
            markup.row('🗂 اگر اطلاعات بیشتری نیاز دارید 🗂 \n📨 با ما ارتباط برقرار کنید 📨'.title())
            markup.row('بازگشت به صفحه اصلی ↩️'.title(),'بازگشت به صفحه فهرست کلمات کلیدی 🔙'.title())
            bot.send_message(chat_id,'لیست اطلاعات با موفقیت باز شد ✅'.title(), reply_markup=markup )

        if message.text in crypto_info_fa :
            bot.reply_to(message,crypto_info_fa[message.text])

        elif message.text == '👨🏻‍💻 تراکنش های کریپتوای را بررسی کنید 👨🏻‍💻':
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True,False)
            markup.row('👇🏻یکی از دو گزینه زیر را انتخاب کنید👇🏻\nبا توجه به شبکه ارز مورد نظر خود'.title())
            markup.row('ترون(TRC20)','اتریوم(ERC20)'.upper())
            markup.row('بازگشت به صفحه اصلی ↩️'.title(),'بازگشت به صفحه فهرست کلمات کلیدی 🔙'.title())
            bot.send_message(chat_id,'لیست شبکه ارزها با موفقیت باز شد ✅'.title(), reply_markup=markup)

        elif  message.text ==  'ترون(trc20)' or message.text == 'اتریوم(erc20)' : 
            global tx_hash_type_fa
            tx_hash_type_fa = message.text
            text_3 = "`"+"هش تراکنش : "+"`"
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True,False)
            markup.row('🔴 برای انجام صحیح مراحل 🔴\nبه مثال زیر توجه کنید'.title())
            markup.row('هش تراکنش : z34zvo2mxix3xz4z5')
            markup.row('بازگشت به صفحه اصلی ↩️'.title(),'بازگشت به صفحه شبکه ارز دیجیتال 🔙'.title())
            bot.send_message(chat_id,'📌 مهم\n'.upper()+' متن زیر را در کلیپ بورد خود کپی کنید و در پایان هش تراکنش خود را به آن اضافه کنید.'.title()+'', reply_markup=markup )
            bot.send_message(chat_id,text_3,parse_mode='MarkdownV2')

        elif message.text == 'بازگشت به صفحه شبکه ارز دیجیتال 🔙' :
            chat_id = message.chat.id
            markup = telebot.types.ReplyKeyboardMarkup(True,False)
            markup.row('👇🏻یکی از دو گزینه زیر را انتخاب کنید👇🏻\nبا توجه به شبکه ارز مورد نظر خود'.title())
            markup.row('ترون(TRC20)','اتریوم(ERC20)'.upper())
            markup.row('بازگشت به صفحه اصلی ↩️'.title(),'بازگشت به صفحه فهرست کلمات کلیدی 🔙'.title())
            bot.send_message(chat_id,'با موفقیت به صفحه شبکه ارز دیجیتال بازگشتید ✅'.title(), reply_markup=markup)




        elif str(message.text.replace(":"," ").split()[0 : -1]).replace("'",'').replace(",","").strip("[ ]") == 'هش تراکنش' : 
            tx_hash = message.text.replace('هش تراکنش','')
            tx_hash = tx_hash.replace(':','').replace(" ",'')
            tx_hash_type_status = ''
            keyboard = types.InlineKeyboardMarkup()
            chat_id = message.chat.id
            try : 
                if tx_hash_type_fa == tx_hash_type_fa:
                    tx_hash_type_status = 'ok'
            except:
                chat_id = message.chat.id
                markup = telebot.types.ReplyKeyboardMarkup(True,False)
                markup.row('👇🏻یکی از دو گزینه زیر را انتخاب کنید👇🏻\nبا توجه به شبکه ارز مورد نظر شما'.title())
                markup.row('ترون(TRC20)','اتریوم(ERC20)'.upper())
                markup.row('بازگشت به صفحه اصلی ↩️'.title(),'بازگشت به صفحه فهرست کلمات کلیدی 🔙'.title())
                bot.send_message(chat_id,'لطفاً ابتدا شبکه ارز دیجیتال خود را مشخص کنید .'.title(), reply_markup=markup)
            
            
            if tx_hash_type_status == 'ok' :
                if tx_hash_type_fa == 'اتریوم(erc20)':
                    try:   
                        global contract_confirmed_or_not_status_erc20_fa
                        contract_confirmed_or_not_status_erc20_fa = ''
                        response = requests.post(etherscan_url+tx_hash,headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
                        if response.status_code == 200 : 
                            soup = BeautifulSoup(response.text , 'html.parser')
                            status_result = str(soup.find_all("span", {"class": "u-label u-label--sm u-label--value u-label--success rounded"})).count("Success")
                            contract_confirmed_or_not_status_erc20_fa = ''
                            if status_result == 1 : 
                                contract_confirmed_or_not_status_erc20_fa = 'معامله تایید شد ✅'
                            elif status_result != 1 :
                                contract_confirmed_or_not_status_erc20_fa = 'معامله تایید نشده ❌\nیا پیدا نشد ❌'
                            tg_message_to_send_hash_erc20 = contract_confirmed_or_not_status_erc20_fa.upper()+'\n'+"--------------------------------------------------------------------"+'\n'
                            tg_message_to_send_hash_erc20 += f"<a href='https://etherscan.io/tx/{tx_hash}'>برای دریافت اطلاعات بیشتر کلیک کنید</a>"
                            tg_message_to_send_hash_erc20 += '\n'+"--------------------------------------------------------------------"
                                

                            bot.send_message(chat_id, tg_message_to_send_hash_erc20, parse_mode = 'HTML', disable_web_page_preview=False, reply_markup=keyboard)

                            

                    except : 
                        problem ='لطفا از صحت شماره تراکنش خود مطمئن شوید.'
                        bot.reply_to(message,problem)

            if tx_hash_type_status == 'ok' :

                if tx_hash_type_fa == 'ترون(trc20)' : 
                    
                        agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
                        headers = {'User-Agent': agent}

                        url_tx_hash = f"https://apilist.tronscanapi.com/api/transaction-info?hash={tx_hash}"

                        response_for_trx = requests.get(url_tx_hash, headers=headers)
                        if response_for_trx.status_code == 200 :
                            try :

                                response_for_trx = (response_for_trx.text)

                                response_for_trx = (json.loads(response_for_trx))

                                contract_confirmed = response_for_trx['confirmed']

                                if str(contract_confirmed) ==  'True' : 
                                    contract_confirmed = 'معامله تایید شد ✅'.upper()
                                elif str(contract_confirmed) != 'True' : 
                                    contract_confirmed = 'معامله تایید نشده ❌\nیا پیدا نشد ❌'
                                tg_message_to_send_hash_trc20 = contract_confirmed.upper()+'\n'+"--------------------------------------------------------------------"+'\n'
                                tg_message_to_send_hash_trc20 += f"<a href='https://tronscan.org/#/transaction/{tx_hash}'>برای دریافت اطلاعات بیشتر کلیک کنید</a>"
                                tg_message_to_send_hash_trc20 += '\n'+"--------------------------------------------------------------------"
                                bot.send_message(chat_id, tg_message_to_send_hash_trc20, parse_mode = 'HTML', disable_web_page_preview=False, reply_markup=keyboard)
                            except :
                                problem ='لطفا از صحت شماره تراکنش خود مطمئن شوید.'
                                bot.reply_to(message,problem)
                        else :
                            problem ='لطفا از صحت شماره تراکنش خود مطمئن شوید.'
                            bot.reply_to(message,problem)


        elif message.text == '📊 قیمت بورس 📊' :
                text = "`"+"مخفف نام سهام : "+"`"
                chat_id = message.chat.id
                markup = telebot.types.ReplyKeyboardMarkup(True,False)
                markup.row('🔴 برای انجام صحیح مراحل 🔴\nبه مثال زیر توجه کنید'.title())
                markup.row(' مخفف نام سهام : AAPL')
                markup.row('بازگشت به صفحه اصلی ↩️'.title(),'بازگشت به صفحه فهرست کلمات کلیدی 🔙'.title())
                bot.send_message(chat_id,'📌 مهم\n'.upper()+' برای وارد کردن نام سهام مورد نظر خود، روی متن زیر کلیک کنید و مخفف نام سهام مورد نظر خود را به انگلیسی به انتهای متن اضافه کنید.'.title(), reply_markup=markup )
                bot.send_message(chat_id,text,parse_mode='MarkdownV2')
       

        elif str(message.text.replace(":"," ").split()[0 : -1]).replace("'",'').replace(",","").strip("[ ]") == 'مخفف نام سهام' : 
            try :
                stock_name = message.text.replace('مخفف نام سهام','')
                stock_name = stock_name.replace(":",'').replace(" ",'')
                global symbol_fa
                symbol_fa = stock_name.upper()
                agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
                headers = {'User-Agent': agent}
                url = f'https://finance.yahoo.com/quote/{symbol_fa}?p={symbol_fa}'
                response = requests.get(url, headers=headers)
                response = (response.text)
                soup = BeautifulSoup( response , 'html.parser')
                global stock_price_global_fa
                global stock_change_percent_global_fa
                global stock_change_usd_global_fa


                stock_price_global_fa = ""
                stock_change_usd_global_fa = ""
                stock_change_percent_global_fa = ""
                # FOR LIVE STOCK
                global live_stock_changes_fa
                live_stock_changes_fa = soup.find(class_ = "Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)")
                global color_status_fa
                color_status_fa = ""
                if str(live_stock_changes_fa) != "None" : 
                    try :
                        market_price_for_live_stokc = str(live_stock_changes_fa.find(class_="C($primaryColor) Fz(24px) Fw(b)"))
                        market_price_for_live_stokc = market_price_for_live_stokc.replace(">",' ').split()[-1].replace("</fin-streamer",'')
                        stock_price_global_fa = market_price_for_live_stokc

                        if "C($negativeColor)" in str(live_stock_changes_fa):
                            color_status_fa = color_status_fa = "C($negativeColor)"
                        elif "C($positiveColor)" in str(live_stock_changes_fa) :
                            color_status_fa = color_status_fa ="C($positiveColor)"
                        elif "C($negativeColor)" and  "C($positiveColor)" not in str(live_stock_changes_fa):
                            color_status_fa = color_status_fa =""

                        live_stock_changes_fa = live_stock_changes_fa.find_all(class_ = color_status_fa)

                        market_price_change_usd_for_live_stokc = str(live_stock_changes_fa[0]).replace(f'<span class="{color_status_fa}">','').replace("</span>",'').strip("[ ]")
                        stock_change_usd_global_fa = market_price_change_usd_for_live_stokc

                        market_price_change_percent_for_live_stokc = str(live_stock_changes_fa[1]).replace(f'<span class="{color_status_fa}">','').replace("</span>",'').strip("( )")
                        
                        stock_change_percent_global_fa = market_price_change_percent_for_live_stokc

                    except:
                        'ok'
                elif str(live_stock_changes_fa) == "None" :

                    try:

                        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        when_live_stock_changes_is_none = soup.find(class_ = "D(ib) Mend(20px)")
                        # get live price
                        price = when_live_stock_changes_is_none.find( class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)" )
                        price = str(price).split()
                        price = price[-1].replace("</fin-streamer>",'')
                        price_index = price.index(">")
                        price = price[price_index : ].replace(">",'')
                        stock_price_global_fa = price
                        # get change usd
                        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        color_status_fa = ("")

                        if "C($negativeColor)" in str(when_live_stock_changes_is_none):
                            color_status_fa = color_status_fa = "C($negativeColor)"
                        elif "C($positiveColor)" in str(when_live_stock_changes_is_none) :
                            color_status_fa = color_status_fa ="C($positiveColor)"
                        elif "C($negativeColor)" and  "C($positiveColor)" not in str(when_live_stock_changes_is_none):
                            color_status_fa = color_status_fa =""
                        
                        market_changes_when_live_stock_is_none = when_live_stock_changes_is_none.find_all (class_ = color_status_fa )

                        change_usd = (str(market_changes_when_live_stock_is_none[0]).replace(f"""<span class="{color_status_fa}">""",'').replace("</span>",'').strip("[ ]"))
                        stock_change_usd_global_fa = change_usd
                        # get change percent
                        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        change_percent = (str(market_changes_when_live_stock_is_none[1]).replace(f"""<span class="{color_status_fa}">""",'').replace("</span>",'').strip("( )"))
                        stock_change_percent_global_fa = change_percent                
                    except : 
                        'ok'
                    # for market status
            
                try :
                    ## for stokc holders
                    ## for stokc holders



                    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
                    headers = {'User-Agent': agent}
                    ## for stokc holders
                    url_for_holders = f'https://finance.yahoo.com/quote/{symbol_fa}/holders?p={symbol_fa}'

                    response_holders = requests.get(url_for_holders, headers=headers)
                    response_holders = (response_holders.text)
                    soup_holders = BeautifulSoup( response_holders , 'html.parser')
                    ## for holders

                    top_one_holder_for_edit = (soup_holders.find(class_ = "Mt(25px) Ovx(a) W(100%)").find(class_ = "BdT Bdc($seperatorColor) Bgc($hoverBgColor):h Whs(nw) H(36px)"))

                    top_one_name = (top_one_holder_for_edit.find(class_ = "Ta(start) Pend(10px)"))
                    top_one_name =(str(top_one_name).replace('<td class="Ta(start) Pend(10px)">','').replace("</td>",''))

                    top_one_holder_for_edit_by_class = top_one_holder_for_edit.find_all(class_= "Ta(end) Pstart(10px)")

                    top_one_shares = (str(top_one_holder_for_edit_by_class[0]).replace('<td class="Ta(end) Pstart(10px)">','').replace("</td>",''))

                    top_one_shares_date_reported = (str(top_one_holder_for_edit_by_class[1:2]).replace('<td class="Ta(end) Pstart(10px)"><span>','').replace("</span></td>",'').strip("[ ]"))
                    top_one_shares_date_reported=top_one_shares_date_reported.replace(",",'').replace(" ",'/')

                    top_one_shares_usd_va = (str(top_one_holder_for_edit_by_class[-1]).replace('<td class="Ta(end) Pstart(10px)">','').replace("</td>",''))

                    #----------------------------------------------------------------------------------------------
                except : 
                    top_one_name = 'N/A'
                    top_one_shares = 'N/A'
                    top_one_shares_date_reported = 'N/A'
                    top_one_shares_usd_va = 'N/A'
                try: 
                    code_for_last_news_edit_for_all_types = ''
                    code_for_last_news_edit_just_text = (soup.find(class_="Ov(h) Pend(14%) Pend(44px)--sm1024"))
                
                    if str(code_for_last_news_edit_just_text).lower() == 'none':
                        code_for_last_news_edit_for_all_types = "Ov(h) Pend(44px) Pstart(25px)"
                    elif str(code_for_last_news_edit_just_text).lower() != 'none':
                        code_for_last_news_edit_for_all_types = "Ov(h) Pend(14%) Pend(44px)--sm1024"
                    
                    try :     
                        test = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="C(#959595) Fz(11px) D(ib) Mb(6px)")
                    except: 
                        code_for_last_news_edit_for_all_types = 'js-stream-content Pos(r)'


                    
                    last_news_agency = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="C(#959595) Fz(11px) D(ib) Mb(6px)")
                    last_news_agency = (str(last_news_agency).replace('<div class="C(#959595) Fz(11px) D(ib) Mb(6px)">','').replace("</div>",''))
                    
                    last_news_title = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="Mb(5px)")
                    last_news_title = (str(last_news_title).replace(">",' ').replace("<"," "))
                    last_news_title_index = (last_news_title.split().index('/u'))
                    last_news_title =  last_news_title.split()[last_news_title_index+1 : -2]
                    last_news_title = (str(last_news_title).replace("'","").replace(",",'').strip("[ ]")+".")


                    last_news_link = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="Mb(5px)").find(class_="js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled")
                    last_news_link_index = (str(last_news_link).replace("js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled",'').replace(">",' ').replace('"',' ').split().index("href="))
                    last_news_link = (str(last_news_link).replace("js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled",'').replace(">",' ').replace('"',' ').split()[last_news_link_index+1])
                    last_news_link = ("https://finance.yahoo.com"+last_news_link)

                    
                except : 
                    last_news_agency = 'N/A'
                    last_news_title = 'N/A'
                    last_news_link = 'N/A'
                    

                try : 
                    market_status_time = soup.find(class_ = "D(ib) Fl(end) Pb(6px) Fz(xs) Fw(b) fin-update-style").find(class_ = "C($c-fuji-orange-b)")
                    market_status_time = (str(market_status_time).replace('<span class="C($c-fuji-orange-b)" data-id="mk-msg">','').replace("</span>",''))
                    market_status_time = market_status_time.replace(".",'')
                    if str(market_status_time).lower() == "none" :
                        market_status_time = market_status_time = "بازارهای آمریکا بسته شد"
                    elif  str(market_status_time).lower() != 'none' and 'close' in str(market_status_time).lower()  : 
                        market_status_time = str(market_status_time).lower().replace('us markets close in','').replace('hours','ساعت و').replace('minutes','دقیقه ')
                        market_status_time += 'تا بسته شدن بازار های آمریکا'
                    elif str(market_status_time).lower() != 'none' and 'open' in str(market_status_time).lower()  : 
                        market_status_time = str(market_status_time).lower().replace('us markets open in','').replace('hours','ساعت و').replace('minutes','دقیقه ')
                        market_status_time += 'تا باز شدن بازار های آمریکا'
                except:
                    market_status_time = "N/A"

                try :
                    info = info_stock(symbol_fa)

                    market_cap=info['market_cap']
                    countre_campone = info['country']
                    comeny_site = info["site"]
                    comeny_name = info['name']
                except : 
                    'ok'
                chat_id = message.chat.id
                
                global tg_message_to_send_fa
                tg_message_to_send_fa = market_status_time+"❗️"+"\n"+"--------------------------------------------------------------------"+'\nکشور 🌍 :\n'+str(countre_campone)+"\n"+"-------------------------------------------------------------------"+'\nنام کامل شرکت 🏢 :\n'
                tg_message_to_send_fa += f"<a href='{comeny_site}'>{comeny_name}</a>"
                tg_message_to_send_fa += "\n"+"--------------------------------------------------------------------"+'\nواحد پول 🪙 :\n'+'دلار 🇺🇸\n'+"--------------------------------------------------------------------"+'\n'+" قیمت سهام 🌋 :\n" + str(stock_price_global_fa) +' 💲\n'+"--------------------------------------------------------------------"+"\n"+" تغییر در 24 ساعت به دلار ⏳ :\n" +str(stock_change_usd_global_fa)+' 💲\n'+"--------------------------------------------------------------------"+'\n'+' تغییر در 24 ساعت به درصد ⏳ :\n'+str(stock_change_percent_global_fa)+" \n"+"--------------------------------------------------------------------"+"\n"+" حجم بازار 🏦 :\n"+str(market_cap)+"\n"+"--------------------------------------------------------------------"+'\nبزرگترین دارنده سهام بر حسب موسسه 🌐 :\n'+str(top_one_name).title()+'\n'+"--------------------------------------------------------------------"+'\n'+' تاریخ گزارش 📆 :\n'+str(top_one_shares_date_reported)+'\n'+'--------------------------------------------------------------------'+'\nمقدار سهام بزرگترین دارنده سهام 💠 :\n'+str(top_one_shares)+'\n'+'--------------------------------------------------------------------'+f"\nارزش سهام به دلار آمریکا 💰 :\n"+str(top_one_shares_usd_va)+'\n'+'--------------------------------------------------------------------'                                                                                                                                            
                
                global tg_message_to_send_sort_fa
                tg_message_to_send_sort_fa =market_status_time+"❗️"+"\n"+"--------------------------------------------------------------------"+'\n'+f" قیمت سهام {str(symbol_fa).upper()}🌋 :\n" + str(stock_price_global_fa) +' 💲\n'+"--------------------------------------------------------------------"+"\n"+" تغییر در 24 ساعت به دلار ⏳ :\n" +str(stock_change_usd_global_fa)+' 💲\n'+"--------------------------------------------------------------------"+'\n'+' تغییر در 24 ساعت به درصد ⏳ :\n'+str(stock_change_percent_global_fa)
                global tg_message_to_send_news_fa
                tg_message_to_send_news_fa = f'آخرین اخبار در مورد {comeny_name}❗️'+"\n"+"--------------------------------------------------------------------"+'\nنام خبرگزاری ✒️ :\n'.title()+str(last_news_agency)+"\n"+"-------------------------------------------------------------------"+'\nعنوان خبر 🗞 :\n'.title()+str(last_news_title)+'\n'+"-------------------------------------------------------------------"+'\n'
                tg_message_to_send_news_fa += f"<a href='{last_news_link}'>برای خواندن جزئیات کامل کلیک کنید 📰</a>"
                tg_message_to_send_news_fa += "\n"+"--------------------------------------------------------------------"

                button_bar = types.InlineKeyboardButton('📚برای دریافت اطلاعات بیشتر کلیک کنید📚'.title(), callback_data='click get more information for stock market fa')
                button_bar2 = types.InlineKeyboardButton('🗞برای دریافت آخرین اخبار کلیک کنید🗞'.title(), callback_data='click to get the latest news for stock market fa')
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(button_bar)
                keyboard.add(button_bar2)
                global message_for_edit_fa
                message_for_edit_fa = message
                bot.send_message(chat_id, tg_message_to_send_sort_fa, parse_mode = 'HTML', disable_web_page_preview=False, reply_markup=keyboard)
            except :
                problem ='مطمئن شوید که نماد نام شرکت را به درستی وارد کرده اید.'
                bot.reply_to(message,problem)



        elif str(message.text.replace(":"," ").split()[0 : -1]).replace("'",'').replace(",","").strip("[ ]")  == 'مخفف نام ارز دیجیتال':
            try :
                cryptocurrency_name = message.text.replace('مخفف نام ارز دیجیتال','')
                cryptocurrency_name = cryptocurrency_name.replace(":",'')
                symbol_crypto = (cryptocurrency_name).upper().replace(" ",'')
                crypto_currency_type_status = ''
                keyboard = types.InlineKeyboardMarkup()
                chat_id = message.chat.id
                try :
                    if  currency_type_fa != 'ایالات متحده(دلار)' and currency_type_fa != 'ایران(تومان)' :
                            
                            
                            currence_countery_price_to_usdt = curences_list_r_from_config_fa[currency_type_fa]
                            agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
                            headers = {'User-Agent': agent}
                            url = f'https://finance.yahoo.com/quote/{currence_countery_price_to_usdt}?p={currence_countery_price_to_usdt}'
                            response_price_to_usdt  = requests.get(url, headers=headers)
                            if response_price_to_usdt.status_code == 200 :
                                response_price_to_usdt = (response_price_to_usdt.text)
                                soup = BeautifulSoup( response_price_to_usdt , 'html.parser')
                                when_live_stock_changes_is_none = soup.find(class_ = "D(ib) Mend(20px)")
                                # FOR LIVE price
                                live_stock_changes = soup.find(class_ = "Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)")
                                when_live_stock_changes_is_none = soup.find(class_ = "D(ib) Mend(20px)")
                                # get live price
                                price = when_live_stock_changes_is_none.find( class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)" )
                                price = str(price).split()
                                price = price[-1].replace("</fin-streamer>",'')
                                price_index = price.index(">")
                                price = price[price_index : ].replace(">",'')
                                price=str(price).replace(',','')

                                currence_price_to_usdt = float(price)
                                currence_price_to_usdt = "%.2f" % currence_price_to_usdt
                                currence_price_to_usdt = float(currence_price_to_usdt)
                                crypto_currency_type_status = 'ok'
                            else : 
                                problem ='مشکل از سرورهای منبع است و ما در تلاش هستیم آن را برطرف کنیم.'
                    elif currency_type_fa == 'ایالات متحده(دلار)' or currency_type_fa == 'ایران(تومان)' : 
                            crypto_currency_type_status = 'ok'

                except:
                    chat_id = message.chat.id
                    markup = telebot.types.ReplyKeyboardMarkup(True,False)
                    markup.row('👇🏻با توجه به ارز مورد نظر خود👇🏻\nیکی از نه گزینه زیر را انتخاب کنید'.title())
                    markup.row('ایالات متحده(دلار)')
                    markup.row('ژاپن(ین)','انگلستان(پوند)'.upper())
                    markup.row('چین(یوان)','آلمان(یورو)')
                    markup.row('هند(روپیه)','کره جنوبی(وون)')
                    markup.row('ایران(تومان)','روسیه(روبل)')
                    markup.row('بازگشت به صفحه اصلی ↩️'.title(),'بازگشت به صفحه فهرست کلمات کلیدی 🔙'.title())
                    bot.send_message(chat_id,'لطفا ابتدا واحد پولی خود را انتخاب کنید تا قیمت ها را مطابق با آن ارز دریافت کنید .'.title(), reply_markup=markup)

                if crypto_currency_type_status == 'ok' : 
                    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
                    headers = {'User-Agent': agent}
                    url = f'https://finance.yahoo.com/quote/{symbol_crypto}-USD?p={symbol_crypto}-USD'
                    response = requests.get(url, headers=headers)
                    
                    response = (response.text)
                    
                    
                    soup = BeautifulSoup( response , 'html.parser')
                    # get live price
                    live_crypto_changes = soup.find(class_ = "D(ib) Mend(20px)")
                    # get live price
                    price_for_crypto = live_crypto_changes.find( class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)" )
                    price_for_crypto = str(price_for_crypto).split()
                    price_for_crypto = price_for_crypto[-1].replace("</fin-streamer>",'')
                    price_index = price_for_crypto.index(">")
                    price_for_crypto = price_for_crypto[price_index : ].replace(">",'')
                    cryptocurrency_price = str(price_for_crypto.replace(',',''))
                    # get change usd
                    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    color_status_fa = ("")

                    if "C($negativeColor)" in str(live_crypto_changes):
                            color_status_fa = color_status_fa = "C($negativeColor)"
                    elif "C($positiveColor)" in str(live_crypto_changes) :
                            color_status_fa = color_status_fa ="C($positiveColor)"
                    elif "C($negativeColor)" and  "C($positiveColor)" not in str(live_crypto_changes):
                            color_status_fa = color_status_fa =""
                            
                    crypto_changes = live_crypto_changes.find_all (class_ = color_status_fa )
                    change_usd = (str(crypto_changes[0]).replace(f"""<span class="{color_status_fa}">""",'').replace("</span>",'').strip("[ ]"))
                    cryptocurrency_change_usd = change_usd
                    # get change percent
                    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                    change_percent = (str(crypto_changes[1]).replace(f"""<span class="{color_status_fa}">""",'').replace("</span>",'').strip("( )"))
                    cryptocurrency_change_percent = change_percent
                    try : 
                        code_for_last_news_edit_for_all_types = ''
                        code_for_last_news_edit_just_text = (soup.find(class_="Ov(h) Pend(14%) Pend(44px)--sm1024"))
                        if str(code_for_last_news_edit_just_text).lower() == 'none':
                            code_for_last_news_edit_for_all_types = "Ov(h) Pend(44px) Pstart(25px)"
                        elif str(code_for_last_news_edit_just_text).lower() != 'none':
                            code_for_last_news_edit_for_all_types = "Ov(h) Pend(14%) Pend(44px)--sm1024"
                        
                        try :     
                            test = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="C(#959595) Fz(11px) D(ib) Mb(6px)")
                        except: 
                            code_for_last_news_edit_for_all_types = 'js-stream-content Pos(r)'


                        try :

                            last_news_agency = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="C(#959595) Fz(11px) D(ib) Mb(6px)")
                            last_news_agency = (str(last_news_agency).replace('<div class="C(#959595) Fz(11px) D(ib) Mb(6px)">','').replace("</div>",''))
                            
                            last_news_title = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="Mb(5px)")
                            last_news_title = (str(last_news_title).replace(">",' ').replace("<"," "))
                            last_news_title_index = (last_news_title.split().index('/u'))
                            last_news_title =  last_news_title.split()[last_news_title_index+1 : -2]
                            last_news_title = (str(last_news_title).replace("'","").replace(",",'').strip("[ ]")+".")


                            last_news_link = soup.find(class_=code_for_last_news_edit_for_all_types).find(class_="Mb(5px)").find(class_="js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled")
                            last_news_link_index = (str(last_news_link).replace("js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled",'').replace(">",' ').replace('"',' ').split().index("href="))
                            last_news_link = (str(last_news_link).replace("js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled",'').replace(">",' ').replace('"',' ').split()[last_news_link_index+1])
                            last_news_link = ("https://finance.yahoo.com"+last_news_link)
                        except:
                            last_news_title = 'N/A'  
                            last_news_agency = 'N/A'
                            last_news_link = 'N/A'
                    except : 
                        'ok'
                    try : 
                        info = info_crypto(str(symbol_crypto).replace(' ',''))
                        # info for crypto
                        market_cap_for_crypto = info['market_cap']
                        currency_site = info['site']
                        currency_name = info['name']

                    except : 
                        'ok'
                    if  currency_type_fa == 'ایران(تومان)' : 

                            try :
                                
                                
                                # nobitx status = no edit
                                response = requests.get(api_price_url+"USDTIRT")
                                response = response.json()
                                irt_to_usdt_price =  response['trades'][0]['price'] 
                                irt_to_usdt_price = str(irt_to_usdt_price).replace("'",'')
                                irt_to_usdt_price = str(irt_to_usdt_price).strip("( )").replace(",",'')
                                irt_to_usdt_price = irt_to_usdt_price.replace(""," ")
                                irt_to_usdt_price = irt_to_usdt_price.split()
                                irt_to_usdt_price.pop(-1)
                                irt_to_usdt_price = str(irt_to_usdt_price)
                                irt_to_usdt_price = irt_to_usdt_price.replace("'",'')
                                irt_to_usdt_price = irt_to_usdt_price.replace(",","")
                                irt_to_usdt_price = irt_to_usdt_price.strip("[ ]")
                                irt_to_usdt_price = irt_to_usdt_price.replace(" ",'')
                                cryptocurrency_price = float(cryptocurrency_price.replace(',','')) 
                                irt_to_usdt_price = float(irt_to_usdt_price)
                                change_irt_fi = float(cryptocurrency_change_usd.replace(',','')) * irt_to_usdt_price
                                crypto_price_irt = irt_to_usdt_price * cryptocurrency_price
                                
                                if int(float(str(crypto_price_irt).replace("-",''))) == 0 :
                                    crypto_price_irt = str(f'{(float(crypto_price_irt)):,}')
                                elif int(float(str(crypto_price_irt).replace("-",''))) > 0 :
                                    crypto_price_irt = "%.2f" % crypto_price_irt
                                    crypto_price_irt = str(f'{(float(crypto_price_irt)):,}')

                                if int(float(str(change_irt_fi).replace("-",''))) == 0 :
                                    change_irt_fi = str(f'{(float(change_irt_fi)):,}')
                                elif int(float(str(change_irt_fi).replace("-",''))) > 0 :
                                    change_irt_fi = "%.2f" % change_irt_fi
                                    change_irt_fi = str(f'{(float(change_irt_fi)):,}')
                                
                                
                                
                    
                                
                                global tg_message_to_send_sort_irt_fa
                                global tg_message_to_send_irt_fa
                                tg_message_to_send_irt_fa = '\nنام کامل ارز دیجیتال 🏢 :\n'.upper()
                                tg_message_to_send_irt_fa += f"<a href='{currency_site}'>{currency_name.upper()}</a>"
                                tg_message_to_send_irt_fa += "\n"+"--------------------------------------------------------------------"+'\nواحد پول 🪙 :\n'+'تومان\n'+"--------------------------------------------------------------------"+'\n'+" قیمت ارز دیجیتال 🌋 :\n".upper() +(crypto_price_irt)  +'\n'+"--------------------------------------------------------------------"+"\n"+" تغییر در 24 ساعت به تومان ⏳ :\n" + str(change_irt_fi)+' \n'+"--------------------------------------------------------------------"+'\n'+' تغییر در 24 ساعت به درصد ⏳ :\n'+str(cryptocurrency_change_percent)+" \n"+"--------------------------------------------------------------------"+"\n"+" حجم بازار 🏦 :\n"+str(market_cap_for_crypto)+'\n'+'--------------------------------------------------------------------'
                                
                                tg_message_to_send_sort_irt_fa = f" قیمت ارز دیجیتال {symbol_crypto} 🌋 :\n".upper() + str(crypto_price_irt) +'\n'+"--------------------------------------------------------------------"+"\n"+" تغییر در 24 ساعت به دلار ⏳ :\n" +str(change_irt_fi)+'\n'+"--------------------------------------------------------------------"+'\n'+' تغییر در 24 ساعت به درصد ⏳ :\n'+str(cryptocurrency_change_percent)
                            except : 
                                'ok'
                    elif  currency_type_fa == 'ایالات متحده(دلار)' :   
                            try:
                                
                                global tg_message_to_send_sort_usd_fa
                                global tg_message_to_send_usd_fa
                                tg_message_to_send_usd_fa = '\nنام کامل ارز دیجیتال 🏢 :\n'.upper()
                                tg_message_to_send_usd_fa += f"<a href='{currency_site}'>{currency_name.upper()}</a>"
                                tg_message_to_send_usd_fa += "\n"+"--------------------------------------------------------------------"+'\nواحد پول 🪙 :\n'+'دلار آمریکا\n'+"--------------------------------------------------------------------"+'\n'+" قیمت ارز دیجیتال 🌋 :\n".upper() + str(cryptocurrency_price) +' 💲\n'+"--------------------------------------------------------------------"+"\n"+" تغییر در 24 ساعت به تومان ⏳ :\n" +str(cryptocurrency_change_usd)+' 💲\n'+"--------------------------------------------------------------------"+'\n'+' تغییر در 24 ساعت به درصد ⏳ :\n'+str(cryptocurrency_change_percent)+" \n"+"--------------------------------------------------------------------"+"\n"+" حجم بازار 🏦 :\n"+str(market_cap_for_crypto)+"\n"+"--------------------------------------------------------------------"
                                
                                tg_message_to_send_sort_usd_fa =f" قیمت ارز دیجیتال {symbol_crypto} 🌋 :\n".upper() + str(cryptocurrency_price) +' 💲\n'+"--------------------------------------------------------------------"+"\n"+" تغییر در 24 ساعت به دلار ⏳ :\n" +str(cryptocurrency_change_usd)+' 💲\n'+"--------------------------------------------------------------------"+'\n'+' تغییر در 24 ساعت به درصد ⏳ :\n'+str(cryptocurrency_change_percent)
                            except : 
                                'ok'
                    elif currency_type_fa != 'ایران(تومان)' and currency_type_fa != 'ایالات متحده(دلار)' : 
                            try:
                                global tg_message_to_send_sort_glob_fa
                                global tg_message_to_send_glob_fa
                                cryptocurrency_price = float(cryptocurrency_price.replace(',','')) * currence_price_to_usdt 
                                if int(float(str(cryptocurrency_price).replace("-",''))) == 0 :
                                    cryptocurrency_price = str(f'{(float(cryptocurrency_price)):,}')
                                elif int(float(str(cryptocurrency_price).replace("-",''))) > 0 :
                                    cryptocurrency_price = "%.2f" % cryptocurrency_price
                                    cryptocurrency_price = str(f'{(float(cryptocurrency_price)):,}')

                                cryptocurrency_change_usd = float(cryptocurrency_change_usd.replace(',','')) * currence_price_to_usdt
                                if int(float(str(cryptocurrency_change_usd).replace("-",''))) == 0 :
                                    cryptocurrency_change_usd = str(f'{(float(cryptocurrency_change_usd)):,}')
                                
                                elif int(float(str(cryptocurrency_change_usd).replace("-",''))) > 0 :
                                    cryptocurrency_change_usd = "%.2f" % cryptocurrency_change_usd
                                    cryptocurrency_change_usd = str(f'{(float(cryptocurrency_change_usd)):,}')



                                tg_message_to_send_glob_fa = '\nنام کامل ارز دیجیتال 🏢 :\n'.upper()
                                tg_message_to_send_glob_fa += f"<a href='{currency_site}'>{currency_name.upper()}</a>"
                                tg_message_to_send_glob_fa += "\n"+"--------------------------------------------------------------------"+'\nواحد پول 🪙 :\n'+f'{curences_list_from_config_fa[currency_type_fa]}\n'+"--------------------------------------------------------------------"+'\n'+"قیمت ارز دیجیتال 🌋 :\n".upper() + str(cryptocurrency_price) +'\n'+"--------------------------------------------------------------------"+"\n"+"تغییر در 24 ساعت ⏳ :\n" +str(cryptocurrency_change_usd)+'\n'+"--------------------------------------------------------------------"+'\n'+'تغییر در 24 ساعت به درصد ⏳ :\n'+str(cryptocurrency_change_percent)+" \n"+"--------------------------------------------------------------------"+"\n"+" حجم بازار 🏦 :\n"+str(market_cap_for_crypto)+"\n"+"--------------------------------------------------------------------"
                                
                                tg_message_to_send_sort_glob_fa =f"قیمت ارز دیجیتال {symbol_crypto} 🌋 :\n".upper() + str(cryptocurrency_price) +'\n'+"--------------------------------------------------------------------"+"\n"+f" تغییر در 24 ساعت به {curences_list_from_config_fa[currency_type_fa]} ⏳ :\n" +str(cryptocurrency_change_usd)+'\n'+"--------------------------------------------------------------------"+'\n'+'تغییر در 24 ساعت به درصد ⏳ :\n'+str(cryptocurrency_change_percent)
                            except : 
                                'ok'




                    global tg_message_to_send_news_crypto_fa
                    tg_message_to_send_news_crypto_fa = f'آخرین اخبار در مورد {currency_name}❗️'+"\n"+"--------------------------------------------------------------------"+'\nنام خبرگزاری ✒️ :\n'.title()+str(last_news_agency)+"\n"+"-------------------------------------------------------------------"+'\nعنوان خبر 🗞 :\n'.title()+str(last_news_title)+'\n'+"-------------------------------------------------------------------"+'\n'
                    tg_message_to_send_news_crypto_fa +=  f"<a href='{last_news_link}'>برای خواندن جزئیات کامل کلیک کنید 📰</a>"
                    tg_message_to_send_news_crypto_fa += "\n"+"--------------------------------------------------------------------"
                    chat_id = message.chat.id
                    button_bar = types.InlineKeyboardButton('📚برای دریافت اطلاعات بیشتر کلیک کنید📚'.title(), callback_data='click get more information for crypto currency market fa')
                    button_bar2 = types.InlineKeyboardButton('🗞برای دریافت آخرین اخبار کلیک کنید🗞'.title(), callback_data='click to get the latest news for crypto currency market fa')
                    keyboard = types.InlineKeyboardMarkup()
                    keyboard.add(button_bar)
                    keyboard.add(button_bar2)
                    message_for_edit_fa = message
                    if currency_type_fa == 'ایران(تومان)' : 
                        bot.send_message(chat_id, tg_message_to_send_sort_irt_fa, parse_mode = 'HTML', disable_web_page_preview=False, reply_markup=keyboard)
                    elif currency_type_fa == 'ایالات متحده(دلار)' :
                        bot.send_message(chat_id, tg_message_to_send_sort_usd_fa, parse_mode = 'HTML', disable_web_page_preview=False, reply_markup=keyboard)
                    elif currency_type_fa != 'ایالات متحده(دلار)' and currency_type_fa != 'ایران(تومان)' :
                        bot.send_message(chat_id, tg_message_to_send_sort_glob_fa, parse_mode = 'HTML', disable_web_page_preview=False, reply_markup=keyboard)


            except :
                    problem ='مطمئن شوید که نماد ارز دیجیتال را به درستی وارد کرده اید.'
                    bot.reply_to(message,problem)
            
        elif message.text == "برای دریافت قیمت تتر/تومان اینجا را کلیک کنید" : 
            try :
                response = requests.get(api_price_url+"USDTIRT")
                response = response.json()
                irt_to_usdt_price =  response['trades'][0]['price'] 
                irt_to_usdt_price = str(irt_to_usdt_price).replace("'",'')
                irt_to_usdt_price = str(irt_to_usdt_price).strip("( )").replace(",",'')
                irt_to_usdt_price = irt_to_usdt_price.replace(""," ")
                irt_to_usdt_price = irt_to_usdt_price.split()
                irt_to_usdt_price.pop(-1)
                irt_to_usdt_price = str(irt_to_usdt_price)
                irt_to_usdt_price = irt_to_usdt_price.replace("'",'')
                irt_to_usdt_price = irt_to_usdt_price.replace(",","")
                irt_to_usdt_price = irt_to_usdt_price.strip("[ ]")
                irt_to_usdt_price = irt_to_usdt_price.replace(" ",'')
                bot.reply_to(message,"قیمت تتر/تومان : "+str(f'{(int(irt_to_usdt_price)):,}')+" تومان")
            except : 
                problem ='مشکل از سرورهای منبع است و ما در تلاش هستیم آن را برطرف کنیم 🛠.'
                bot.reply_to(message,problem)

        elif "برای دریافت قیمت تتر" in message.text.replace("/",' '): 
            try:
                if currency_type_fa == currency_type_fa :
                    if message.text == f"برای دریافت قیمت تتر/{curences_list_from_config_fa[currency_type_fa].lower()} اینجا را کلیک کنید" and currency_type_fa != 'iran(irt)':
                        currence_countery_price_to_usdt = curences_list_r_from_config_fa[currency_type_fa]
                        agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
                        headers = {'User-Agent': agent}
                        url = f'https://finance.yahoo.com/quote/{currence_countery_price_to_usdt}?p={currence_countery_price_to_usdt}'
                        response_price_to_usdt  = requests.get(url, headers=headers)
                        if response_price_to_usdt.status_code == 200 :
                            response_price_to_usdt = (response_price_to_usdt.text)
                            soup = BeautifulSoup( response_price_to_usdt , 'html.parser')
                            when_live_stock_changes_is_none = soup.find(class_ = "D(ib) Mend(20px)")
                            # FOR LIVE price
                            live_stock_changes = soup.find(class_ = "Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)")
                            when_live_stock_changes_is_none = soup.find(class_ = "D(ib) Mend(20px)")
                            # get live price
                            price = when_live_stock_changes_is_none.find( class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)" )
                            price = str(price).split()
                            price = price[-1].replace("</fin-streamer>",'')
                            price_index = price.index(">")
                            price = price[price_index : ].replace(">",'')
                            price=str(price).replace(',','')

                            currence_price_to_usdt = float(price)
                            currence_price_to_usdt = "%.2f" % currence_price_to_usdt
                            bot.reply_to(message,f"قیمت تتر/{curences_list_from_config_fa[currency_type_fa]}  : "+str(f'{(float(currence_price_to_usdt)):,}'))
                        else:
                            problem ='مشکل از سرورهای منبع است و ما در تلاش هستیم آن را برطرف کنیم 🛠.'
                            bot.reply_to(message,problem)




            except:
                    chat_id = message.chat.id
                    markup = telebot.types.ReplyKeyboardMarkup(True,False)
                    markup.row('👇🏻با توجه به ارز مورد نظر خود👇🏻\nیکی از نه گزینه زیر را انتخاب کنید'.title())
                    markup.row('ایالات متحده(دلار)')
                    markup.row('ژاپن(ین)','انگلستان(پوند)'.upper())
                    markup.row('چین(یوان)','آلمان(یورو)')
                    markup.row('هند(روپیه)','کره جنوبی(وون)')
                    markup.row('ایران(تومان)','روسیه(روبل)')
                    markup.row('بازگشت به صفحه اصلی ↩️'.title(),'بازگشت به صفحه فهرست کلمات کلیدی 🔙'.title())
                    bot.send_message(chat_id,'لطفا ابتدا واحد پولی خود را انتخاب کنید .'.title(), reply_markup=markup)
    



@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
        chat_id = call.message.chat.id
        
        if (call.data==("click get more information for stock market")):
            try:
                bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="successful ✅\nCheck the message you received".title() )
                bot.send_message(chat_id, tg_message_to_send, parse_mode = 'HTML', disable_web_page_preview=False)
            except:
                bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="not successful ❌".title() )

# click get more information for crypto currency market

        elif(call.data==("click to get the latest news for stock market")):   
            try :
                bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="successful ✅\nCheck the message you received".title() )
                bot.send_message(chat_id, tg_message_to_send_news, parse_mode = 'HTML', disable_web_page_preview=False)
            except:
                bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="not successful ❌".title() )
        # for crypto calls
        
        elif(call.data==("click get more information for crypto currency market")):   
            try :
                bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="successful ✅\nCheck the message you received".title() )
                if currency_type == 'iran(irt)' :
                    bot.send_message(chat_id, tg_message_to_send_irt, parse_mode = 'HTML', disable_web_page_preview=False)
                elif currency_type == 'united states(usd)':
                    bot.send_message(chat_id, tg_message_to_send_usd, parse_mode = 'HTML', disable_web_page_preview=False)
                elif currency_type != 'iran(irt)' and currency_type != 'united states(usd)' : 
                    bot.send_message(chat_id, tg_message_to_send_glob, parse_mode = 'HTML', disable_web_page_preview=False)

                   
            except:
                bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="not successful ❌".title() )
        
        elif(call.data==("click to get the latest news for crypto currency market")):   
                    try :
                        bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="successful ✅\nCheck the message you received".title() )
                        bot.send_message(chat_id, tg_message_to_send_news_crypto, parse_mode = 'HTML', disable_web_page_preview=False)
                    except:
                        bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="not successful ❌".title() )

        elif (call.data == ("click get more information for stock market fa")):
            try:
                bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="موفقیت آمیز ✅\nپیامی که دریافت کردید را بررسی کنید".title() )
                bot.send_message(chat_id, tg_message_to_send_fa, parse_mode = 'HTML', disable_web_page_preview=False)
            except:
                bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="موفقیت آمیز نبود ❌".title() )

        # click get more information for crypto currency market

        elif(call.data == ("click to get the latest news for stock market fa")):   
            try :
                bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="موفقیت آمیز ✅\nپیامی که دریافت کردید را بررسی کنید".title() )
                bot.send_message(chat_id, tg_message_to_send_news_fa, parse_mode = 'HTML', disable_web_page_preview=False)
            except:
                bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="موفقیت آمیز نبود ❌".title() )
        # for crypto calls
        
        elif(call.data==("click get more information for crypto currency market fa")):   
            try :
                bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="موفقیت آمیز ✅\nپیامی که دریافت کردید را بررسی کنید".title() )
                if currency_type_fa == 'ایران(تومان)' :
                    bot.send_message(chat_id, tg_message_to_send_irt_fa, parse_mode = 'HTML', disable_web_page_preview=False)
                elif currency_type_fa == 'ایالات متحده(دلار)':
                    bot.send_message(chat_id, tg_message_to_send_usd_fa, parse_mode = 'HTML', disable_web_page_preview=False)
                elif currency_type_fa != 'ایران(تومان)' and currency_type_fa != 'ایالات متحده(دلار)' : 
                    bot.send_message(chat_id, tg_message_to_send_glob_fa, parse_mode = 'HTML', disable_web_page_preview=False)

                   
            except:
                bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="موفقیت آمیز نبود ❌".title() )
        
        elif(call.data==("click to get the latest news for crypto currency market fa")):   
                    try :
                        bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="موفقیت آمیز ✅\nپیامی که دریافت کردید را بررسی کنید".title() )
                        bot.send_message(chat_id, tg_message_to_send_news_crypto_fa, parse_mode = 'HTML', disable_web_page_preview=False)
                    except:
                        bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text="موفقیت آمیز نبود ❌".title() )





          
           



bot.infinity_polling()

