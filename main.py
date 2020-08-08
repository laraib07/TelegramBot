from telegram.ext import Updater, CommandHandler, MessageHandler, Filters , CallbackQueryHandler
import telegram.ext
import logging
import modules.init as Init
import modules.inlinehelp as Help
import modules.timer as Timer
import modules.reminder as Reminder

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


command_handler = [dict(command='start',
                        callback=Init.start),

                   dict(command='help',
                        callback=Help.help),

                   dict(command='timer',
                        callback=Timer.set,
                        pass_args=True,
                        pass_job_queue=True,
                        pass_chat_data=True),

                   dict(command='unsettimer',
                        callback=Timer.unset,
                        pass_chat_data=True),

                   dict(command='reminder',
                        callback=Reminder.set,
                        pass_args=True,
                        pass_job_queue=True,
                        pass_chat_data=True),

                   dict(command='unsetreminder',
                        callback=Reminder.unset,
                        pass_chat_data=True)]


def main():
    '''Run bot.'''
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    token = input()
    updater = Updater(token, use_context=True)

    # allow to register handler --> command, video, audio, etc
    dp = updater.dispatcher


    # adding command handlers to diapatcher
    for parameters in command_handler:
        dp.add_handler(CommandHandler(**parameters))

    dp.add_handler(CallbackQueryHandler(Help.query))
    dp.add_handler(MessageHandler(Filters.command, Init.unknown))

    # update polling
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
