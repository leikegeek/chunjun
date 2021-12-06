#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/12/5 11:00 下午
# @Author : 竹芒
# @Version：V 0.1
# @File : map_filter_reduce.py
# @desc : Map 会将一个函数映射到一个输入列表的所有元素上.其定义：map(function_to_apply, list_of_inputs)
#         filter过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，符合要求即函数映射到该元素时返回值为True
#         当需要对一个列表进行一些计算并返回结果时，Reduce 是个非常有用的函数
from functools import reduce
# 使用lambda表达式配合map完成
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)


# 也可以使用匿名函数
def multiply(x):
    return x*x


def add(x):
    return x+x


funcs = [multiply, add]
for i in range(5):
    value = map(lambda x: x(i), funcs)
    print(list(value))

number_list = range(-5, 5)
less_then_zero = filter(lambda x: x % 2 == 0, number_list)
print(list(less_then_zero))

product = reduce((lambda x, y: x+y), range(0, 101))
print(product)
