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
    tornado.options.parse_command_line()
    app = Application(
        handlers=handlers,
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        debug=True,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
