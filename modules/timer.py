_help_ = '''
Use to set a timer.

*commands:*
- /timer <seconds>:Set a timer.
- /unsettimer: Unset existing timer.
'''

def alert(context):
    '''send the alert message.'''
    job = context.job
    context.bot.send_message(job.context, text='Beep!')


def set(update, context):
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    try:
        # args[0] should contain the time for the timer in seconds
        seconds = int(context.args[0])

        if seconds < 0:
            update.message.reply_text('Time can\'t be negative.')
            return None

        # Remove old timer and add a new one.
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(alert, seconds, context=chat_id)
        context.chat_data['job'] = new_job

        update.message.reply_text('Timer successfully set!')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /timer <seconds>')


def unset(update, context):
    """Remove the job if the user changed their mind."""
    if 'job' not in context.chat_data:
        update.message.reply_text('You have no active timer')
        return None

    job = context.chat_data['job']
    job.schedule_removal()
    del context.chat_data['job']

    update.message.reply_text('Timer successfully unset!')

