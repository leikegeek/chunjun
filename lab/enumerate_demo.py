#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/1/20 11:19 下午
# @Author : 竹芒
# @Version：V 0.1
# @File : enumerate_demo.py
# @desc : 枚举（enumerate）是 Python
# 它允许我们遍历数据并自动计数
for counter, value in enumerate(range(1, 100)):
    print(counter, value)

# 不只如此，enumerate 也接受一些可选参数，这使它更有用
some_list = ['apple', 'orange', 'banana', 'pear']
for c, value in enumerate(some_list, 1):
    print(c, value)
# 上面这个可选参数允许我们定制从哪个数字开始枚举。
# 你还可以用来创建包含索引的元组列表， 例如：
counter_list = list(enumerate(some_list, 1))
print(counter_list)
