from telegram.ext.updater import Updater
# from telegram import ParseMode
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
# from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import os #provides ways to access the Operating System and allows us to read the environment variables

load_dotenv()




# updater = Updater("5826929844:AAEV4U3fbdXbYrZSpY-5uVMgcPY743Qq5M8",
#                   use_context=True)
  
  
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



from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
############################### Bot ############################################
def start(update, context):




   chat_id = update.message.chat_id
   first_name = update.message.chat.first_name
   last_name = update.message.chat.last_name
   username = update.message.chat.username
   print("chat_id : {} and firstname : {} lastname : {}  username {}". format(chat_id, first_name, last_name , username))
   update.message.reply_text(main_menu_message(),
                            reply_markup=main_menu_keyboard())

def main_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard()
                        )

def first_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=first_menu_message(),
                        reply_markup=first_menu_keyboard())

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
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Link your Trading Bot 🫵🏻', callback_data='m1')],
              [InlineKeyboardButton(text='Continue on Website 💻 (Recommended)', url='https://kharetradingbot.netlify.app/login')],
              [InlineKeyboardButton('ℹ About Khare', callback_data='m3')]]
  return InlineKeyboardMarkup(keyboard)



def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
              [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
              [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message():
  return "Hello friend, Welcome to the Khare Trading Bot! ❤🎉 \n  \n With the help of our bot, you'll be able to achieve remote crypto trading 💰 with advanced trading features, developed to minimize risk and maximize profits.👌 \n \n Whether you're trading with a signal provider, on your own, or using TradingView alerts, our bot will do the heavy lifting for you. 💯 \n  \n Choose the option in main menu:     "

def first_menu_message():
  return 'Choose the submenu in first menu:'

def second_menu_message():
  return 'Choose the submenu in second menu:'



# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                                               Not a Valid Command

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                                               Not a Valid Command





############################# Handlers #########################################
updater = Updater(os.getenv("TELEGRAM_API_KEY"), use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu,
                                                    pattern='m1_1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu,
                                                    pattern='m2_1'))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
