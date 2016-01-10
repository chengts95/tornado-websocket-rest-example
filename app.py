import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.websocket
import json

cl = []

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class SocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            cl.append(self)

    def on_close(self):
        if self in cl:
            cl.remove(self)

class ApiHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self, *args):
        self.finish()
        id = self.get_argument("id")
        value = self.get_argument("value")
        data = {"id": id, "value" : value}
        data = json.dumps(data)
        for c in cl:
            c.write_message(data)

    @tornado.web.asynchronous
    def post(self):
        pass


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
             (r'/', IndexHandler),
             (r'/ws', SocketHandler),
             (r'/api', ApiHandler),
        ]

        settings = {
            'template_path': './templates',
            'static_path': './static'
        }
        tornado.web.Application.__init__(self, handlers, **settings)
        
        
if __name__ == '__main__':
#    app.listen(8888)
#    ioloop.IOLoop.instance().start()
    
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
