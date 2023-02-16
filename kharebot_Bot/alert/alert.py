from services.config import backend_Api, binance_Api
from requests import request, post
from telegram import ParseMode
import datetime 
import time
from dotenv import load_dotenv
load_dotenv()
import os #provides ways to access the Operating System and allows us to read the environment variables

import telebot



# if __name__ == '__main__':
running = True
while running:

  try:
    x = datetime.datetime.now().minute/5  # insert your number here
    if x - int(x) != 0 or datetime.datetime.now().minute!= 00:  
        url = backend_Api + "/alert"
        response = request("GET", url)

        sendUserId=response.json()[0]
        sendDuration=response.json()[4]
        for index, y in enumerate(sendDuration):
          if y=="5mins":
            print(index)
            # # str(sendDuration).index(y)
            print(response.json()[0][index])
            print(response.json()[1][index])
            # print(response.json()[2][index])

            sendApiSecret=response.json()[0][index]
            sendTradingPair=response.json()[3][index]
            sendApiKey=response.json()[1][index]
            sendId=response.json()[2][index]


            url = binance_Api + "/price?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret +   "&cryptoRequest=" + sendTradingPair
            binance_response = request("GET", url)
            print(binance_response.json()[0])
 
            print(os.getenv("TELEGRAM_API_KEY"))
 
            # url = "https://api.telegram.org/bot"+ os.getenv("TELEGRAM_API_KEY") + "/sendMessage?chat_id=" + response.json()[2][index] + "&text=Trading pair:- " + sendTradingPair + "\n\nPrice:- " + binance_response.json()[0]
            # response = request("GET", url)
            bot = telebot.TeleBot(os.getenv("TELEGRAM_API_KEY"))
            bold_text = "Trading pair:- *" + sendTradingPair + "*\n\nPrice:- *" + binance_response.json()[0] + "*"
            bot.send_message(sendId, bold_text)



    u = datetime.datetime.now().minute/10  # insert your number here
    if u - int(u) == 0 or datetime.datetime.now().minute== 00:
      print("ff") 
    b = datetime.datetime.now().minute/15  # insert your number here
    if u - int(u) == 0 or datetime.datetime.now().minute== 00 :
      print("rr")             
    if datetime.datetime.now().minute== 30:
      print("kk")
    if datetime.datetime.now().minute== 00:
      print("yy")
    y = datetime.datetime.now().hour/2  # insert your number here
    if y - int(y) == 0 and datetime.datetime.now().minute== 00:
        print("00")
    k = datetime.datetime.now().hour/4  # insert your number here
    if k - int(k) == 0 and datetime.datetime.now().minute== 00:
        print("pp")  
    if datetime.datetime.now().hour== 00 and datetime.datetime.now().minute== 00: 
        print("dd")     
    time.sleep(60)   
  
  except KeyboardInterrupt:
      print('interrupted!') 
      continue 
