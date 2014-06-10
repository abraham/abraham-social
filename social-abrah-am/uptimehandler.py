"""Handle checking if the app is functioning ok."""

from tornado import gen, web
from requesthandler import RequestHandler


class UptimeHandler(RequestHandler):

    @web.asynchronous
    @gen.coroutine
    def get(self):
        self.write('OK')
        self.finish()
