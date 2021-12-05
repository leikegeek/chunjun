#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/12/5 10:21 下午
# @Author : 竹芒
# @Version：V 0.1
# @File : generators.py
# @desc :  iterable可迭代对象（Python中任意的对象，只要它定义了可以返回一个迭代器的 __iter__ 方法，
#          或者定义了可以支持下标索引的 __getitem__ 方法（这些双下划线方法会在其他章节中全面解释），那么它就是一个可迭代对象）
#          iterator迭代器（任意对象，只要定义了 next（Python2） 或者 __next__ 方法，它就是一个迭代器）
#          iteration迭代，generators生成器-->生成器也是一种迭代器，但是你只能对其迭代一次。这是因为它们并没有把所有的
#          值存在内存中，而是在运行时生成值。你通过遍历来使用它们，要么用一个 “for” 循环，
#          要么将它们传递给任意可以进行迭代的函数和结构。大多数时候生成器是以函数来实现的。
#          然而，它们并不返回一个值，而是 yield (暂且译作“生出”)一个值，生成器最佳应用场景是：
#          你不想同一时间将所有计算出来的大量结果集分配到内存当中，特别是结果集里还包含循环。
#  eg.
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


for x in fibon(100):
    print(x)


# Python内置函数next()可以获取序列代下一个元素。以下代码将在最后一行抛出StopIteration的异常，这个异常的含义是：
# 所有的值已被yield完，为什么我们在使用 for 循环时没有这个异常，因为for 循环会自动捕捉到这个异常并停止调用 next()
def generators():
    for i in range(3):
        yield i


gen = generators()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# Python内置函数iter可以根据一个可迭代对象返回一个迭代器对象,例如Python内置数据类型str就是一个可迭代对象，但是想要迭代它需要
# 先使用iter返回一个迭代器对象
var_str = "lake"
var_iter = iter(var_str)
print(next(var_iter))
