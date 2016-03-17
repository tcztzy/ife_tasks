#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.render('index.html')


class TaskHandler(RequestHandler):
    def get(self, task_id):
        self.render('task%s.html' % task_id)


handlers = [
    (r'/', IndexHandler),
    (r'/task/(\d+)/', TaskHandler),
]
