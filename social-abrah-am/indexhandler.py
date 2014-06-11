import tornado
from tornado import gen
import datetime
import time
from email import utils


from requesthandler import RequestHandler


class IndexHandler(RequestHandler):

    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        self.set_header('Expires', _expires({'minutes': 10}))

        posts = []
        db = self.settings['db']
        cursor = db.posts.find().sort('_.created', -1).limit(50)

        while (yield cursor.fetch_next):
            post = cursor.next_object()
            posts.append(post)

        context = {
            'posts': posts,
        }

        self.render('index.html', **context)


def _expires(args):
    now = datetime.datetime.now()
    later = now + datetime.timedelta(**args)
    latertuple = later.timetuple()
    latertimestamp = time.mktime(latertuple)
    return utils.formatdate(latertimestamp)
