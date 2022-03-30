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
# open 的返回值是一个文件句柄，从操作系统托付给你的 Python 程序。一旦你处理完文件，你会想要归还这个文件句柄，只有这样你的程序不会超出一次能打开的文件句柄的数量上限。
# 显式地调用 close 关闭了这个文件句柄，但前提是只有在 read 成功的情况下。如果有任意异常正好在 f = open(...) 之后产生，f.close() 将不会被调用（取决于 Python
# 解释器的做法，文件句柄可能还是会被归还，但那是另外的话题了）。为了确保不管异常是否触发，文件都能关闭，我们将其包裹成一个 with 语句:
# open 的第一个参数是文件名。第二个（mode 打开模式）决定了这个文件如何被打开。
# 如果你想读取文件，传入 r；
# 如果你想读取并写入文件，传入 r+；
# 如果你想覆盖写入文件，传入 w；
# 如果你想在文件末尾附加内容，传入 a；
with open('photo.jpg', 'r+') as f:
    jpgdata = f.read()
