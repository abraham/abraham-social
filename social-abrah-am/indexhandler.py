import tornado
from tornado import gen
import datetime
import time
from email import utils
from views import link_text

from requesthandler import RequestHandler


class IndexHandler(RequestHandler):

    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        self.set_header('Expires', _expires({'minutes': 10}))

        posts = []
        db = self.settings['db']
        query = {'_.ns': {'$in': ['twitter', 'github', 'stackexchange:answers', 'plus']}}
        cursor = db.posts.find().sort('_.created', -1).limit(100)

        while (yield cursor.fetch_next):
            doc = cursor.next_object()
            posts.append(doc)

        context = {
            'posts': posts,
            'cover': 'https://lh3.googleusercontent.com/-V7-W-a_teII/U6Rr7LNirfI/AAAAAAADBJQ/EqZjztIDjJI/s2520-fcrop64=1,00002776ffffffa8/Sunny_Mountains.jpg',
            'avatar': 'https://lh4.googleusercontent.com/-6LBE-Jve_ls/AAAAAAAAAAI/AAAAAAAC8qM/9bpLLGd_FlY/photo.jpg?sz=240'
        }

        self.render('index.html', **context)


def _expires(args):
    now = datetime.datetime.now()
    later = now + datetime.timedelta(**args)
    latertuple = later.timetuple()
    latertimestamp = time.mktime(latertuple)
    return utils.formatdate(latertimestamp)
