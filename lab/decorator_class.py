#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/12/12 10:53 下午
# @Author : 竹芒
# @Version：V 0.1
# @File : decorator_class.py
# @desc :

class LogHandler(object):
    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + ' was called'
        print(log_string)
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')
        self.notify()
        return self.func(*args)

    def notify(self):
        pass


class EmailLog(LogHandler):
    def __init__(self, func=None, email='test@test.com', *args, **kwargs):
        self.email = email
        super(EmailLog, self).__init__(func, *args, **kwargs)

    def notify(self):
        print('send a email')


@EmailLog
def func1():
    pass


func1()

