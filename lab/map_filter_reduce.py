#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/12/5 11:00 下午
# @Author : 竹芒
# @Version：V 0.1
# @File : map_filter_reduce.py
# @desc : Map 会将一个函数映射到一个输入列表的所有元素上.其定义：map(function_to_apply, list_of_inputs)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)
