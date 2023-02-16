from telegram.ext.updater import Updater
from telegram import ParseMode
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
# from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from requests import request, post
import datetime
import json 
import services
import re

# print(services.backend_Api)

import os #provides ways to access the Operating System and allows us to read the environment variables
from services.config import backend_Api, binance_Api

load_dotenv()

print(backend_Api)

  
# def start(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "    Hello friend, Welcome to the Khare Trading Bot! ❤🎉 \n  \n With the help of our bot, you'll be able to achieve remote crypto trading 💰 with advanced trading features, developed to minimize risk and maximize profits.👌 \n \n Whether you're trading with a signal provider, on your own, or using TradingView alerts, our bot will do the heavy lifting for you. 💯"
#         )
  




# lang1 = KeyboardButton('English 👍')  
# lang2 = KeyboardButton('українська 💪')
# lang3 = KeyboardButton('Other language 🤝')
# lang_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(lang1).add(lang2).add(lang3)





# # Hello friend, Welcome to the Khare Bot.Please write\
# #         /help to see the commands available.
        

# def help(update: Update, context: CallbackContext):
#     update.message.reply_text("""Available Commands :-
#     /youtube - To get the youtube URL
#     /linkedin - To get the LinkedIn profile URL
#     /gmail - To get gmail URL
#     /geeks - To get the GeeksforGeeks URL""")
  
  
# def gmail_url(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "Your gmail link here (I am not\
#         giving mine one for security reasons)")
  
  
# def youtube_url(update: Update, context: CallbackContext):
#     update.message.reply_text("Youtube Link =>\
#     https://www.youtube.com/")
  
  
# def linkedIn_url(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "LinkedIn URL => \
#         https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/")
  
  
# def geeks_url(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "GeeksforGeeks URL => https://www.geeksforgeeks.org/")
  
  
# def unknown(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "Sorry '%s' is not a valid command" % update.message.text)
  
  
# def unknown_text(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
# updater.dispatcher.add_handler(CommandHandler('help', help))
# updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
# updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
# updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
# updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
# updater.dispatcher.add_handler(MessageHandler(
#     Filters.command, unknown))  # Filters out unknown commands
  
# # Filters out unknown messages.
# updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
# updater.start_polling()

print(datetime.datetime.now().minute)
print(40/5)



# running = True
# while running:
# x = "00" # insert your number here
# if x == "00":  
#         url = backend_Api + "/alert"
#         response = request("GET", url)


#         sendAlert=response.json()[2]
#         for x in sendAlert:
#           # if x=="5mins":
#             sendApiKey=response.json()[0][sendAlert.index(x)]
#             sendApiSecret=response.json()[1][sendAlert.index(x)]
#             sendId=response.json()[3][sendAlert.index(x)]


#             print(binance_Api)
#             url = binance_Api + "/alert?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret
#             response = request("GET", url)
#             print(response.text)
#             # url = "https://api.telegram.org/bot"+ os.getenv("TELEGRAM_API_KEY") + "/sendMessage?chat_id=" + sendId + "&text="  + response.text
#             # response = request("GET", url)
#             # post(url = API_ENDPOINT, data = data)


#             my_data = {'chat_id': sendId ,'text': response.text}
#             my_url = 'https://api.telegram.org/bot'+ os.getenv("TELEGRAM_API_KEY") +'/sendMessage'
#             post(url=my_url, data=my_data)




# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk               Defining Global Variable
global verifiedPassword
global verifiedUsername
global globalUsername
global globalPassword
global binanceApiKey
global binanceApiSecret
global globalbinanceApiKey
global globalbinanceApiSecret
global scanTrade
global binancePrice
global binance_future_trade_name
global setAlertCommand
global global_binance_get_price
setAlertCommand = "ready"
binance_future_trade_name= "never"
binancePrice="ready"
scanTrade="never"
verifiedUsername="never"
verifiedPassword="never"
binanceApiKey="never"
binanceApiSecret="never"
globalbinanceApiKey=""
globalbinanceApiSecret=""
globalUsername=""
globalPassword=""


# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk              Help Request
def help(update: Update, context: CallbackContext):
    global verifiedPassword
    global verifiedUsername
    global binance_future_trade_name
    binance_future_trade_name="never"
    verifiedPassword="never"
    verifiedUsername="never"
    binanceApiKey="never"
    binanceApiSecret="never"
    update.message.reply_text("""Available Commands :- \n/start - To start bot 🤖 \n/linkAccount - To link account to bot 👌 \n/myAccount -To access User menu \n/getPrice -To get the prices of coins \n/pasteTrade -To scan trade signals before entry \n/deleteApiKey -To delete User api \n/logOut -To sign out \n/exitAll -To sign out of all Devices
    """)




############################### Bot ######################################################################################################            STARTING THE BOT
def start(update, context):

   global verifiedPassword
   global verifiedUsername
   global binance_future_trade_name
   binance_future_trade_name="never"
   verifiedPassword="never"
   verifiedUsername="never"
   global chat_id
   chat_id =  update.message.chat_id

  #  first_name = update.message.chat.first_name
  #  last_name = update.message.chat.last_name
  #  username = update.message.chat.username
   print("chat_id : {}". format(chat_id))
   update.message.reply_text(main_menu_message(),
  reply_markup=main_menu_keyboard(update, context))

def main_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard(update, context)
                        )



# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk              Linking My Account
def linkAccount(update: Update, context: CallbackContext):
    global verifiedPassword
    global verifiedUsername
    global binanceApiKey
    global binanceApiSecret
    global binance_future_trade_name
    binance_future_trade_name="never"
    verifiedPassword="never"
    binanceApiKey="never"
    binanceApiSecret="never"
    chat_id =  update.message.chat_id
    url = backend_Api + "/id"

    response = request("GET", url)

    print(response.json())
  # for info in response.json()[0]:
    print(response.json()[0])
    if str(chat_id) in response.json()[0]:
         verifiedUsername ="never"
         update.message.reply_text(
          "Your Account is already linked to this bot, click on /logOut to sign out"
         )
    else:     
       verifiedUsername ="ready"
       update.message.reply_text("Enter Email Address")



# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk              Scan Pasting Signal
def pasteCode(update: Update, context: CallbackContext):
    global verifiedPassword
    global verifiedUsername
    global binanceApiKey
    global binanceApiSecret
    global scanTrade
    scanTrade="ready"
    verifiedPassword="never"
    binanceApiKey="never"
    binanceApiSecret="never"
    verifiedUsername ="never"
    chat_id =  update.message.chat_id
    update.message.reply_text("Step 1:- \nUse abbreviation like example [BTC, ETH, BNB], not bitcoin or ethereum or ethereums🤷‍♀️👍. \n \nStep 2:- \nEnsure that the trading pair has no space of symbols inbetween each other, for example[BTC/USDT ❌, BTCUSDT ✔] to ensure accuracy. \n \nStep 3:-  \nThe signal or trade details you want to paste should be detailed, at least should contain the key requirement to enter the trade 🏃‍♂️😉. \n \nStep 4:- \nLastly before you click on 'Confirm' make sure you have reviewed that all the BOT has successfully detected the trade details you pasted.👌 ")
    update.message.reply_text("Paste the Trade Signal")






# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                Globally Signing Out
def exitAll(update: Update, context: CallbackContext):
    global verifiedPassword
    global verifiedUsername
    global binanceApiKey
    global binanceApiSecret
    verifiedPassword="never"
    binanceApiKey="never"
    binanceApiSecret="never"
    verifiedUsername ="never"

    chat_id =  update.message.chat_id
    url = backend_Api + "/signout?globalSignout=" + str(chat_id)

    response = request("GET", url)

    print(response.text)
  # for info in response.json()[0]:
    if response.text=="none":
         verifiedUsername ="never"
         update.message.reply_text(
          "Your Account is not linked to any device‼, \n \nTry /linkAccount to sign in or click on <a href='https://kharetradingbot.netlify.app/'>here</a> to create an account",parse_mode=ParseMode.HTML
         )
    else:     
       update.message.reply_text(response.text)



# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk              My Account Callback

def first_menu_one(update,context):
  global verifiedPassword
  global verifiedUsername
  verifiedPassword="never"
  verifiedUsername="never"
  chat_id = update.callback_query.message.chat.id
  print(chat_id)
  query = update.callback_query
  query.answer()
  url = backend_Api + "/id"

  response = request("GET", url)

  print(response.json())
  # for info in response.json()[0]:
  print(response.json()[0])
    # if response.json()[0][info] != str(chat_id):
  if str(chat_id) in response.json()[0]:
        query.edit_message_text(
                        text='Welcome back, ' +  response.json()[1][response.json()[0].index(str(chat_id))] + "👋 \n \nHere are your offers 🔌.", 
                        reply_markup=first_menu_one_keyboard_one())   
  
  else:                   

     query.edit_message_text(text="Sorry, your Account is not linked to the Trading bot, Please click on /linkAccount to link your account. 🤖 \n\n\nIf you haven't Signup, please click on the button below to register👇👇👇",
       reply_markup=reply_markup)       
                        # reply_markup=first_menu_one_keyboard_one())   


