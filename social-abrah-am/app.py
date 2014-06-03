import os
import tornado
import tornado.web
import motor


from indexhandler import IndexHandler


dbConnection = os.environ.get('MONGODB_CONNECTION')
dbReplicaSet = os.environ.get('MONGODB_SET')
db = motor.MotorReplicaSetClient(dbConnection, replicaSet=dbReplicaSet).posts


settings = {
    'debug': os.environ.get('DEBUG') in ('True', 'true', True),
    'gzip': True,
    'db': db,
    'template_path': 'social-abrah-am/templates',
}


application = tornado.web.Application([
    (r'/', IndexHandler),
    # (r'/plus/', IndexHandler),
    # (r'/uptime', IndexHandler),

    (r'/favicon.ico', tornado.web.RedirectHandler, {'url': 'https://abrah.am/favicon.ico'}),
    (r'/css/(.*)', tornado.web.StaticFileHandler, {'path': 'social-abrah-am/css'}),
    (r'/img/(.*)', tornado.web.StaticFileHandler, {'path': 'social-abrah-am/img'}),
    (r'/js/(.*)', tornado.web.StaticFileHandler, {'path': 'social-abrah-am/js'}),
    (r'/fonts/(.*)', tornado.web.StaticFileHandler, {'path': 'social-abrah-am/fonts'}),
], **settings)


if __name__ == '__main__':
    port = os.environ.get('PORT', 8080)
    print ''
    print '==============='
    print 'Starting server'
    print '==============='
    print 'DEBUG', settings['debug']
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
