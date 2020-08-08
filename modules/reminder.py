_help_ = '''
Use to set reminders for an interval of time.

*commands:*
- /reminder <minutes> <message>:Set a reminder.
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
        # args[0] should contain the time for the reminder in minutes.
        minutes = int(context.args[0])
        global msg
        msg = " ".join(context.args[1:])

        if minutes < 0:
            update.message.reply_text('Time can\'t be negative.')
            return None

        # Remove old reminder and add a new one.
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(alert, minutes*60, context=chat_id)
        context.chat_data['job'] = new_job

        update.message.reply_text('Reminder successfully set!')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /reminder <minutes> <message>')


def unset(update, context):
    """Remove the job if the user changed their mind."""
    if 'job' not in context.chat_data:
        update.message.reply_text('You have no active reminder')
        return None

    job = context.chat_data['job']
    job.schedule_removal()
    del context.chat_data['job']

    update.message.reply_text('Reminder successfully unset!')

