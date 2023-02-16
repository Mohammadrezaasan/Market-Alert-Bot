Bot_Token = "Token" 
'------------------------------------------------------------------------------------------------------------------------------------'
RapidAPI_Key = "Token"
'----------------------------------------------------------------------------------------------------------------------------------'
crypto_info = {
    'what is cryptocurrency? 🤔' :'What Is Cryptocurrency?\ncryptocurrency is a digital or virtual currency that is secured by cryptography, which makes it nearly impossible to counterfeit or double-spend. Many cryptocurrencies are decentralized networks based on blockchain technology—a distributed ledger enforced by a disparate network of computers. A defining feature of cryptocurrencies is that they are generally not issued by any central authority, rendering them theoretically immune to government interference or manipulation.',
    'how does cryptocurrency work? 🤯' :'How does cryptocurrency work?\nCryptocurrencies run on a distributed public ledger called blockchain, a record of all transactions updated and held by currency holders.Units of cryptocurrency are created through a process called mining, which involves using computer power to solve complicated mathematical problems that generate coins. Users can also buy the currencies from brokers, then store and spend them using cryptographic wallets.If you own cryptocurrency, you don’t own anything tangible. What you own is a key that allows you to move a record or a unit of measure from one person to another without a trusted third party.Although Bitcoin has been around since 2009, cryptocurrencies and applications of blockchain technology are still emerging in financial terms, and more uses are expected in the future. Transactions including bonds, stocks, and other financial assets could eventually be traded using the technology.',
    'how to buBot_Token = "TOKEN" 

'------------------------------------------------------------------------------------------------------------------------------------'
crypto_info = {
    'what is cryptocurrency? 🤔' :'What Is Cryptocurrency?\ncryptocurrency is a digital or virtual currency that is secured by cryptography, which makes it nearly impossible to counterfeit or double-spend. Many cryptocurrencies are decentralized networks based on blockchain technology—a distributed ledger enforced by a disparate network of computers. A defining feature of cryptocurrencies is that they are generally not issued by any central authority, rendering them theoretically immune to government interference or manipulation.',
    'how does cryptocurrency work? 🤯' :'How does cryptocurrency work?\nCryptocurrencies run on a distributed public ledger called blockchain, a record of all transactions updated and held by currency holders.Units of cryptocurrency are created through a process called mining, which involves using computer power to solve complicated mathematical problems that generate coins. Users can also buy the currencies from brokers, then store and spend them using cryptographic wallets.If you own cryptocurrency, you don’t own anything tangible. What you own is a key that allows you to move a record or a unit of measure from one person to another without a trusted third party.Although Bitcoin has been around since 2009, cryptocurrencies and applications of blockchain technology are still emerging in financial terms, and more uses are expected in the future. Transactions including bonds, stocks, and other financial assets could eventually be traded using the technology.',
    'how to buy cryptocurrency? 😎' : 'How to buy cryptocurrency?\n1- Do thorough research on crypto to better understand crypto.\n2- Choose a reliable exchange where you can buy cryptocurrencies.\n3- After choosing an exchange and creating an account in it, you can deposit the amount of money you want to invest in cryptocurrencies into your account.\n4- To invest in currencies, be sure to do a thorough research on the currency you want to invest in.\n5- And finally, to store your currencies, you can use the digital wallet that you have in your exchange account or use different digital wallets that you install as an application on your device(before using the wallet do enough research on it).',
}

'------------------------------------------------------------------------------------------------------------------------------------'
Bot_Info = {
    '🤖 introducing the robot 🤖': "Hello, my name is Live Information Bot 🤖\nI can tell you the stock prices of international companies and in addition to stocks, I can also tell you the prices of cryptocurrencies and when you get their prices, you can click on the (latest news) button to get the latest news about that company or cryptocurrency.\n And I can check if the crypto transactions you made were successful.".title(),
    '🗂 if you need more information 🗂 \n📨 contact us 📨': '📧 Email : \nLive_Information_Bot@Live_Information.co',   
}
'------------------------------------------------------------------------------------------------------------------------------------'
bot_kaywords = ("📊 mtock market price 📊\nWith the help of this key and the instructions that have been explained, you can get the stock price of your favorite company live\n--------------------------------------------------------------------\n💵 Cryptocurrency price 💵\nWith the help of this key and the instructions explained, you can get the price of your favorite cryptocurrency live.\n--------------------------------------------------------------------\n📒 List of information 📒\nA list of questions has been prepared for those who need more information, By clicking on the desired question, you will receive the answer to that question.\n--------------------------------------------------------------------\n👨🏻‍💻 Tx_Hash Check 👨🏻‍💻\nThis key will help you to check if the transaction you made was successful or not. It is designed for two types of networks,{TRON(TRC20),Ethereum(ERC20)}.\n--------------------------------------------------------------------")
     
'------------------------------------------------------------------------------------------------------------------------------------'

curences_list_from_config = {

    'england(gbp)':'GBP=X',
    'germany(eur)':'EUR=X',
    'united states(usd)':'USD',
    'south korea(krw)':'KRW=X',
    'japan(jpy)':'JPY=X',
    'china(cnh)':'CNH=X',
    'india(inr)':'INR=X',
    'russia(rub)':'RUB=X',
    'iran(irt)' : 'IRT'

}


def info_crypto(crypto_name) :

    import requests
    from bs4 import BeautifulSoup 
    symbol = (crypto_name+'-usd').upper()

    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
    headers = {'User-Agent': agent}
    try :
        url = f'https://finance.yahoo.com/quote/{symbol}/profile?p={symbol}'
        response = requests.get(url, headers=headers)
        response = (response.text)
        soup = BeautifulSoup( response , 'html.parser')
    except :
        d =''
    
    try :
        dis = soup.find(class_ ='Pb(30px) smartphone_Px(20px)').find_all("div", string=True)
        dis = str(dis[0]).replace('<div data-test="prof-desc">','').replace('</div>','')
    except :
        d = ''
    
    site = dis.split()[-1]
    site = site.replace('/.','')

    name = dis.split()[0]
    try :
        url2 = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}'
        response2 = requests.get(url2, headers=headers)
        response2 = (response2.text)
        soup2 = BeautifulSoup( response2 , 'html.parser')
    except :
        d =''
    try : 
        market_cap = str(soup2.find(class_='D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)').find(class_='Ta(end) Fw(600) Lh(14px)'))
        market_cap = market_cap.replace('<td class="Ta(end) Fw(600) Lh(14px)" data-test="MARKET_CAP-value">','').replace('</td>','')
    except :
        d = ''
    info = {'site' : site , 'name' : name , 'market_cap' : market_cap + ' USD'} 

    try:
        return info
    except:
        d = ''



