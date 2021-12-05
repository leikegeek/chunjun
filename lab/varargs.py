#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/12/5 10:06 下午
# @Author : 竹芒
# @Version：V 0.1
# @File : varargs.py
# @desc : *args用于传不定个数的参数，args并不是规定死的，换成 *var可以。
#         *kwargs用于传不定个数的键值对的参数，kwargs同上可以换。
#         标准参数与以上可变参数同时使用的时候的顺序为：demo_func(var, *args, **kwargs)
#         常用于函数装饰器

def lab_args(args_1, args_2, args_3):
    print("args:", args_1)
    print("args:", args_2)
    print("args:", args_3)


args = ("abc", 1, 3)
lab_args(*args)
kwargs = {"args_1": "abc", "args_3": 1, "args_2": 2}
lab_args(**kwargs)
