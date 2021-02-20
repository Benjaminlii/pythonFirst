# /usr/bin/env python
# coding=UTF-8

# author:Benjamin
# date:2020.11.18 12：00

# Python的循环有两种：
#   for-in循环
#   这里说一下内置方法range(start, end, step)：表示在[start, end)区间内按照步长step（可选参数）生成列表。start默认为0。
for i in range(1, 101, 2):
    print ('hello', i)
#   while循环
num = 0
while num < 50:
    print ('num = %d' % num)
    num += 1
