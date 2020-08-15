from requests_html import HTMLSession
from telegram import ParseMode


_help_='''
Use to find definition of some terms.

*commands:*
- /define <words>:find definition of <words>.
'''

session = HTMLSession()

def define(update,context):
    try:
        args = '_'.join(context.args)
        if len(args) == 0:
            raise IndexError

        source = session.get('https://simple.wikipedia.org/wiki/' + args)

        if source.ok:
            definition = source.html.find('mw-content-text, p', first =True).text

        else:
            definition = 'Nothing feasible found.'

        update.message.reply_text(definition)

    except IndexError:
        update.message.reply_text('*Usage:* /define <words>',
                                  parse_mode=ParseMode.MARKDOWN)
