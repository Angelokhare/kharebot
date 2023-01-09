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
from requests import request
import time
import services
import re

# print(services.backend_Api)

import os #provides ways to access the Operating System and allows us to read the environment variables
load_dotenv()


  
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
    verifiedPassword="never"
    verifiedUsername="never"
    binanceApiKey="never"
    binanceApiSecret="never"
    update.message.reply_text("""Available Commands :-
    /start - To start bot 🤖 \n
    /linkAccount - To link account to bot 👌 \n
    /myAccount -To access User menu
    /deleteApiKey -To delete User api
    /logOut -To sign out \n
    /exitAll -To sign out of all Devices
    """)




############################### Bot ######################################################################################################            STARTING THE BOT
def start(update, context):

   global verifiedPassword
   global verifiedUsername
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
    verifiedPassword="never"
    binanceApiKey="never"
    binanceApiSecret="never"
    chat_id =  update.message.chat_id
    url = "https://kharebot-backend.fly.dev/id"

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
    url = "https://kharebot-backend.fly.dev/signout?globalSignout=" + str(chat_id)

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
  url = "https://kharebot-backend.fly.dev/id"

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

        query.edit_message_text("""Sorry, your Account is not linked to the Trading bot, Please click on /linkAccount to link your account. 🤖""")                                          


def first_menu_one_keyboard_one():
  keyboard = [[InlineKeyboardButton('Binance 👉', callback_data='binance')],
              [InlineKeyboardButton('Kucoin 👉', callback_data='kucoin')],
                      [InlineKeyboardButton('Back 🔙', callback_data='main')]
                    ]

  return InlineKeyboardMarkup(keyboard)

def client_keyboard_one():
  keyboard = [[InlineKeyboardButton('Check Balance 👉', callback_data='checkBalance')],
              [InlineKeyboardButton('Transfer 👉', callback_data='transfer')],
              [InlineKeyboardButton('Live Trade 👉', callback_data='liveTrade')],
              [InlineKeyboardButton('Manual Trading 👉', callback_data='manualTrading')],
              [InlineKeyboardButton('Auto Trading 👉', callback_data='autoTrading')],
              [InlineKeyboardButton('Purchase Airtime 👉', callback_data='purchaseAirtime')],
              [InlineKeyboardButton('Purchase Data 👉', callback_data='purchaseData')],
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
  url = "https://kharebot-backend.fly.dev/binance?id=" + str(chat_id)

  response = request("GET", url)

  # for info in response.json()[0]:
  print(response.text)

  if response.text=="unaunteticated" :
   binanceApiKey="ready"
   query.edit_message_text("Don't know how to get your Binance API click <a href='https://www.binance.com/en/support/faq/how-to-create-api-360002502072'>here</a>",parse_mode=ParseMode.HTML)
   query.edit_message_text("Enter your Binance API Key")
  else: 
    binanceApiKey="never" 
    query.edit_message_text(
                        text='Welcome back, ' +  response.text + "👋 \n \nHere are your offers 🔌.", 
                        reply_markup=client_keyboard_one())  






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
  url = "https://kharebot-backend.fly.dev/id"

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

          update.message.reply_text("""Sorry, your Account is not linked to the Trading bot, Please click on /linkAccount to link your account. 🤖""")                                          








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
       url = "https://kharebot-backend.fly.dev/signout?id=" + str(update.callback_query.message.chat.id)

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
  url = "https://kharebot-backend.fly.dev/id"

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

    # kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk  FOR ACCOUNT LINKING
    if verifiedUsername=="ready":

      if verifiedPassword=="ready":
        verifiedPassword="never"
        verifiedUsername="never"
        globalPassword=update.message.text.lower().strip()

        # import requests

        url = "https://kharebot-backend.fly.dev/testing?email=" + globalUsername + "&password=" + globalPassword + "&id=" + str(update.message.chat_id)

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
        globalbinanceApiSecret=update.message.text.lower().strip()

        url = "https://kharebot-backend.fly.dev/binance?binanceApiKey=" + globalbinanceApiKey + "&binanceApiSecret=" + globalbinanceApiSecret + "&idTelegram=" + str(update.message.chat_id)

        response = request("GET", url)

        print(response.text)
        update.message.reply_text(
        response.text,parse_mode=ParseMode.HTML)


        binanceApiKey="never"
        binanceApiSecret="never"

      else:
        binanceApiSecret="ready" 
        globalbinanceApiKey=update.message.text.lower().strip()
        update.message.reply_text(
        "Enter your Binance Api Secret")        

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

        # if "usdc" in update.message.text.lower():

        # if "usd " in update.message.text.lower():

        # if "busd" in update.message.text.lower():
        update.message.reply_text(globalTradeType + "\nEntry:-" +  globalPrice + "\nStoploss:-" + globalLoss +"\n" + "Position:-" + globalTradePosition + "\n" + "Leverage:-" + globalLeverage + "\nProfit:-" + globalProfit)




















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

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                                      Link Account
updater.dispatcher.add_handler(CommandHandler('exitAll', exitAll))

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                                  Main Menu
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                               Help request
updater.dispatcher.add_handler(CommandHandler('help', help))

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                               Help request
updater.dispatcher.add_handler(CommandHandler('pasteTrade', pasteCode))


# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                               Sign Out
updater.dispatcher.add_handler(CallbackQueryHandler(signout_menu, pattern='signout'))
updater.dispatcher.add_handler(CallbackQueryHandler(signout, pattern='yes_signout'))
updater.dispatcher.add_handler(CommandHandler('logOut', signout_menu_link))


updater.dispatcher.add_handler(CallbackQueryHandler(first_menu_one, pattern='m11'))
updater.dispatcher.add_handler(CommandHandler('myAccount', first_menu_one_link))

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                          Binance Click
updater.dispatcher.add_handler(CallbackQueryHandler(binance_menu_one, pattern='binance'))


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
