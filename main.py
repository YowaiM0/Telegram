
import telebot  # importing a library to work with the Telegram API
import random  # importing a library to work with random
from telebot import types # importing a submodule for working with buttons
from bote import TOKEN
bot = telebot.TeleBot(TOKEN)

    # handler of the start command
@bot.message_handler(commands=['start'])
def start_command(message):
    # creating an instance of the inline keyboard
    inline_keyboard = types.InlineKeyboardMarkup()  
    buttons = []  
    
   # adding 5 buttons
    for i in range(5):  
        buttons.append(types.InlineKeyboardButton(text="🍪", callback_data=str(i)))
     
   # adding them to the keyboard
    inline_keyboard.row(*buttons) 
    bot.send_message(message.chat.id, 'What will you choose?', reply_markup=inline_keyboard)
    

# button event handler
@bot.callback_query_handler(func=lambda call: True)  
def callback_query(call):
    if call.data == str(random.randint(0, 4)):  
        bot.send_message(call.message.chat.id, 'Congratulations, you've won! 🥳 ')  # send a winning message
    else: # send a message about the loss
        bot.send_message(call.message.chat.id, 'Alas, you have lost!😿') 


if __name__ == '__main__':
    bot.infinity_polling()  
 
