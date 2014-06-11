

from twitter_text import Autolink


def link_text(self, text):
    '''Link text'''
    text = text.replace('\n', '<br />')
    tt = Autolink(text)
    options = {
        'url_target': '_blank',
    }
    return tt.auto_link(options)