# Create the inline keyboard

                                      


  # Link your Trading Bot 🫵🏻
reg_keyboard =  InlineKeyboardButton(text='Continue on Website 💻', url='https://kharetradingbot.netlify.app/signup', callback_data='open_url')
keyboard = [[reg_keyboard]]
reply_markup = InlineKeyboardMarkup(keyboard)

def first_menu_one_keyboard_one():
  keyboard = [[InlineKeyboardButton('Binance 👉', callback_data='binance')],
              [InlineKeyboardButton('Kucoin 👉', callback_data='kucoin')],
                      [InlineKeyboardButton('Back 🔙', callback_data='main')]
                    ]

  return InlineKeyboardMarkup(keyboard)

def client_keyboard_binance():
  keyboard = [[InlineKeyboardButton('Get Price 👉', callback_data='getPrice_binance')],
             [InlineKeyboardButton('My Info 👉', callback_data='myInfo_binance')],
             [InlineKeyboardButton('Check Balance 👉', callback_data='checkBalance_binance')],
             [InlineKeyboardButton('Set Alert 👉', callback_data='setAlert_binance')],
              [InlineKeyboardButton('Enter Trade 👉', callback_data='manualTrading_binance')],
              [InlineKeyboardButton('Transfer 👉', callback_data='transfer_binance')],
              [InlineKeyboardButton('Live Trade 👉', callback_data='liveTrade_binance')],
              [InlineKeyboardButton('Auto Trading 👉', callback_data='autoTrading_binance')],
              [InlineKeyboardButton('Purchase Airtime 👉', callback_data='purchaseAirtime_binance')],
              [InlineKeyboardButton('Purchase Data 👉', callback_data='purchaseData_binance')],
              [InlineKeyboardButton('Sign Out 🚪', callback_data='signout')],
              [InlineKeyboardButton('Back 🔙', callback_data='m11')]
              # [InlineKeyboardButton(cha, callback_data='main')]
              ]
  return InlineKeyboardMarkup(keyboard)



# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk      BINANCE API CALLBACK
def binance_menu_one(update,context):
  print("yeah")
  global verifiedPassword
  global verifiedUsername
  global binanceApiKey
  global binanceApiSecret
  # binanceApiSecret="ready"
  verifiedPassword="never"
  verifiedUsername="never"
  chat_id = update.callback_query.message.chat.id
  print(chat_id)
  query = update.callback_query
  query.answer()
  url = backend_Api + "/binance?id=" + str(chat_id)

  response = request("GET", url)

  # for info in response.json()[0]:
  print(response.text)

  if response.text=="unaunteticated" :
   binanceApiKey="ready"
   query.edit_message_text("Enter your Binance API Key \n \n \n \nDon't know how to get your Binance API click <a href='https://www.binance.com/en/support/faq/how-to-create-api-360002502072'>here</a> ",parse_mode=ParseMode.HTML)
  #  query.edit_message_text("Enter your Binance API Key")
  #  query.edit_message_text("Enter your Binance API Key")
  else: 
    binanceApiKey="never" 
    query.edit_message_text(
                        text='Welcome back, ' +  response.text + "👋 \n \nHere are your offers 🔌.", 
                        reply_markup=client_keyboard_binance())  






# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk        My Account CallBack

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk         My Account Link



def first_menu_one_link(update,context):
  global verifiedPassword
  global verifiedUsername
  verifiedPassword="never"
  verifiedUsername="never"
  chat_id = update.message.chat_id
  print(chat_id)
  query = update.callback_query
  # query.answer()
  url = backend_Api + "/id"

  response = request("GET", url)

  print(response.json())
  # for info in response.json()[0]:
  print(response.json()[0])
    # if response.json()[0][info] != str(chat_id):
  if str(chat_id) in response.json()[0]:
         update.message.reply_text(
                        text='Welcome back, ' +  response.json()[1][response.json()[0].index(str(chat_id))] + "👋 \n \nHere are your offers 🔌.", 
                        reply_markup=first_menu_one_keyboard_one())   
  
  else:                   

          update.message.reply_text(text="""Sorry, your Account is not linked to the Trading bot, Please click on /linkAccount to link your account. 🤖 \n\nIf you haven't Signup, please click on the button below to register👇👇👇""",  reply_markup=signup_menu_keyboard())                                          



def signup_menu_keyboard(update, context):
  # Link your Trading Bot 🫵🏻
  keyboard = [
              [InlineKeyboardButton(text='Continue on Website 💻 (Recommended)', url='https://kharetradingbot.netlify.app/signup')]
  ]
  return InlineKeyboardMarkup(keyboard)

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk          SET ALERT



def setAlert_binance(update,context):
      query = update.callback_query
      query.answer()
      query.edit_message_text(text="Select your time Interval:", reply_markup=set_alert_keyboard_binance()) 






def mins5_binance(update,context):
      chat_id = update.callback_query.message.chat.id
      query = update.callback_query
      query.answer()
      url = backend_Api + "/binance_api?id=" + str(chat_id)

      response = request("GET", url)

      sendApiKey=response.json()[0]
      sendApiSecret=response.json()[1]

      url = binance_Api + "/price?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret + "&cryptoRequest=BTCUSDT"

      response = request("GET", url)
      print(response.json())
      if response.json()=="401 Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.":
          query.edit_message_text("Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.")
      else:
          global setAlertCommand
          global setDuration
          global binancePrice
          binancePrice ="never"
          setDuration = "5mins"
          setAlertCommand = "ready" 
          query.edit_message_text(text="Please enter your trading pair in this format e.g[BTCUSDT, TRXUSDT, BNBBUSD]:")       


def mins10_binance(update,context):
      chat_id = update.callback_query.message.chat.id
      query = update.callback_query
      query.answer()
      url = backend_Api + "/binance_api?id=" + str(chat_id)

      response = request("GET", url)

      sendApiKey=response.json()[0]
      sendApiSecret=response.json()[1]

      url = binance_Api + "/price?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret + "&cryptoRequest=BTCUSDT"

      response = request("GET", url)
      if response.json()=="401 Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.":
          query.edit_message_text("Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.")
      else:
          global setAlertCommand
          global setDuration
          global binancePrice
          binancePrice ="never"
          setDuration = "10mins"
          setAlertCommand = "ready" 
          query.edit_message_text(text="Please enter your trading pair in this format e.g[BTCUSDT, TRXUSDT, BNBBUSD]:")         


def mins15_binance(update,context):
      chat_id = update.callback_query.message.chat.id
      query = update.callback_query
      query.answer()
      url = backend_Api + "/binance_api?id=" + str(chat_id)

      response = request("GET", url)

      sendApiKey=response.json()[0]
      sendApiSecret=response.json()[1]

      url = binance_Api + "/price?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret + "&cryptoRequest=BTCUSDT"

      response = request("GET", url)
      if response.json()=="401 Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.":
          query.edit_message_text("Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.")
      else:
          global setAlertCommand
          global setDuration
          global binancePrice
          binancePrice ="never"
          setDuration = "15mins"
          setAlertCommand = "ready" 
          query.edit_message_text(text="Please enter your trading pair in this format e.g[BTCUSDT, TRXUSDT, BNBBUSD]:")  



def mins30_binance(update,context):
      chat_id = update.callback_query.message.chat.id
      query = update.callback_query
      query.answer()
      url = backend_Api + "/binance_api?id=" + str(chat_id)

      response = request("GET", url)

      sendApiKey=response.json()[0]
      sendApiSecret=response.json()[1]

      url = binance_Api + "/price?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret + "&cryptoRequest=BTCUSDT"

      response = request("GET", url)
      if response.json()=="401 Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.":
          query.edit_message_text("Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.")
      else:
          global setAlertCommand
          global setDuration
          global binancePrice
          binancePrice ="never"
          setDuration = "30mins"
          setAlertCommand = "ready" 
          query.edit_message_text(text="Please enter your trading pair in this format e.g[BTCUSDT, TRXUSDT, BNBBUSD]:")  


