#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/1/19 11:19 下午
# @Author : 竹芒
# @Version：V 0.1
# @File : collections_demo.py
# @desc :
from collections import defaultdict, Counter, deque

# defaultdict 与 dict 类型不同，你不需要检查 key 是否存在
books = (('Tang History', 'Anshi Wang'),
         ('New Tang History', 'Xiu Ouyang'),
         ('Wudai History', 'Anshi Wang'),
         ('Song History', 'Tuo Tuo'),
         ('Liao History', 'Tuo Tuo'),
         ('Yuan History', 'Ji liu')
         )
best_books = defaultdict(list)
for name, author in books:
    best_books[name].append(author)

print(best_books)

# Counter 是一个计数器，它可以帮助我们针对某项数据进行计数,以下可以统计每个人写了几本书
write_books = Counter(author for name, author in books)
print(write_books)

# deque 提供了一个双端队列，你可以从头/尾两端添加或删除元素
# 也可以限制这个列表的大小，当超出你设定的限制时，数据会从对队列另一端被挤出去（pop）
# d = deque(maxlen=30)
d = deque()
d.append(1)
d.append(2)
d.append(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)

