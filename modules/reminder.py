from telegram import ParseMode
from datetime import time


_help_ = '''
Use to set reminders.

*commands:*
- /reminder <minutes> <message>:Set a reminder at <HH:MM>.
- /unsetreminder: Unset existing reminder.
'''

def alert(context):
    '''send the alert message.'''
    job = context.job
    context.bot.send_message(job.context, text=msg)


def set(update, context):
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    try:
        # args[0] should contain the time for the reminder in <HH:MM>.
        indian_timezone = '+05:30'
        when = time.fromisoformat(context.args[0] + indian_timezone)
        global msg
        msg = " ".join(context.args[1:])


        # Remove old reminder and add a new one.
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(alert, when, context=chat_id)
        context.chat_data['job'] = new_job

        update.message.reply_text(f'Reminder successfully set at \
                                  {context.args[0]}!')

    except (IndexError, ValueError):
        update.message.reply_text('*Usage:* /reminder <HH:MM> <message>',
                                  parse_mode=ParseMode.MARKDOWN)


def unset(update, context):
    """Remove the job if the user changed their mind."""
    if 'job' not in context.chat_data:
        update.message.reply_text('You have no active reminder')
        return None

    job = context.chat_data['job']
    job.schedule_removal()
    del context.chat_data['job']

    update.message.reply_text('Reminder successfully unset!')