def hour1_binance(update,context):
      chat_id = update.callback_query.message.chat.id
      query = update.callback_query
      query.answer()
      url = backend_Api + "/binance_api?id=" + str(chat_id)

      response = request("GET", url)

      sendApiKey=response.json()[0]
      sendApiSecret=response.json()[1]

      url = binance_Api + "/price?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret + "&cryptoRequest=BTCUSDT"

      response = request("GET", url)
      if response.json()=="401 Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.":
          query.edit_message_text("Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.")
      else:
          global setAlertCommand
          global setDuration
          global binancePrice
          binancePrice ="never"
          setDuration = "1hour"
          setAlertCommand = "ready" 
          query.edit_message_text(text="Please enter your trading pair in this format e.g[BTCUSDT, TRXUSDT, BNBBUSD]:")  


def hour2_binance(update,context):
      chat_id = update.callback_query.message.chat.id
      query = update.callback_query
      query.answer()
      url = backend_Api + "/binance_api?id=" + str(chat_id)

      response = request("GET", url)

      sendApiKey=response.json()[0]
      sendApiSecret=response.json()[1]

      url = binance_Api + "/price?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret + "&cryptoRequest=BTCUSDT"

      response = request("GET", url)
      if response.json()=="401 Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.":
          query.edit_message_text("Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.")
      else:
          global setAlertCommand
          global setDuration
          global binancePrice
          binancePrice ="never"
          setDuration = "2hours"
          setAlertCommand = "ready" 
          query.edit_message_text(text="Please enter your trading pair in this format e.g[BTCUSDT, TRXUSDT, BNBBUSD]:")           


def hour4_binance(update,context):
      chat_id = update.callback_query.message.chat.id
      query = update.callback_query
      query.answer()
      url = backend_Api + "/binance_api?id=" + str(chat_id)

      response = request("GET", url)

      sendApiKey=response.json()[0]
      sendApiSecret=response.json()[1]

      url = binance_Api + "/price?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret + "&cryptoRequest=BTCUSDT"

      response = request("GET", url)
      if response.json()=="401 Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.":
          query.edit_message_text("Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.")
      else:
          global setAlertCommand
          global setDuration
          global binancePrice
          binancePrice ="never"
          setDuration = "4hours"
          setAlertCommand = "ready" 
          query.edit_message_text(text="Please enter your trading pair in this format e.g[BTCUSDT, TRXUSDT, BNBBUSD]:") 



def day1_binance(update,context):
      chat_id = update.callback_query.message.chat.id
      query = update.callback_query
      query.answer()
      url = backend_Api + "/binance_api?id=" + str(chat_id)

      response = request("GET", url)

      sendApiKey=response.json()[0]
      sendApiSecret=response.json()[1]

      url = binance_Api + "/price?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret + "&cryptoRequest=BTCUSDT"

      response = request("GET", url)
      if response.json()=="401 Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.":
          query.edit_message_text("Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.")
      else:
          global setAlertCommand
          global setDuration
          global binancePrice
          binancePrice ="never"
          setDuration = "1day"
          setAlertCommand = "ready" 
          query.edit_message_text(text="Please enter your trading pair in this format e.g[BTCUSDT, TRXUSDT, BNBBUSD]:")           


def set_alert_keyboard_binance():
  keyboard = [[InlineKeyboardButton('5 Mins 👉', callback_data='mins5_binance')],
             [InlineKeyboardButton('10 Mins 👉', callback_data='mins10_binance')],
             [InlineKeyboardButton('15 Mins 👉', callback_data='mins15_binance')],
             [InlineKeyboardButton('30 Mins 👉', callback_data='mins30_binance')],
             [InlineKeyboardButton('1 Hour 👉', callback_data='hour1_binance')],
             [InlineKeyboardButton('2 Hours 👉', callback_data='hour2_binance')],
              [InlineKeyboardButton('4 Hours 👉', callback_data='hour4_binance')],
              [InlineKeyboardButton('1 Day 👉', callback_data='day1_binance')],
              [InlineKeyboardButton('Edit Alert👉', callback_data='edit_alert_binance')],

              [InlineKeyboardButton('Back 🔙', callback_data='binance')]
              # [InlineKeyboardButton(cha, callback_data='main')]
              ]
  return InlineKeyboardMarkup(keyboard)

def selected_alert_keyboard_binance():
  keyboard = [
              [InlineKeyboardButton('Back 🔙', callback_data='setAlert_binance')]
              # [InlineKeyboardButton(cha, callback_data='main')]
              ]
  return InlineKeyboardMarkup(keyboard)


# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk          Check Binance Balance



def check_Binance_Balance(update,context):
  chat_id = update.callback_query.message.chat.id
  print(chat_id)
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text="Check your Balance here:-", 
                        reply_markup=check_Binance_Balance_keyboard())   
                                       


def check_Binance_Balance_keyboard():
  keyboard = [[InlineKeyboardButton('Overall Balance 👉', callback_data='overallbalance_binance')],
              [InlineKeyboardButton('Futures Balance 👉', callback_data='futuresbalance_binance')],
              [InlineKeyboardButton('Spot Balance 👉', callback_data='spotbalance_binance')],
              [InlineKeyboardButton('Margin Balance 👉', callback_data='marginbalance_binance')],
                      [InlineKeyboardButton('Back 🔙', callback_data='binance')]
                    ]

  return InlineKeyboardMarkup(keyboard)

def Binance_Back_Balance_keyboard():
  keyboard = [
                      [InlineKeyboardButton('Back 🔙', callback_data='binance')]
                    ]

  return InlineKeyboardMarkup(keyboard)

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk OVERALL BALANCE BINANCE
def overallbalance_binance(update,context):
  chat_id = update.callback_query.message.chat.id
  print(chat_id)
  query = update.callback_query
  query.answer()
  url = backend_Api + "/binance_api?id=" + str(chat_id)

  response = request("GET", url)

  sendApiKey=response.json()[0]
  sendApiSecret=response.json()[1]

  url = binance_Api + "/balance?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret + "&balanceRequest=all"

  response = request("GET", url)

  # print(response.json())
  query.edit_message_text(text=response.json(),
                          reply_markup=Binance_Back_Balance_keyboard())   
                                       

def futuresbalance_binance(update,context):
  chat_id = update.callback_query.message.chat.id
  print(chat_id)
  query = update.callback_query
  query.answer()
  url = backend_Api + "/binance_api?id=" + str(chat_id)

  response = request("GET", url)

  sendApiKey=response.json()[0]
  sendApiSecret=response.json()[1]

  url = binance_Api + "/balance?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret + "&balanceRequest=futures"

  response = request("GET", url)

  # print(response.json())
  query.edit_message_text(
                        text="Check your Balance here:-", 
                        reply_markup=check_Binance_Balance_keyboard())   


def spotbalance_binance(update,context):
  chat_id = update.callback_query.message.chat.id
  print(chat_id)
  query = update.callback_query
  query.answer()
  url = backend_Api + "/binance_api?id=" + str(chat_id)

  response = request("GET", url)

  sendApiKey=response.json()[0]
  sendApiSecret=response.json()[1]

  url = binance_Api + "/balance?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret + "&balanceRequest=spot"

  response = request("GET", url)

  # print(response.json())
  query.edit_message_text(
                        text=response.text, 
                        reply_markup=Binance_Back_Balance_keyboard())                         
                                       


def check_Binance_Balance_keyboard():
  keyboard = [[InlineKeyboardButton('Overall Balance 👉', callback_data='overallbalance_binance')],
              [InlineKeyboardButton('Futures Balance 👉', callback_data='futuresbalance_binance')],
              [InlineKeyboardButton('Spot Balance 👉', callback_data='spotbalance_binance')],
              [InlineKeyboardButton('Margin Balance 👉', callback_data='marginbalance_binance')],
                      [InlineKeyboardButton('Back 🔙', callback_data='main')]
                    ]

  return InlineKeyboardMarkup(keyboard)

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk          Get Prices Of Coins Binance


def check_Price_menu_message():
  return "Select which Trading Account:"
def check_Price_keyboard():
  keyboard = [[InlineKeyboardButton('Binance 👉', callback_data='binance_price')],
              [InlineKeyboardButton('Kucoin 👉', callback_data='kucoin_price')],
  ]
  return InlineKeyboardMarkup(keyboard)



def getPrice_binance_link(update,context):
  query = update.callback_query
  # query.answer()
  chat_id =  update.message.chat_id
  url = backend_Api + "/id"

  response = request("GET", url)

  print(response.json())
  # for info in response.json()[0]:
  print(response.json()[0])
  if str(chat_id) in response.json()[0]:
    update.message.reply_text(
                        text=check_Price_menu_message(),
                        reply_markup=check_Price_keyboard())
  else:
     update.message.reply_text(      
      "You presently haven't linked your account with the bot. \n \nClick on /linkAccount to sign in."
     )  

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk   BINANCE PRICE

kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk Price Button
def binance_price(update,context):
  global binancePrice
  chat_id = update.callback_query.message.chat.id
  query = update.callback_query
  query.answer()
  url = backend_Api + "/binance?id=" + str(chat_id)

  response = request("GET", url)

  # for info in response.json()[0]:
  print(response.text)

  if response.text=="unaunteticated" :
   binancePrice="never"
   query.edit_message_text("You presently don't have an API linked to this bot. \nYou need to link your account to an API to make a request to the server 👍. \nClick on /myAccount to link your Binance API to this trading Bot 🏃‍♂️💨.")

  else: 
    binancePrice="ready"
    query.edit_message_text(
                       "Step 1. \nUse symbols when making a request for example [ ETHUSDT, BTCUSDT, TRXUSDT, XRPUSDT.....] ✔ not [bitcoin or tron or dogecoin] ❌. \n \nStep 2. \nWhen entering trading pair don't leave space or symbols inbetween [BTCUSDT ✔] \n[BTC ETH ❌ BTC~USDT ❌] \n \n \nEnter the trading pair ")  


 






def check_again_binance_price(update,context):
  global binancePrice
  chat_id = update.callback_query.message.chat.id
  query = update.callback_query
  query.answer()
  url = backend_Api + "/binance?id=" + str(chat_id)

  response = request("GET", url)

  # for info in response.json()[0]:
  print(response.text)

  if response.text=="unaunteticated" :
   binancePrice="never"
   query.edit_message_text("You presently don't have an API linked to this bot. \nYou need to link your account to an API to make a request to the server 👍. \nClick on /myAccount to link your Binance API to this trading Bot 🏃‍♂️💨.")

  else: 
    binancePrice="ready"
    query.edit_message_text(
                       "Step 1. \nUse symbols when making a request for example [ ETHUSDT, BTCUSDT, TRXUSDT, XRPUSDT.....] ✔ not [bitcoin or tron or dogecoin] ❌. \n \nStep 2. \nWhen entering trading pair don't leave space or symbols inbetween [BTCUSDT ✔] \n[BTC ETH ❌ BTC~USDT ❌] \n \n \nEnter the trading pair ")  





# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                  ENTER A TRADE MANUAL

def manualTrading_keyboard():
  keyboard = [[InlineKeyboardButton('Futures 👉', callback_data='futures_manualTrading_binance')],
              [InlineKeyboardButton('Spot 👉', callback_data='spot_manualTrading_binance')],
              [InlineKeyboardButton('Margin 👉', callback_data='margin_manualTrading_binance')],
                      [InlineKeyboardButton('Back 🔙', callback_data='binance')]

  ]
  return InlineKeyboardMarkup(keyboard)

def manualTrading_binance(update,context):
  chat_id = update.callback_query.message.chat.id
  print(chat_id)
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text="Select your trading medium:-", 
                        reply_markup=manualTrading_keyboard())  



def futures_manualTrading_binance(update,context):
  global binance_future_trade_name
  global binancePrice
  global binance_future_trade_type
  global binance_future_trade_method
  global binance_future_trade_quantity
  binance_future_trade_quantity="never"
  binance_future_trade_method="never"
  binancePrice="never"
  binance_future_trade_name="ready"
  binance_future_trade_type="never"
  chat_id = update.callback_query.message.chat.id
  print(chat_id)
  query = update.callback_query
  query.answer()


  query.edit_message_text(
                        text="Enter the trading pair \ne.g[BTCUSDT, ETHUSDT, BNBBUSD.....]", 
)  



# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk          Sign Out
def signout_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=signout_menu_message(),
                        reply_markup=signout_keyboard())
def signout_menu_message():
  return "Are you sure you want to SIGNOUT from this trading bot?"
def signout_keyboard():
  keyboard = [[InlineKeyboardButton('Yes ✅', callback_data='yes_signout')],
              [InlineKeyboardButton('No ❌', callback_data='m11')],
  ]
  return InlineKeyboardMarkup(keyboard)



def signout(update: Update, context: CallbackContext):
       url = backend_Api+ "/signout?id=" + str(update.callback_query.message.chat.id)

       response = request("GET", url)

       print(response.text)
       query = update.callback_query
       query.answer()
       query.edit_message_text(
      #  update.message.reply_text(
        response.text
       )

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkusing the LOGOUT LINK

def signout_menu_link(update,context):
  query = update.callback_query
  # query.answer()
  chat_id =  update.message.chat_id
  url = backend_Api + "/id"

  response = request("GET", url)

  print(response.json())
  # for info in response.json()[0]:
  print(response.json()[0])
  if str(chat_id) in response.json()[0]:
    update.message.reply_text(
                        text=signout_menu_message(),
                        reply_markup=signout_keyboard())
  else:
     update.message.reply_text(      
      "You presently haven't linked your account with the bot. \n \nClick on /linkAccount to sign in."
     )             



# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk Sign Out END








def second_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=second_menu_message(),
                        reply_markup=second_menu_keyboard())

# and so on for every callback_data option
def first_submenu(bot, update):
  pass

def second_submenu(bot, update):
  pass

############################ Keyboards #########################################
def main_menu_keyboard(update, context):
  # Link your Trading Bot 🫵🏻
  keyboard = [[InlineKeyboardButton('My Account 👍', callback_data='m11')],
              [InlineKeyboardButton(text='Continue on Website 💻 (Recommended)', url='https://kharetradingbot.netlify.app/login')],
              [InlineKeyboardButton('ℹ About Khare', callback_data='m12')]]
  return InlineKeyboardMarkup(keyboard)





