"""Route paths and serve content."""


import os
from tornado import ioloop, web
from motor import MotorReplicaSetClient


from indexhandler import IndexHandler
from uptimehandler import UptimeHandler


dbConnection = os.environ.get('MONGODB_CONNECTION')
dbReplicaSet = os.environ.get('MONGODB_SET')
db = MotorReplicaSetClient(dbConnection, replicaSet=dbReplicaSet).posts


settings = {
    'debug': os.environ.get('DEBUG') in ('True', 'true', True),
    'gzip': True,
    'db': db,
    'template_path': 'social-abrah-am/templates',
}


application = web.Application([
    (r'/', IndexHandler),
    # (r'/plus/', IndexHandler),
    (r'/uptime', UptimeHandler),

    (r'/favicon.ico', web.RedirectHandler, {'url': '/img/favicon.ico'}),
    (r'/css/(.*)', web.StaticFileHandler, {'path': 'social-abrah-am/css'}),
    (r'/img/(.*)', web.StaticFileHandler, {'path': 'social-abrah-am/img'}),
    (r'/js/(.*)', web.StaticFileHandler, {'path': 'social-abrah-am/js'}),
    (r'/fonts/(.*)', web.StaticFileHandler, {'path': 'social-abrah-am/fonts'}),
], **settings)


if __name__ == '__main__':
    port = os.environ.get('PORT', 8080)
    print ''
    print '==============='
    print 'Starting server'
    print '==============='
    print 'DEBUG', settings['debug']
    application.listen(port)
    ioloop.IOLoop.instance().start()
