# /usr/bin/env python
# coding=UTF-8

# author:Benjamin
# date:2020.11.17 20:13

# python中条件语句的语法
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

# 在python2中
# raw_input()读入一行字符串
# input()会自动计算读入的内容，要读入字符串需要加''
num1, ch, num2 = raw_input().split()
num1 = int(num1)
num2 = int(num2)
ans = None

if ch == '+':
    ans = num1 + num2
elif ch == '-':
    ans = num1 - num2
elif ch == '*':
    ans = num1 * num2
elif ch == '/':
    ans = num1 / num2
print (ans)
