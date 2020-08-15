from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
import importlib


'''
Script to aadd  inline help for Bot.
'''

def help(update,context):
    keyboard = [[InlineKeyboardButton('timer', callback_data='timer'),
                 InlineKeyboardButton('reminder', callback_data='reminder')],

                [InlineKeyboardButton('find', callback_data='dictionary'),
                 InlineKeyboardButton('define', callback_data='wiki')]]


    reply = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose: ', reply_markup=reply)


def query(update, context):
    query = update.callback_query
    query.answer()
    get_help = importlib.import_module('modules.' + query.data)
    query.edit_message_text(text=get_help._help_,
                            parse_mode=ParseMode.MARKDOWN)

