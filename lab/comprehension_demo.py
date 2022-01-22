#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/1/22 11:32 下午
# @Author : 竹芒
# @Version：V 0.1
# @File : comprehension_demo.py
# @desc :
# 列表推导式格式：variable = [out_exp for out_exp in input_list if out_exp == 2]
multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)
squared = [x**2 for x in range(10)]
print(squared)
# 字典推导式
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}
print(mcase_frequency)
# 集合推导式类似于列表推导式，区别在于使用大括号
squared_c = {x**2 for x in range(10)}
print(squared_c)
