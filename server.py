import tornado.ioloop
import tornado.web
import db

class MainHandler(tornado.web.RequestHandler):
    def get(self, id):
        article = db.get_text(
            id)
        self.write(article[0])

def make_app():
    return tornado.web.Application([
        (r"/(.*)", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8081)
    tornado.ioloop.IOLoop.current().start()