def info_stock(stock_name) :
    import requests
    from bs4 import BeautifulSoup 
    symbol = (stock_name).upper()

    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
    headers = {'User-Agent': agent}
    try :
        url = f'https://finance.yahoo.com/quote/{symbol}/profile?p={symbol}'
        response = requests.get(url, headers=headers)
        response = (response.text)
        soup = BeautifulSoup( response , 'html.parser')
    except :
        d =''
    
    dis = soup.find(class_ = 'asset-profile-container')

    name = str(dis.find(class_='Fz(m) Mb(10px)')).replace('<h3 class="Fz(m) Mb(10px)">','').replace('.</h3>','')

    site = str(dis.find(class_='D(ib) W(47.727%) Pend(40px)').find_all(class_='C($linkColor)')[1]).replace('<a class="C($linkColor)" href="','').split('"')[0]
    
    country = str(dis.find(class_ ='D(ib) W(47.727%) Pend(40px)')).split('<br/><a class="C($linkColor)"')[0].split('<br/>')[-1]

    try :
        url2 = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}'
        response2 = requests.get(url2, headers=headers)
        response2 = (response2.text)
        soup2 = BeautifulSoup( response2 , 'html.parser')
    except :
        d =''
    try : 
        market_cap = str(soup2.find(class_='D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)').find(class_='Ta(end) Fw(600) Lh(14px)'))
        market_cap = market_cap.replace('<td class="Ta(end) Fw(600) Lh(14px)" data-test="MARKET_CAP-value">','').replace('</td>','')
    except :
        d = ''
    info = {'site' : site , 'name' : name , 'market_cap' : market_cap +' USD','country' : country} 

    try  :
        return info

    except :
        d = ''


