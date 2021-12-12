#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/12/6 10:04 下午
# @Author : 竹芒
# @Version：V 0.1
# @File : decorators_demo.py
# @desc : 装饰器（Decorators）是修改其他函数的功能的函数

from functools import wraps
from urllib import request


def log_handler(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print('Start %s(%s, %s)...' % (func.__name__, args, kwargs))
        result = func(*args, **kwargs)
        print("return message is " + str(result))
        return result
    return with_logging


@log_handler
def add_func(x):
    return x + x


@log_handler
def remove_func(name=None, age=1):
    print("name is" + name + ", age is " + str(age))


s1 = add_func(4)
remove_func("tom", 5)
