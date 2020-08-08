'''
Script to provide basic functions.
'''

# define /start callbak function
def start(update, context) :
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Welcome sir, How may I help you?')

# define unknown command callbak function
def unknown(update, context) :
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='You entered an unknown command.')



