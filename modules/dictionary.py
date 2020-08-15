from requests_html import HTMLSession
from telegram import ParseMode


_help_='''
Use to find meanings of english word.

*commands:*
- /find <word>:find meaning of <word>.
'''

session = HTMLSession()
separator = '\n\n'

def find(update,context):
    try:
        source = session.get(f'https://www.merriam-webster.com/dictionary/{context.args[0]}')
        if source.ok:
            # Finding meaning of <word>
            meanings = source.html.find('#dictionary-entry-1', first =True).text
            result = separator.join(meanings.split('\n'))

            # checking synonyms of <word>
            synonyms = source.html.find('.mw-list',first=True)
            if bool(synonyms):
                synonyms = synonyms.text.split('\n')
                # Appending synonmys to result
                result += separator + '*Synonyms : *' + ' '.join(synonyms)

        else:
            meanings = source.html.find('.spelling-suggestion',first=True).text
            result = ("The word you've entered isn't in the dictionary."
                      "Try with spelling suggestion given below.\n\n")
            result += separator.join(meanings.split('\n')[2:])

        update.message.reply_text(result,
                                  parse_mode=ParseMode.MARKDOWN)

    except IndexError:
        update.message.reply_text('*Usage:* /find <word>',
                                  parse_mode=ParseMode.MARKDOWN)

