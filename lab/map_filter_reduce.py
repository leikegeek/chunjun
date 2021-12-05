#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/12/5 11:00 下午
# @Author : 竹芒
# @Version：V 0.1
# @File : map_filter_reduce.py
# @desc : Map 会将一个函数映射到一个输入列表的所有元素上.其定义：map(function_to_apply, list_of_inputs)

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

