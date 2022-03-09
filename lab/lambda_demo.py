#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/3/9 11:10 下午
# @Author : 竹芒
# @Version：V 0.1
# @File : lambda_demo.py
# @desc : lambda 参数：操作（参数）
add = lambda x, y: x+y
print((add(3, 4)))
a = [(4, 5), (89, 1), (-9, 20), (1, 34)]
a.sort(key=lambda x: x[1])
print(a)

