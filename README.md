![IMG_4957](https://user-images.githubusercontent.com/108104864/188712566-e1a1c0c5-72a5-4d19-b47e-3343d9755ad5.jpg)



## <p align="center">A simple and convenient robot that tells you the weather with a few clicks <a href="https://t.me/tester_mohammadreza_asan1_bot">Weather Info Bot</a>.</p>

## <p align="center">Bot API Source : <a href="https://www.weatherapi.com/">Weather Api</a>

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
bot = telebot.TeleBot(Token_bot)
```
 ## Next step
 * To get the information you need, you must apply to the source site to receive the information you need after the request { Currently, I am using the prepared and edited source of <a href="https://rapidapi.com/weatherapi/api/weatherapi-com/">Rapid Api</a> site because you waste less time and it makes your work faster. }
 ```
 url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
```
  
## Codes docs



* The following code is related to the beginning part
```
@bot.message_handler(commands=['start']) # Here we set the message handler = start { For when message handler = start, the function does the following }
def handle_start(message): 
   chat_id = message.chat.id 
   text="`"+"The name of the desired city : "+"`" # Here we used the Telegram feature for text format { With this method, the user just clicks on the text and copies it to her clipboard, making the user's work faster. }
   markup = telebot.types.ReplyKeyboardMarkup(True, False) # In this section, we prepare a variable for the buttons, which will send the text inside the button only by clicking on it.
   markup.row("🔴 First, enter the name of your desired city as in the example below 🔴")
   markup.row('The name of the desired city : London')
   bot.send_message(chat_id,'Hello 🙋🏻‍♂️\nwelcome to the Weather Info Bot 👾 '+'\n🔴🔴 IMPORTANT 🔴🔴\nTo enter the name of your desired city, click on the text below and add the name of your desired city to the end of the text.',reply_markup=markup) # In this section, you enter the desired texts, which will be sent as text along with the button page
   bot.send_message(chat_id,text,parse_mode='MarkdownV2')
```
 
 * The code below is for the important part after the start part
 ```
 @bot.message_handler(content_types=['text']) # We put the message handler = content_types=['text'] here { If the user enters any text, our function will be activated and after activation, it will check the conditions that we have written in the form of try, if, and elif inside that function to see if the text entered by the user matches our conditions. or not? , if it matches, it fulfills that condition. }
def handle_text(message):
    message.text = message.text.lower() # In this section, we convert all the messages entered by the user into lowercase letters so that they don't have problems, and we write our codes according to the standard.
 ```
 * The following code is used to get the city name from the user 
 ```
     if  'the name of the desired city' in message.text :
        try:

            global city_name
            city_name = message.text.replace('the name of the desired city','')
            city_name =  city_name.replace(":","") # In this section, using the city name variable, we set the city name entered by the user = city name variable.
            city_name_test = city_name.replace(" ","")
            city_name_test = city_name_test[0] , city_name_test[1]
            if city_name_test[0]  not in Alphabet : # In this section, we check that the first two letters of the city name match the English alphabet and that the city name is not smaller than two letters.
                bot.reply_to(message,"The city name was not registered successfully ❌")
           
            elif city_name_test[1] not in Alphabet : 
                bot.reply_to(message,"The city name was not registered successfully ❌")

            elif city_name_test[0] in Alphabet : # In this section, we also check that if the first letter of the city name is in the English alphabet, save the city name and go to the next step.
                chat_id = message.chat.id 
                markup = telebot.types.ReplyKeyboardMarkup(True, False)
                markup.row("🤖 Introducing The Robot 🤖")
                markup.row('🗝 click here to find out what each keyword does 🗝')
                markup.row('📓 click here to open the list of keywords for you 📓')
                markup.row('🔄 Changing the name of the city 🔄')
                bot.send_message(chat_id,"The city name was successfully registered ✅\nCity Name :"+city_name.title(),reply_markup=markup)
        except: 
            bot.reply_to(message,"The city name was not registered successfully ❌")
 ```
 
 * The following code is used to get the current weather condition 
 ```
 elif message.text == "🌦 click here to get current weather conditions 🌦" :
        try :
            querystring = {"q":city_name,"days":"3"} # In this section, the city name was entered by the user in the city name field, we saved it as a value in the city name variable and placed it as the city name.

            headers = {
	     "X-RapidAPI-Key": RapidAPI_Key,
	     "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
         }

            response = requests.request("GET", url, headers=headers, params=querystring)

            information_received = json.loads(response.text) # And in this part, we sort the information we obtained after the request with the help of json
            current = information_received["current"]
            location = information_received["location"]
            condition = current['condition']
    
            # In this section, we edit the information we have obtained  
            bot.reply_to(message,'Country Name 🌎 : '+location['country']+'\nRegion 🗺 : '+location['region']+'\nCity Name 🏙 : '+location['name']+"\n------------------------------------------------------"+'\nLocal Time ⌚️ : '+location['localtime'].split()[1]+'\nCalendar 🗓 : '+location['localtime'].split()[0]+'\nLatest update on local time ⌚️ : '+current['last_updated'].split()[1]+"\nIt’s "+condition['text']+' Now'+sticker[condition['text']]+'\nTemperature 🌡 : '+str(current['temp_c'])+'°C'+'\nFeels Like 🚻 : '+str(current['feelslike_c'])+'°C'+'\nTemperature 🌡 : '+str(current['temp_f'])+'°F'+'\nFeels Like 🚻 : '+str(current['feelslike_f'])+'°F'+'\nWind Speed According To The Latest Update 🌬 : '+str(current['wind_kph'])+'KPH'+'\nWind Speed According To The Latest Update 🌬 : '+str(current['wind_mph'])+'MPH'+'\nWind Direction 🧭 : '+str(current['wind_dir'])+'\nPressure In Inches 🛫 : '+str(current['pressure_in'])+'\nPrecipitation Amount 🌧 : '+str(current['precip_mm'])+'MM'+'\nPrecipitation Amount 🌧 : '+str(current['precip_in'])+' Inches'+'\nHumidity💧: '+str(current['humidity'])+'%'+'\nCloud Cover ☁️ : '+str(current['cloud'])+'%'+'\nVisibility 🛣 : '+str(current['vis_km'])+'KM'+'\nVisibility 🛣 : '+str(current['vis_miles'])+'MPH'+'\nUV ☀️🕶 : '+str(current['uv']))                                                                                                                                                                
        except : 
            bot.reply_to(message,'🔴🔴 Make sure the city name you entered is correct 🔴🔴')
   
 ```
* The following code is used to get the local time and date of the location you entered
```
 elif message.text == '⌚️🌎 click here to get the local time of your desired location ⌚️🌎' :  
        try :
    
            querystring = {"q":city_name,"days":"3"}

            headers = {
         "X-RapidAPI-Key": RapidAPI_Key,
         "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
         }

            response = requests.request("GET", url, headers=headers, params=querystring)

            information_received = json.loads(response.text)
            current = information_received["current"]
            location = information_received["location"]
            condition = current['condition']
        
                

            bot.reply_to(message,'Country Name 🌎 : '+location['country']+'\nRegion 🗺 : '+location['region']+'\nCity Name 🏙 : '+location['name']+"\nLocal Time ⌚️ : "+location['localtime'].split()[1]+'\nCalendar 🗓 : '+location['localtime'].split()[0]+"\nIt’s "+condition['text']+' Now'+sticker[condition['text']])
        except : 
            bot.reply_to(message,'🔴🔴 Make sure the city name you entered is correct 🔴🔴')

 ```
 * The following code is used to get the daily forecast
 ```
 elif message.text in select_day_for_daily_forecast : # In this section, we want to use the variables that we created in the config file { Here we use the keywords that we have prepared and the user enters them to determine the forecast day and we translate them using the dictionary method }
        global answer_choose_the_day_of_the_daily_forecast 
        answer_choose_the_day_of_the_daily_forecast = message.text 
        try :
            querystring = {"q":city_name,"days":"3"}

            headers = {
         "X-RapidAPI-Key": RapidAPI_Key,
         "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

            response = requests.request("GET", url, headers=headers, params=querystring)

            information_received = json.loads(response.text)
            location = information_received["location"]
            forecast = information_received['forecast']["forecastday"][select_day_for_daily_forecast[answer_choose_the_day_of_the_daily_forecast]]['day']
            condition = forecast['condition']
            date1 = information_received['forecast']["forecastday"][select_day_for_daily_forecast[answer_choose_the_day_of_the_daily_forecast]]
                        

            bot.reply_to(message,'Country Name 🌎 : '+location['country']+'\nRegion 🗺 : '+location['region']+'\nCity Name 🏙 : '+location['name']+"\n------------------------------------------------------"+'\nForecast Date 🗓 : '+str(date1['date'])+'\n'+condition['text']+' '+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+' '+sticker[condition['text']]+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Maximum Temperature 🌡 : "+str(forecast['maxtemp_c'])+'°C'+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Minimum Temperature 🌡 : "+str(forecast['mintemp_c'])+'°C'+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Average Temperature 🌡 : "+str(forecast['avgtemp_c'])+"°C"+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Maximum Temperature 🌡 : "+str(forecast['maxtemp_f'])+'°F'+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Minimum Temperature 🌡 : "+str(forecast['mintemp_f'])+'°F'+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Average Temperature 🌡 : "+str(forecast['avgtemp_f'])+'°F'+'\nMaximum Wind Speed 🌬 : '+str(forecast['maxwind_kph'])+'KPH'+'\nMaximum Wind Speed 🌬 : '+str(forecast['maxwind_mph'])+'MPH'+'\nAverage Visibility 🛣 : '+str(forecast['avgvis_km'])+'KM'+'\nAverage Visibility 🛣 : '+str(forecast['avgvis_miles'])+'MPH'+'\nAverage Humidity 💧 : '+str(forecast['avghumidity'])+'%'+"\nWill It Rain "+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+' 🌧 : '+yes_or_no[str(forecast["daily_will_it_rain"])]+'\nChance Of Rain '+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+' 🌧 : '+str(forecast['daily_chance_of_rain'])+'%'+"\nWill It Snow "+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+' 🌨 : '+yes_or_no[str(forecast["daily_will_it_snow"])]+'\nChance Of Snow '+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+' 🌨 : '+str(forecast['daily_chance_of_snow'])+'%'+'\nTotal Precipitation 🌧 : '+str(forecast['totalprecip_mm'])+'MM'+'\nTotal Precipitation 🌧 : '+str(forecast['totalprecip_in'])+'Inches')                                                        
        except : 
            bot.reply_to(message,'🔴🔴 Make sure the city name you entered is correct 🔴🔴')
 ```
 * The following code is for setting the hourly forecast day and displaying the list of forecast hours
 ```
     elif message.text in select_day_for_hourly_forecast : 
        global hour4
        hour4 = message.text
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('00:00','01:00','02:00','03:00')
        markup.row('04:00','05:00','06:00','07:00')
        markup.row('08:00','09:00','10:00','11:00')
        markup.row('12:00','13:00','14:00','15:00')
        markup.row('16:00','17:00','18:00','19:00')
        markup.row('20:00','21:00','22:00','23:00')
        markup.row('Return to main page ↩️','Return to the hourly daily forecast page 🔙')
        bot.send_message(chat_id,'‼️ Select one of the following hours and you will receive the weather forecast for that hour according to the selected time frame ‼️',reply_markup=markup)
      
 ```
 
 * The following code is used to get the hourly forecast
 ```
     elif message.text in choose_an_hour : 
        try :

            hour2 = message.text
            
            querystring = {"q":city_name,"days":"3"}

            headers = {
         "X-RapidAPI-Key": RapidAPI_Key,
         "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

            response = requests.request("GET", url, headers=headers, params=querystring)

            information_received = json.loads(response.text)
            location = information_received["location"]
            forecast = information_received['forecast']["forecastday"][select_day_for_hourly_forecast[hour4]]['hour'][choose_an_hour[hour2]]
            condition = forecast['condition']
            location = information_received["location"]
            date1 = information_received['forecast']["forecastday"][select_day_for_hourly_forecast[hour4]]            

            bot.reply_to(message,'Country Name 🌎 : '+location['country']+'\nRegion 🗺 : '+location['region']+'\nCity Name 🏙 : '+location['name']+"\n------------------------------------------------------"+'\nForecast Date 🗓 : '+str(date1['date'])+'\n'+condition['text']+' At '+hour2+' '+sticker[condition['text']]+"\nTemperature 🌡 : "+str(forecast['temp_c'])+"°C"+"\nFeels Like 🚻 : "+str(forecast['feelslike_c'])+"°C"+"\nThe Heat We Feel ♨️ : "+str(forecast['heatindex_c'])+'°C'+"\nTemperature 🌡 : "+str(forecast['temp_f'])+"°F"+"\nFeels Like 🚻 : "+str(forecast['feelslike_f'])+"°F"+"\nThe Heat We Feel ♨️ : "+str(forecast['heatindex_f'])+'°F'+"\nWind Speed At "+hour2+" 🌬 : "+str(forecast['wind_kph'])+"KPH"+"\nWind Speed At "+hour2+" 🌬 : "+str(forecast['wind_mph'])+"MPH"+"\nWind Temperature 🌡 : "+str(forecast['windchill_c'])+'°C'+"\nWind Temperature 🌡: "+str(forecast['windchill_f'])+'°F'+"\nWind Direction 🧭 : "+str(forecast["wind_dir"])+"\nPressure In Inches 🛫 : "+str(forecast["pressure_in"])+"\nWill It Rain "+the_name_of_each_day_2[hour4]+' At '+hour2+' 🌧 : '+yes_or_no[str(forecast["will_it_rain"])]+'\nChance Of Rain '+the_name_of_each_day_2[hour4]+' At '+hour2+' 🌧 : '+str(forecast['chance_of_rain'])+'%'+"\nPrecipitation Amount 🌧 : "+str(forecast['precip_mm'])+"MM"+"\nPrecipitation Amount 🌧 : "+str(forecast['precip_in'])+"Inches"+"\nWill It Snow "+the_name_of_each_day_2[hour4]+" At "+hour2+' 🌨 : '+yes_or_no[str(forecast["will_it_snow"])]+'\nChance Of Snow '+the_name_of_each_day_2[hour4]+' At '+hour2+' 🌨 : '+str(forecast['chance_of_snow'])+'%')                                                                                                                                                                
        except : 
            bot.reply_to(message,'🔴🔴 Make sure the city name you entered is correct 🔴🔴')
 ```
 * <a href="https://github.com/Mohammadrezaasan/Weather-Info-Bot/blob/main/Main.py">Click here to get the full code</a>
 
 * <a href="https://github.com/Mohammadrezaasan/Weather-Info-Bot/blob/main/weather_info_config.py">Click here to get the config file</a>
 ## Keyword guide
	
|Keyword names|What can they do?|
|:---:|------|
|The name of the desired city :|Saves the desired city name.|
|🤖 Introducing The Robot 🤖|This key will help you get to know the bot and understand what it can do.|
|📓 Click here to open the list of keywords for you 📓|You can use this key to open the keyword list.|
|🔄 Changing the name of the city 🔄|Using this key, you can change the name of the city you want.|
|🌦 Click here to get current weather conditions 🌦|You can use this key to get the current weather condition.|
|😎 click here to get the weather forecast 😎|Using this key, a list of keywords will be opened for you, using which you can get the weather forecast.|
|⏳ Daily Forecast ⏳|Using this key, a list of keywords will be opened for you, with which you can set the weather forecast for the day you want.|
|🕥 Hourly Daily Forecast 🕥|Using this key, a list of keywords will be opened for you. First, you specify the forecast day and then the list of hours will open for you to enter any hour that is in the list. You will get the weather conditions for the hour you entered.|
|🌌 Day And Night Times 🌄For Example[ sunrise : 5:55 ]|You can use this key to get information such as Sunrise, Sunset,Moonrise, Moonset, Moon phases, Moonlight.|
|⌚️🌎 Click here to get the local time of your desired location ⌚️🌎|You can use this key to get the local time of any city and any country|

 ## How does the bot respond to keywords?
 |<p align="center"><video src="https://user-images.githubusercontent.com/108104864/188339284-0438f705-3890-4321-bcb2-f0af97978fb6.MOV" width="250" height="500"/>|
|:---:|
|!!Keywords used in the video!!|
|The name of the desired city :|Saves the desired city name.|
|🤖 Introducing The Robot 🤖|This key will help you get to know the bot and understand what it can do.|
|📓 Click here to open the list of keywords for you 📓|You can use this key to open the keyword list.|
|🔄 Changing the name of the city 🔄|Using this key, you can change the name of the city you want.|
|🌦 Click here to get current weather conditions 🌦|You can use this key to get the current weather condition.|
|😎 click here to get the weather forecast 😎|Using this key, a list of keywords will be opened for you, using which you can get the weather forecast.|
|⏳ Daily Forecast ⏳|Using this key, a list of keywords will be opened for you, with which you can set the weather forecast for the day you want.|
|🕥 Hourly Daily Forecast 🕥|Using this key, a list of keywords will be opened for you. First, you specify the forecast day and then the list of hours will open for you to enter any hour that is in the list. You will get the weather conditions for the hour you entered.|
|🌌 Day And Night Times 🌄For Example[ sunrise : 5:55 ]|You can use this key to get information such as Sunrise, Sunset,Moonrise, Moonset, Moon phases, Moonlight.|
|⌚️🌎 Click here to get the local time of your desired location ⌚️🌎|You can use this key to get the local time of any city and any country|

 
 
 
 
 
 
