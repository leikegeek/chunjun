#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/2/28 8:58 上午
# @Author : 竹芒
# @Version：V 0.1
# @File : introspection_demo.py
# @desc : 自省（introspection），在计算机编程领域里，是指在运行时来判断一个对象的类型的能力
import inspect

# dir返回一个列表，这列表列出一个对象所拥有的属性和方法
my_list = [1, 2, 3]
print(dir(my_list))
# type函数返回一个对象的类型
print(type([]))
# id() 函数返回任意不同种类对象的唯一ID
name = "python"
print(id(name))
# inspect 模块也提供了许多有用的函数，来获取活跃对象的信息
print(inspect.getmembers(str))
print(inspect.getdoc(str))
