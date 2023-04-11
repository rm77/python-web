from gevent.pywsgi import WSGIServer
from pure_flask import app

http_server = WSGIServer(('', 62000), app)
http_server.serve_forever()

