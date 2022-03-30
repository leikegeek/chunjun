#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/3/30 9:36 下午
# @Author : 竹芒
# @Version：V 0.1
# @File : yield_demo.py
# @desc : ield 的用法有以下四种常见的情况：
# 一个是生成器，
# 二是用于定义上下文管理器，
# 三是协程，
# 四是配合 from 形成 yield from 用于消费子生成器并传递消息。
# 这四种用法，其实都源于 yield 所具有的暂停的特性，也就说程序在运行到 yield 所在的位置 result = yield expr 时，
# 先执行 yield expr 将产生的值返回给调用生成器的 caller，然后暂停，等待 caller 再次激活并恢复程序的执行。
# 而根据恢复程序使用的方法不同，yield expr 表达式的结果值 result 也会跟着变化。如果使用 __next()__ 来调用，
# 则 yield 表达式的值 result 是 None；如果使用 send() 来调用，则 yield 表达式的值 result 是通过 send 函数传送的值
#

def grep(pattern):
    print("search for ", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


search = grep('lake')
next(search)
search.send("I love you")
search.send("who is lake")
search.send("nobody")


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1


for n in fab(10):
    print(str(n)+'\n')
