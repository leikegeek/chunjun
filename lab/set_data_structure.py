#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/12/6 9:53 下午
# @Author : 竹芒
# @Version：V 0.1
# @File : set_data_structure.py
# @desc : set（集合）是一个非常有用的数据结构。它与列表（list）的行为类似，区别在于 set 不能包含重复的值

some_list = ['a', 'b', 'c', 'b', 'd', 'e', 'f', 'a']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

# 取交集
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))

# 取差集
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))
