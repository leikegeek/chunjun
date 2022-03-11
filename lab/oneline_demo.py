#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/3/10 8:29 上午
# @Author : 竹芒
# @Version：V 0.1
# @File : oneline_demo.py
# @desc :
# python -m http.server 起一个web服务
# cat file.json | python -m json.tool 打印格式化
from pprint import  pprint
my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
pprint(my_dict)
# python -m cProfile my_script.py 脚本性能瓶井分析
# 将cvs转化为json
# python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"
# todo
# for else 语句 当for循环完成后，会执行else里面当代码块
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')