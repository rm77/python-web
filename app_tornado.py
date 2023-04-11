# -*- coding: utf-8 -*-
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, RequestHandler, Application
from tornado.httpserver import HTTPServer
from pure_flask import app


class MainHandler(RequestHandler):
    def get(self):
        self.write("This message comes from Tornado ^_^")

tr = WSGIContainer(app)

application = Application([
    (r"/tornado", MainHandler),
    (r".*", FallbackHandler, dict(fallback=tr)),
])

#http_server = HTTPServer(application, ssl_options={'certfile': '/etc/ca.crt', 'keyfile': '/etc/ca.key'})
http_server = HTTPServer(application)

if __name__ == "__main__":
    http_server.listen(62000, address='0.0.0.0')
    IOLoop.instance().start()
