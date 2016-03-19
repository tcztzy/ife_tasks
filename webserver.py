#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options
from tornado.web import Application

from handlers import handlers

define("port", default=8000, help="run on the given port", type=int)


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(__file__)
    tornado.options.parse_command_line()
    settings = {
        "static_path": os.path.join(BASE_DIR, "static"),
        "template_path": os.path.join(BASE_DIR, "templates"),
        "debug": True,
    }
    app = Application(handlers=handlers, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