def second_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
              [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message():
  return "Hello friend, Welcome to the Khare Trading Bot! ❤🎉 \n  \nWith the help of our bot, you'll be able to achieve remote crypto trading 💰 with advanced trading features, developed to minimize risk and maximize profits.👌 \n \nWhether you're trading with a signal provider, on your own, or using TradingView alerts, our bot will do the heavy lifting for you. 💯 \n  \nClick on /link if you're lost. \n \nChoose the option in main menu:     "



def second_menu_message():
  return 'Choose the submenu in second menu:'


# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk          Delete Trading Api
def  deleteApiKey(update,context):
  query = update.callback_query
  # query.answer()
  print("ooo")
  chat_id =  update.message.chat_id
  url = backend_Api + "/id"

  response = request("GET", url)

  print(response.json())
  # for info in response.json()[0]:
  print(response.json()[0])
  if str(chat_id) in response.json()[0]:
    update.message.reply_text(
                        text=deleteApi_message(),
                        reply_markup=deleteApi_keyboard())
  else:
     update.message.reply_text(      
      "You presently haven't linked your account with the bot. \n \nClick on /linkAccount to sign in."
     )     



def deleteApi_message():
  return "Select which trading account:"
def deleteApi_keyboard():
  keyboard = [[InlineKeyboardButton('Binance 👉', callback_data='binanceApiDelete')],
              [InlineKeyboardButton('Kucoin 👉', callback_data='m11')],
              [InlineKeyboardButton('Back 🔙', callback_data='m11')],
  ]
  return InlineKeyboardMarkup(keyboard)

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk               Delete Binance Api

def binanceApiDelete(update,context):
  query = update.callback_query
  query.answer()
  print("ls")
  chat_id=update.callback_query.message.chat.id
  url = backend_Api+ "/binance?id=" + str(update.callback_query.message.chat.id)

  response = request("GET", url)

  # print(response.json())
  if response.text== "unaunteticated":
      query.edit_message_text("Sorry, you haven't connected your Binance api with this account. \n \nClick /addApi to connect your api to this trading bot.")
  else:    
     query.edit_message_text(
                        text=binanceApiDelete_message(),
                        reply_markup=binanceApiDelete_keyboard())


def binanceApiDelete_message():
  return "Are you sure you want to delete your Binance Api from this trading bot?"
def binanceApiDelete_keyboard():
  keyboard = [[InlineKeyboardButton('Yes ✅', callback_data='yes_binanceApiDelete')],
              [InlineKeyboardButton('No ❌', callback_data='m11')],
  ]
  return InlineKeyboardMarkup(keyboard)

def yes_binanceApiDelete(update,context):
  query = update.callback_query
  query.answer()

  chat_id=update.callback_query.message.chat.id
  url = backend_Api + "/binance?removeApi=" + str(update.callback_query.message.chat.id)

  response = request("GET", url)

  # print(response.json())
  query.edit_message_text("Your Binance Api key has successfully been deleted from your bot Account. \n \nClick /addApi to connect your api to this trading bot.")



def pasteTrade_keyboard():
            keyboard = [[InlineKeyboardButton('Confirm ✔', callback_data='confirmPastedTrade')],
              [InlineKeyboardButton('Edit 🤔', callback_data='editPastedTrade')],
                      [InlineKeyboardButton('Decline ❌', callback_data='binance')]
                    ]
            return InlineKeyboardMarkup(keyboard)

def binance_future_trade_type_keyboard():
            keyboard = [[InlineKeyboardButton('Cross👉', callback_data='cross_binance_future_trade_type')],
              [InlineKeyboardButton('Isolated 👉', callback_data='isolated_binance_future_trade_type')],
                    ]
            return InlineKeyboardMarkup(keyboard)  

def binance_future_trade_method_keyboard():
            keyboard = [[InlineKeyboardButton('Buy / Long 📈', callback_data='buy_binance_future_trade_method')],
              [InlineKeyboardButton('Short / Sell 📉', callback_data='sell_binance_future_trade_method')],
                    ]
            return InlineKeyboardMarkup(keyboard)    

def binance_future_trade_buy_keyboard():
            keyboard = [[InlineKeyboardButton('Market price 💹', callback_data='market_buy_binance_future_trade_method')],
              [InlineKeyboardButton('Buy limit 🕥', callback_data='limit_buy_binance_future_trade_method')],
                    ]
            return InlineKeyboardMarkup(keyboard)                           

def binance_future_trade_sell_keyboard():
            keyboard = [[InlineKeyboardButton('Market price 💹', callback_data='market_sell_binance_future_trade_method')],
              [InlineKeyboardButton('Sell limit 🕥', callback_data='limit_sell_binance_future_trade_method')],
                    ]
            return InlineKeyboardMarkup(keyboard) 
                 

def binance_future_trade_entry_keyboard():
            keyboard = [[InlineKeyboardButton('Yes ✅', callback_data='yes_takeprofit')],
              [InlineKeyboardButton('No ❌', callback_data='no_takeprofit')],
                    ]
            return InlineKeyboardMarkup(keyboard)             

def binance_future_trade_stoploss_keyboard():
            keyboard = [[InlineKeyboardButton('Yes ✅', callback_data='yes_stoploss')],
              [InlineKeyboardButton('No ❌', callback_data='no_stoploss')],
                    ]
            return InlineKeyboardMarkup(keyboard)   

def final_future_trade_keyboard():
            keyboard = [[InlineKeyboardButton('Confirm ✅', callback_data='confirm_binance_future_trade')],
              [InlineKeyboardButton('Edit 🤔', callback_data='edit_binance_future_trade')],
                      [InlineKeyboardButton('Decline ❌', callback_data='binance')]
                    ]
            return InlineKeyboardMarkup(keyboard)
def refresh_price_keyboard_binance():
            keyboard = [[InlineKeyboardButton('Refresh 🔃', callback_data='refresh_price_text_binance')],
                      [InlineKeyboardButton('Check Again', callback_data='check_again_binance_price')],
                      [InlineKeyboardButton('Back 🔙', callback_data='binance')]

                    ]
            return InlineKeyboardMarkup(keyboard)  


def confirm_binance_future_trade_message():            
   return "Trading Pair:-" + global_binance_future_trade_name+ "\nLeverage:-" + global_binance_future_trade_leverage +"\nEntry:-" + global_binance_future_trade_entry + "\nQuantity:-" + global_binance_future_trade_quantity + "\nType:-" + global_binance_future_trade_method + "\nMargin:-" + global_binance_future_trade_type + "\nTake profit:-" + global_takeprofit_binance_futures + "\nStoploss:-" + global_stoploss_binance_futures

def edit_binance_future_trade_keyboard():
            keyboard = [[InlineKeyboardButton('Trading Pair 👉', callback_data='edit_binance_future_trade_trading_pair')],
              [InlineKeyboardButton('Leverage 👉', callback_data='edit_binance_future_trade_leverage')],
                      [InlineKeyboardButton('Entry 👉', callback_data='edit_binance_future_trade_entry')]
              [InlineKeyboardButton('Type 👉', callback_data='edit_binance_future_trade_type')],
              [InlineKeyboardButton('Margin 👉', callback_data='edit_binance_future_trade_margin')],
              [InlineKeyboardButton('Quantity 👉', callback_data='edit_binance_future_trade_quantity')],
              [InlineKeyboardButton('Take Profit 👉', callback_data='edit_binance_future_trade_take_profit')],
              [InlineKeyboardButton('Stoploss 👉', callback_data='edit_binance_future_trade_stoploss')],
              [InlineKeyboardButton('Back 🔙', callback_data='confirm_binance_future_trade')]

                    ]
            return InlineKeyboardMarkup(keyboard)


global binance_future_trade_quantity
global global_binance_future_trade_type
global binance_future_trade_type


def cross_binance_future_trade_type(update,context):    
    global global_binance_future_trade_type
    global binance_future_trade_type
    binance_future_trade_type="ready"
    global_binance_future_trade_type="Cross"
    query = update.callback_query
    query.answer()
    print("ls")
    chat_id=update.callback_query.message.chat.id
    query.edit_message_text(
          text="Enter your leverage e.g[20x, 50x, 70x...]")

def isolated_binance_future_trade_type(update,context):    
    global global_binance_future_trade_type
    global binance_future_trade_type
    binance_future_trade_type="ready"
    global_binance_future_trade_type="Isolated"
    query = update.callback_query
    query.answer()
    print("ls")
    chat_id=update.callback_query.message.chat.id
    query.edit_message_text(
          text="Enter your leverage e.g[20x, 50x, 70x...]")          
 
def buy_binance_future_trade_method(update,context):
    global global_binance_future_trade_method
    global global_binance_future_trade_market
    global_binance_future_trade_method="Long"
    global_binance_future_trade_market="BUY"
    query = update.callback_query
    query.answer()
    print("ls")
    chat_id=update.callback_query.message.chat.id
    query.edit_message_text(
          text="Select the options below:",
                        reply_markup=binance_future_trade_buy_keyboard()) 

def sell_binance_future_trade_method(update,context):
    global global_binance_future_trade_market
    global global_binance_future_trade_method
    global_binance_future_trade_method="Short"
    global_binance_future_trade_market="SELL"
    query = update.callback_query
    query.answer()
    print("ls")
    chat_id=update.callback_query.message.chat.id
    query.edit_message_text(
          text="Select the options below:",
                        reply_markup=binance_future_trade_sell_keyboard())                   


def limit_buy_binance_future_trade_method(update,context):
      global binance_future_trade_method
      binance_future_trade_method="ready"
      query = update.callback_query
      query.edit_message_text(
          text="Enter Buy limit")

def limit_sell_binance_future_trade_method(update,context):
      global binance_future_trade_method
      binance_future_trade_method="ready"
      query = update.callback_query
      query.edit_message_text(
          text="Enter Sell limit")     

def market_buy_binance_future_trade_method(update,context):
      global global_binance_future_trade_entry
      global_binance_future_trade_entry="Market price"      
      query = update.callback_query
      query.edit_message_text(
          text="Set Take profit?",                        
          reply_markup=binance_future_trade_entry_keyboard())    


def market_sell_binance_future_trade_method(update,context):
      global global_binance_future_trade_entry
      global_binance_future_trade_entry="Market price"
      query = update.callback_query
      query.edit_message_text(
          text="Set Take profit?",                        
          reply_markup=binance_future_trade_entry_keyboard())  


def no_takeprofit(update,context):
       global global_takeprofit_binance_futures
       global_takeprofit_binance_futures="None"
       query = update.callback_query
       query.edit_message_text(
          text="Set Stoploss?",                        
          reply_markup=binance_future_trade_stoploss_keyboard())   

def yes_takeprofit(update,context):
       global takeprofit_binance_futures
       takeprofit_binance_futures="ready"
       query = update.callback_query
       query.edit_message_text(
          text="Enter Take profit")      

def yes_stoploss(update,context):
       global stoploss_binance_futures
       stoploss_binance_futures="ready"
       query = update.callback_query
       query.edit_message_text(
          text="Enter Stoploss")   


def no_stoploss(update,context):
       global global_stoploss_binance_futures
       global_stoploss_binance_futures="None"
       query = update.callback_query
       query.edit_message_text(
          text="Trading Pair:-" + global_binance_future_trade_name+ "\nLeverage:-" + global_binance_future_trade_leverage +"\nEntry:-" + global_binance_future_trade_entry + "\nQuantity:-" + global_binance_future_trade_quantity +"\nType:-" + global_binance_future_trade_method + "\nMargin:-" + global_binance_future_trade_type + "\nTake profit:-" + global_takeprofit_binance_futures + "\nStoploss:-" + global_stoploss_binance_futures, 
          reply_markup=final_future_trade_keyboard())     




def confirm_binance_future_trade(update,context):     
    chat_id = update.callback_query.message.chat.id    
    url = backend_Api + "/binance_api?id=" + str(chat_id)
    response = request("GET", url)

    sendApiKey=response.json()[0]
    sendApiSecret=response.json()[1]
    print(binance_Api)
    url = binance_Api + "/futures_trade?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret + "&tradingPair=" + global_binance_future_trade_name + "&margin:-" + global_binance_future_trade_type + "&leverage=" + global_binance_future_trade_leverage + "&entry=" + global_binance_future_trade_entry + "&type=" + global_binance_future_trade_method +"&market="  + global_binance_future_trade_market + "&quantity=" + global_binance_future_trade_quantity + "&takeProfit=" + global_takeprofit_binance_futures + "&stopLoss:-" + global_stoploss_binance_futures

    response = request("GET", url)
    query = update.callback_query
    query.edit_message_text( response.json())

    # print(response.json())                                 

def refresh_price_text_binance(update,context):
      chat_id = update.callback_query.message.chat.id
      query = update.callback_query      
      url = backend_Api + "/binance_api?id=" + str(chat_id)

      response = request("GET", url)

      sendApiKey=response.json()[0]
      sendApiSecret=response.json()[1]

      back = backend_Api + "/addprice?telegramId=" + str(chat_id) + "&requestType=" + "remove" 
      back_response = request("GET", back)
      print("kkkkkk")
      print(back_response.text)
      url = binance_Api + "/price?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret + "&cryptoRequest=" + back_response.text

      response = request("GET", url)


      query.edit_message_text( "Trading pair:- " + back_response.text +"\n\nPrice:- "+response.json()[0],  reply_markup= refresh_price_keyboard_binance())




def edit_binance_future_trade(update,context):
     query = update.callback_query
     query.edit_message_text(
          text="Select which Option you want to edit",
reply_markup= edit_binance_future_trade_keyboard())



def edit_binance_future_trade_trading_pair(update,context):
  global edit_binance_future_trade_condition_trading_pair
  edit_binance_future_trade_condition_trading_pair="ready"
  query = update.callback_query
  query.answer()
  query.edit_message_text(
    text="Enter the trading pair \ne.g[BTCUSDT, ETHUSDT, BNBBUSD.....]", 
)  

def edit_binance_future_trade_leverage(update,context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
          text="Enter your leverage e.g[20x, 50x, 70x...]") 
# def edit_binance_future_trade_entry(update,context):
# def edit_binance_future_trade_type(update,context):
# def edit_binance_future_trade_margin(update,context):
# def edit_binance_future_trade_take_profit(update,context):
# def edit_binance_future_trade_stoploss(update,context):



# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                                               Not a Valid Command

def unknown(update: Update, context: CallbackContext):
    global verifiedPassword
    global globalUsername
    global globalPassword
    global verifiedUsername
    global binanceApiKey
    global binanceApiSecret
    global globalbinanceApiSecret
    global globalbinanceApiKey
    global binancePrice
    global global_binance_future_trade_name
    global global_binance_future_trade_leverage
    global global_binance_future_trade_type
    global global_takeprofit_binance_futures
    global global_stoploss_binance_futures
    global binance_future_trade_name
    global binance_future_trade_type
    global binance_future_trade_method
    global global_binance_future_trade_entry
    global global_takeprofit_binance_futures
    global takeprofit_binance_futures
    global stoploss_binance_futures
    global global_stoploss_binance_futures
    global global_binance_future_trade_quantity
    global binance_future_trade_quantity
    global setDuration
    global setAlert
    global setAlertId
    global setAlertCommand
    global global_binance_get_price
      

                       

    # kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk  FOR ACCOUNT LINKING
    if verifiedUsername=="ready":

      if verifiedPassword=="ready":
        verifiedPassword="never"
        verifiedUsername="never"
        globalPassword=update.message.text.lower().strip()

        # import requests

        url = backend_Api + "/testing?email=" + globalUsername + "&password=" + globalPassword + "&id=" + str(update.message.chat_id)

        response = request("GET", url)

        print(response.text)
        update.message.reply_text(
        response.text,parse_mode=ParseMode.HTML)
        verifiedUsername="never"
        verifiedPassword="never"
      else:
        verifiedPassword="ready"
        globalUsername=update.message.text.lower().strip()
        print(globalUsername)
        update.message.reply_text(
        "Enter Password")
        print(verifiedUsername)


    elif binanceApiKey=="ready":
      if binanceApiSecret=="ready":
        binanceApiKey="never"
        binanceApiSecret="never"
        globalbinanceApiSecret=update.message.text.strip()

        url = backend_Api + "/binance?binanceApiKey=" + globalbinanceApiKey + "&binanceApiSecret=" + globalbinanceApiSecret + "&idTelegram=" + str(update.message.chat_id)

        response = request("GET", url)

        print(response.text)
        update.message.reply_text(
        response.text,parse_mode=ParseMode.HTML)


        binanceApiKey="never"
        binanceApiSecret="never"

      else:
        binanceApiSecret="ready" 
        globalbinanceApiKey=update.message.text.strip()
        update.message.reply_text(
        "Enter your Binance Api Secret") 

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk        get Price
    elif binancePrice=="ready":
      binancePrice="never"
      chat_id =  update.message.chat_id
      global_binance_get_price= update.message.text.upper().strip()
      url = backend_Api + "/binance_api?id=" + str(chat_id)

      response = request("GET", url)

      sendApiKey=response.json()[0]
      sendApiSecret=response.json()[1]
      back = backend_Api + "/addprice?telegramId=" + str(chat_id) + "&requestType=add" + "&cryptoName=" + update.message.text.upper().strip()

      url = binance_Api + "/price?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret + "&cryptoRequest=" + update.message.text.upper().strip()
      response = request("GET", url)
      back_response = request("GET", back)


  # print(response.json())
      update.message.reply_text("Trading pair:- " + global_binance_get_price +"\n\nPrice:- "+response.json()[0],  reply_markup= refresh_price_keyboard_binance())


# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk           SET ALERT
    elif setAlertCommand == "ready":
          setAlertCommand = "never"      
          setAlert= update.message.text.upper().strip()
          setAlertId= str(update.message.chat_id)
  

          url = backend_Api + "/binance_api?id=" + setAlertId
          response = request("GET", url)

          sendApiKey=response.json()[0]
          sendApiSecret=response.json()[1]
          url = binance_Api + "/price?binanceApiKey=" + sendApiKey + "&binanceApiSecret=" + sendApiSecret + "&cryptoRequest=" + update.message.text.upper().strip()

          response = request("GET", url)
          # print(response.text)
          print(response.json()[0])
          # print(response.json().isalpha())
          # print(response.text.isalpha())
          # print(str(response.json()).isalpha())
          # print(str(response.text).isalpha())

          if response.json()=="401 Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.":
              update.message.reply_text("Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨.")

          elif response.json()=="400\nInvalid symbol.\n \nClick /getPrice to try again.":
              update.message.reply_text(text="Invalid symbol try again.", reply_markup=selected_alert_keyboard_binance()) 

          elif response.json()=="400\nIllegal characters found in parameter 'symbol'; legal range is '^[A-Z0-9-_.]{1,20}$'":
              update.message.reply_text(text="Invalid characters were found\nCharacters including Spacebar and special keys, try again.", reply_markup=selected_alert_keyboard_binance())                            




          elif response.json()[1]!=200 :   
            update.message.reply_text(
          text= "Encountered error, please try again", reply_markup=selected_alert_keyboard_binance())           
          else:

            url = backend_Api + "/alert?id=" + setAlertId +"&duration=" + setDuration + "&tradingPair=" + setAlert

            response = request("GET", url)
            print("jjjlllkk")
            update.message.reply_text(
          text=response.text, reply_markup=selected_alert_keyboard_binance())              



    


# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk               ENTER TRADE MANUALLY
    elif binance_future_trade_name=="ready":
       print("LLL")
       global_binance_future_trade_name=update.message.text.upper().strip()
       binance_future_trade_name="never"
       update.message.reply_text(
          text="Select your Trade type:",
        reply_markup= binance_future_trade_type_keyboard())

    elif binance_future_trade_quantity=="ready": 
        global_binance_future_trade_quantity= update.message.text.lower().strip()
        binance_future_trade_quantity="never" 
        update.message.reply_text(
          text="Select your Trade method:",
        reply_markup= binance_future_trade_method_keyboard())   

    elif binance_future_trade_type=="ready":
         binance_future_trade_type="never"
         binance_future_trade_quantity="ready"
         for x in update.message.text.lower().strip():
            if x.isalpha():
              print(update.message.text.lower().strip()[0: update.message.text.lower().strip().index(x)])
              global_binance_future_trade_leverage=update.message.text.lower().strip()[0: update.message.text.lower().strip().index(x)] + "x"
              break
            else:
              global_binance_future_trade_leverage=update.message.text.lower().strip() + "x"
         update.message.reply_text(
          text="Enter the quantity you want to BUY/SELL.")        

    elif binance_future_trade_method=="ready":   
        global_binance_future_trade_entry=update.message.text.lower().strip()
        binance_future_trade_method="never"
        update.message.reply_text(
          text="Set Take profit?",                        
          reply_markup=binance_future_trade_entry_keyboard())   

    elif takeprofit_binance_futures=="ready":
        global_takeprofit_binance_futures=update.message.text.lower().strip()
        takeprofit_binance_futures="never"
        update.message.reply_text(
          text="Set Stoploss?",                        
          reply_markup=binance_future_trade_stoploss_keyboard()) 
       
    elif stoploss_binance_futures=="ready":
       global_stoploss_binance_futures=update.message.text.lower().strip()
       stoploss_binance_futures="never"
       update.message.reply_text(
          text=confirm_binance_future_trade_message(), 
          reply_markup=final_future_trade_keyboard())    



# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk   EDIT TRADE
    elif edit_binance_future_trade_trading_pair=="ready":
       global_binance_future_trade_name=update.message.text.upper().strip()
       binance_future_trade_name="never"
       update.message.reply_text(
          text=confirm_binance_future_trade_message(), 
          reply_markup=final_future_trade_keyboard()) 





    elif scanTrade=="ready":
        globalLoss=""
        globalProfit=""
        globalTradePosition=""
        globalTradeType=""
        globalLeverage="none"



        if "futures" in update.message.text.lower():
          globalTradeType="Futures"  
        if "cross" in update.message.text.lower():
          globalTradeType="Futures"   
        if "isolated" in update.message.text.lower():
          globalTradeType="Futures" 

        if "sl" in update.message.text.lower():
            globalTradeType="Futures"  
            definedVariable=update.message.text.lower().replace("sl", "?")
            print(definedVariable.lower()[definedVariable.index("?"):definedVariable.index("?") +6])
            if str( re.search(r'\d+', definedVariable.lower()[definedVariable.index("?"):definedVariable.index("?") +10]).group()):
               globalLoss=str( re.search(r'\d+\.\d+', definedVariable.lower()[definedVariable.index("?"):definedVariable.index("?") +10]).group()) 
            else:
               globalLoss=str( re.search(r'\d+\.\d+', definedVariable.lower()[definedVariable.index("?"): definedVariable.index("?") -10]).group())  

        if "stop" in update.message.text.lower():
          globalTradeType="Futures"  
          if "loss" in update.message.text.lower():
            definedVariable1=update.message.text.lower().replace("stop", "?")
            definedVariable=definedVariable1.replace("loss", "")
            print(definedVariable.lower()[definedVariable.index("?"):definedVariable.index("?") +6])
            if str( re.search(r'\d+', definedVariable.lower()[definedVariable.index("?"):definedVariable.index("?") +10]).group()):
               globalLoss=str( re.search(r'\d+\.\d+', definedVariable.lower()[definedVariable.index("?"):definedVariable.index("?") +10]).group()) 
            else:
               globalLoss=str( re.search(r'\d+\.\d+', definedVariable.lower()[definedVariable.index("?"): definedVariable.index("?") -10]).group()) 
          else:
            if str( re.search(r'\d+', definedVariable.lower()[definedVariable.index("?"):definedVariable.index("?") +10]).group()):
               globalLoss=str( re.search(r'\d+\.\d+', definedVariable.lower()[definedVariable.index("?"):definedVariable.index("?") +10]).group()) 
            else:
               globalLoss=str( re.search(r'\d+\.\d+', definedVariable.lower()[definedVariable.index("?"): definedVariable.index("?") -10]).group()) 

             
        #  for x in definedVariable.lower()[definedVariable.index("?"): definedVariable.index("?") +6]:
              # if x.isnumeric():
                #  globalLoss=int(re.search(r'\d+', definedVariable.lower()[definedVariable.index("?"):definedVariable.index("?") +6]).group()) 
                #  break
              # else:
                #  break  
            # for x in definedVariable.lower()[definedVariable.index("?"): definedVariable.index("?") -6]:
              # if x.isnumeric():
                #  globalLoss=int(re.search(r'\d+', definedVariable.lower()[definedVariable.index("?"): definedVariable.index("?") -6]).group()) 
                #  break 
              # else:
                #  break    
           
        if "buy" in update.message.text.lower():
          globalTradeType="Futures" 
          globalTradePosition="Buy" 
        if "sell" in update.message.text.lower():
          globalTradePosition="Sell"
          globalTradeType="Futures" 
        if "long" in update.message.text.lower():
          globalTradeType="Futures" 
          globalTradePosition="Long" 
        if "short" in update.message.text.lower():
          globalTradeType="Futures" 
          globalTradePosition="Short" 
        if "leverage" in update.message.text.lower():
          globalTradeType="Futures"   
          definedVariable=update.message.text.lower().replace("leverage", "?")
          if str( re.search(r'\d+', definedVariable.lower()[definedVariable.index("?"):definedVariable.index("?") +10]).group()):
               globalLeverage=str( re.search(r'\d+', definedVariable.lower()[definedVariable.index("?"):definedVariable.index("?") +10]).group()) + "x"
          else:
               globalLeverage=str( re.search(r'\d+', definedVariable.lower()[definedVariable.index("?"): definedVariable.index("?") -6]).group()) + "x"
        if "profit" in update.message.text.lower():
          globalTradeType="Futures"   
          definedVariable=update.message.text.lower().replace("profit", "?") 
          for x in definedVariable.lower()[definedVariable.index("?"): ] :
            if x.isalpha():
              print( definedVariable.lower()[definedVariable.rindex("?") + 2: ].index(x))
              globalProfit= definedVariable.lower()[definedVariable.rindex("?") + 2: ][0 : definedVariable.lower()[definedVariable.rindex("?") + 2: ].index(x) -2 ].strip()
              break
            else:
              globalProfit=definedVariable.lower()[definedVariable.rindex("?") + 2: ].strip() 

        if "target" in update.message.text.lower():
          globalTradeType="Futures"   
          definedVariable=update.message.text.lower().replace("target", "?") 
          for x in definedVariable.lower()[definedVariable.index("?"): ] :
            if x.isalpha():
              print( definedVariable.lower()[definedVariable.rindex("?") + 2: ].index(x))
              globalProfit= definedVariable.lower()[definedVariable.rindex("?") + 2: ][0 : definedVariable.lower()[definedVariable.rindex("?") + 2: ].index(x) -2 ].lstrip()
              break
            else:
              globalProfit=definedVariable.lower()[definedVariable.rindex("?") + 2: ].lstrip()           

        if "tp" in update.message.text.lower():
          globalTradeType="Futures"   
          definedVariable=update.message.text.lower().replace("tp", "?") 
          for x in definedVariable.lower()[definedVariable.index("?"): ] :
            if x.isalpha():
              print( definedVariable.lower()[definedVariable.rindex("?") + 2: ].index(x))
              globalProfit= definedVariable.lower()[definedVariable.rindex("?") + 2: ][0 : definedVariable.lower()[definedVariable.rindex("?") + 2: ].index(x) -2 ].lstrip()
              break
            else:
              globalProfit=definedVariable.lower()[definedVariable.rindex("?") + 2: ].lstrip()   


        if "entry" in update.message.text.lower():
          globalTradeType="Futures"   
          definedVariable=update.message.text.lower().replace("entry", "?") 
          for x in definedVariable.lower()[definedVariable.index("?"): ] :
            if x.isalpha():
              print( definedVariable.lower()[definedVariable.rindex("?") + 2: ].index(x))
              globalPrice= definedVariable.lower()[definedVariable.rindex("?") + 2: ][0 : definedVariable.lower()[definedVariable.rindex("?") + 2: ].index(x) -2 ].strip()
              break
            else:
              globalPrice=definedVariable.lower()[definedVariable.rindex("?") + 2: ].strip()


        if "price" in update.message.text.lower():
          globalTradeType="Futures"   
          definedVariable=update.message.text.lower().replace("price", "?") 
          for x in definedVariable.lower()[definedVariable.index("?"): ] :
            if x.isalpha():
              print( definedVariable.lower()[definedVariable.rindex("?") + 2: ].index(x))
              globalPrice= definedVariable.lower()[definedVariable.rindex("?") + 2: ][0 : definedVariable.lower()[definedVariable.rindex("?") + 2: ].index(x) -2 ].strip()
              if globalPrice== "":
                 definedVariable=update.message.text.lower().replace("entry", "?") 
                 for x in definedVariable.lower()[definedVariable.index("?"): ] :
                    if x.isalpha():
                       print(definedVariable.lower()[definedVariable.rindex("?") + 2: ][0 : definedVariable.lower()[definedVariable.rindex("?") + 2: ].index(x) -2 ].strip())
                       globalPrice= (definedVariable.lower()[definedVariable.rindex("?") + 2: ][0 : definedVariable.lower()[definedVariable.rindex("?") + 2: ].index(x) -2 ].strip())
                       print(globalPrice.strip())
                       break
              else:
                   break    
            else:
              globalPrice=definedVariable.lower()[definedVariable.rindex("?") + 2: ].strip()               



        if "limit" in update.message.text.lower():
          globalTradeType="Futures"    
        if "margin" in update.message.text.lower():
          globalTradeType="Futures"   
        if "spot" in update.message.text.lower():
          globalTradeType="Spot"   
        if "usdt" in update.message.text.lower():
           definedVariable=update.message.text.lower().replace("usdt", "?")
           if definedVariable[definedVariable.index("?") -1].isalpha()==True:
            print("kk")
           else:
             definedVariable.replace(definedVariable[definedVariable.index("?")-1], "")
             definedVariable.replace(definedVariable[definedVariable.index("?")-1], "")

        # if "usdc" in update.message.text.lower():

        # if "usd " in update.message.text.lower():

        # if "busd" in update.message.text.lower():
        # scanTrade="never"
        update.message.reply_text(text=globalTradeType + "\nEntry:-" +  globalPrice + "\nStoploss:-" + globalLoss +"\n" + "Position:-" + globalTradePosition + "\n" + "Leverage:-" + globalLeverage + "\nProfit:-" + globalProfit,
                        reply_markup=pasteTrade_keyboard())

            


















    elif verifiedUsername=="never":
      if binanceApiKey=="never":
       update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                                               Not a Valid Command





############################# Handlers #########################################
updater = Updater(os.getenv("TELEGRAM_API_KEY"), use_context=True)

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                                        Start Application
updater.dispatcher.add_handler(CommandHandler('start', start))

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                                      Link Account
updater.dispatcher.add_handler(CommandHandler('linkAccount', linkAccount))

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                                      Exit All
updater.dispatcher.add_handler(CommandHandler('exitAll', exitAll))

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                                  Main Menu
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                               Help request
updater.dispatcher.add_handler(CommandHandler('help', help))

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                               Paste request
updater.dispatcher.add_handler(CommandHandler('pasteTrade', pasteCode))

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                               Delete request
updater.dispatcher.add_handler(CommandHandler('deleteApiKey', deleteApiKey))


# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                               Sign Out
updater.dispatcher.add_handler(CallbackQueryHandler(signout_menu, pattern='signout'))
updater.dispatcher.add_handler(CallbackQueryHandler(signout, pattern='yes_signout'))
updater.dispatcher.add_handler(CommandHandler('logOut', signout_menu_link))

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                               REFRESH
updater.dispatcher.add_handler(CallbackQueryHandler(refresh_price_text_binance, pattern='refresh_price_text_binance'))


updater.dispatcher.add_handler(CallbackQueryHandler(first_menu_one, pattern='m11'))
updater.dispatcher.add_handler(CommandHandler('myAccount', first_menu_one_link))

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                          Binance Api Delete
updater.dispatcher.add_handler(CallbackQueryHandler(binanceApiDelete, pattern='binanceApiDelete'))
updater.dispatcher.add_handler(CallbackQueryHandler(yes_binanceApiDelete, pattern='yes_binanceApiDelete'))


# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                          Get Price
updater.dispatcher.add_handler(CommandHandler('getPrice', getPrice_binance_link))
updater.dispatcher.add_handler(CallbackQueryHandler(binance_price, pattern='binance_price'))
updater.dispatcher.add_handler(CallbackQueryHandler(check_again_binance_price, pattern='check_again_binance_price'))
updater.dispatcher.add_handler(CallbackQueryHandler(binance_price, pattern='getPrice_binance'))



# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                          Binance Click
updater.dispatcher.add_handler(CallbackQueryHandler(binance_menu_one, pattern='binance'))


# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                          Binance Manual Trading Check
updater.dispatcher.add_handler(CallbackQueryHandler(manualTrading_binance, pattern='manualTrading_binance'))


# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                          Binance Future Trading Check
updater.dispatcher.add_handler(CallbackQueryHandler(futures_manualTrading_binance, pattern='futures_manualTrading_binance'))


# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                          Binance Balance Check
updater.dispatcher.add_handler(CallbackQueryHandler(check_Binance_Balance, pattern='checkBalance_binance'))
updater.dispatcher.add_handler(CallbackQueryHandler(overallbalance_binance, pattern='overallbalance_binance'))
updater.dispatcher.add_handler(CallbackQueryHandler(futuresbalance_binance, pattern='futuresbalance_binance'))
updater.dispatcher.add_handler(CallbackQueryHandler(spotbalance_binance, pattern='spotbalance_binance'))



# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk #                                          SET ALERT BINANCE
updater.dispatcher.add_handler(CallbackQueryHandler(setAlert_binance, pattern='setAlert_binance'))
updater.dispatcher.add_handler(CallbackQueryHandler(day1_binance, pattern='day1_binance'))
updater.dispatcher.add_handler(CallbackQueryHandler(hour1_binance, pattern='hour1_binance'))
updater.dispatcher.add_handler(CallbackQueryHandler(hour2_binance, pattern='hour2_binance'))
updater.dispatcher.add_handler(CallbackQueryHandler(hour4_binance, pattern='hour4_binance'))
updater.dispatcher.add_handler(CallbackQueryHandler(mins30_binance, pattern='mins30_binance'))
updater.dispatcher.add_handler(CallbackQueryHandler(mins15_binance, pattern='mins15_binance'))
updater.dispatcher.add_handler(CallbackQueryHandler(mins10_binance, pattern='mins10_binance'))
updater.dispatcher.add_handler(CallbackQueryHandler(mins5_binance, pattern='mins5_binance'))







# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                          Type of Trade Margin
updater.dispatcher.add_handler(CallbackQueryHandler(cross_binance_future_trade_type, pattern='cross_binance_future_trade_type'))
updater.dispatcher.add_handler(CallbackQueryHandler(isolated_binance_future_trade_type, pattern='isolated_binance_future_trade_type'))


# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                          Type of Trade Methods
updater.dispatcher.add_handler(CallbackQueryHandler(buy_binance_future_trade_method, pattern='buy_binance_future_trade_method'))
updater.dispatcher.add_handler(CallbackQueryHandler(sell_binance_future_trade_method, pattern='sell_binance_future_trade_method'))



# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                          Market Trading
updater.dispatcher.add_handler(CallbackQueryHandler(market_buy_binance_future_trade_method, pattern='market_buy_binance_future_trade_method'))
updater.dispatcher.add_handler(CallbackQueryHandler(market_sell_binance_future_trade_method, pattern='market_sell_binance_future_trade_method'))


# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                          Limit Trading
updater.dispatcher.add_handler(CallbackQueryHandler(limit_buy_binance_future_trade_method, pattern='limit_buy_binance_future_trade_method'))
updater.dispatcher.add_handler(CallbackQueryHandler(limit_sell_binance_future_trade_method, pattern='limit_sell_binance_future_trade_method'))


# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                          Take Profit
updater.dispatcher.add_handler(CallbackQueryHandler(yes_takeprofit, pattern='yes_takeprofit'))
updater.dispatcher.add_handler(CallbackQueryHandler(no_takeprofit, pattern='no_takeprofit'))



# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                          Stop Loss
updater.dispatcher.add_handler(CallbackQueryHandler(yes_stoploss, pattern='yes_stoploss'))
updater.dispatcher.add_handler(CallbackQueryHandler(no_stoploss, pattern='no_stoploss'))


# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                          Confirm Futures Trade Binance
updater.dispatcher.add_handler(CallbackQueryHandler(confirm_binance_future_trade, pattern='confirm_binance_future_trade'))


updater.dispatcher.add_handler(CallbackQueryHandler(second_menu, pattern='m12'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu,
                                                    pattern='m1_1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu,
                                                    pattern='m2_1'))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))



if __name__ == '__main__':
  updater.start_polling()
  # url = backend_Api + "/alert"
  # response = request("GET", url)



  # sendUserId=response.json()
  # print(response.json()[4])
  # sendDuration=response.json()[4]  
  # for x in sendDuration:
  #         if x=="1day":
  #           print(response.json()[0][sendDuration.index(x)])
  #           print(response.json()[1][sendDuration.index(x)])

 