y cryptocurrency? 😎' : 'How to buy cryptocurrency?\n1- Do thorough research on crypto to better understand crypto.\n2- Choose a reliable exchange where you can buy cryptocurrencies.\n3- After choosing an exchange and creating an account in it, you can deposit the amount of money you want to invest in cryptocurrencies into your account.\n4- To invest in currencies, be sure to do a thorough research on the currency you want to invest in.\n5- And finally, to store your currencies, you can use the digital wallet that you have in your exchange account or use different digital wallets that you install as an application on your device(before using the wallet do enough research on it).',
    'how to donate? 🤑' : 'How to donate?\n1- Select your desired currency, for example (BTC).\n2- Enter the wallet address to which you want to deposit.\n3- Make sure that the currency network, for example (TRC 20), is similar to the currency network you want to deposit.\n4- Finally, choose the amount of currency you want to deposit and complete the confirmation process.'
}
'------------------------------------------------------------------------------------------------------------------------------------'
Addresses = {
    'donation btc(btc)💸' :"🔴 Address :\nbc1qwsnghp2nmqytejnf0xv2tlse5hfg3uzpal3868",
    'donation eth(eth)💸' :"🔴 Address :\n0x7B075A1c07e05d3542c13e56A61b63Da91125171",
    'donation bnb(bnb)💸' :"🔴 Address :\nbnb16m655nnxxj8vdv08tj74u3v7uazkspqyjnam5r",
    'donation xrp(xrp)\n💸' :"🔴 Address :\nrnqe3zNxe8nkJhDQNyBBnGmVJw7NVmi2dB",
    'donation busd(eth)\n💸' :"🔴 Address :\n0x7B075A1c07e05d3542c13e56A61b63Da91125171",
    'donation usdt(eth)\n💸' :"🔴 Address :\n0x7B075A1c07e05d3542c13e56A61b63Da91125171",
    'donation usdc(matic)\n💸' :"🔴 Address :\n0x7B075A1c07e05d3542c13e56A61b63Da91125171"
    }
photos ={
    'donation btc(btc)💸' : open("donation_photos\\btc.jpg",'rb'),
    'donation ETH(ETH)💸' : open("donation_photos\\eth.jpg",'rb'),
    'donation bnb(bnb)💸' : open("donation_photos\\bnb.jpg",'rb'),
    'donation xrp(xrp)\n💸' : open("donation_photos\\xrp.jpg",'rb'),
    'donation busd(eth)\n💸' : open("donation_photos\\busd.jpg",'rb'),
    'donation usdt(eth)\n💸' : open("donation_photos\\usdt-eth network.jpg",'rb'),
    'donation usdc(matic)\n💸' : open("donation_photos\\usdc.jpg",'rb')
    }
'------------------------------------------------------------------------------------------------------------------------------------'
Bot_Info = {
    '🤖 introducing the robot 🤖': "Hello, my name is market alert bot 🤖\nI can tell you the current price of major currencies in the crypto market with just a few simple clicks 🚀\nAnd I can also check with the transaction hash whether your transfer was successful  ✅or not❌. Just a few simple clicks and enter your transaction hash, that's it.\nAnd you can use the information list 📒 to find the right answer to your questions\nAnd if you don't find your answer in that list, you can contact us 📬with just one click 🖱",
    '🗂 if you need more information 🗂 \n📨 contact us 📨': '🟢 WhatsApp : +989906678506\n🔵 Telegram : @marketalertbotsupport\n📧 Email : cryptoandstockmarketalert@gmail.com',
}
'------------------------------------------------------------------------------------------------------------------------------------'



