#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/1/19 11:12 下午
# @Author : 竹芒
# @Version：V 0.1
# @File : slots_demo.py
# @desc : Python 不能在对象创建时直接分配一个固定量的内存来保存所有的属性。
# 因此如果你创建许多对象（成千上万个），它会消耗掉很多内存。 不过还是有一个方法来规避这个问题。
# 这个方法需要使用 __slots__ 来告诉 Python 不要使用字典，而且只给一个固定集合的属性分配空间
class SlotsClass(object):
    __slots__ = ['name', 'identify']

    def __init__(self, name, identify):
        self.name = name
        self.identify = identify

