# /usr/bin/env python
# coding=UTF-8

# author:Benjamin
# date:2020.11.18 14:34

# python中的函数和其他编程语言中的函数含义大致一样
# 这里只讨论不同点

# 1. python中解释器自身就提供了很多函数，被称为内置函数
# 例如：abs(),input(),range()等等，这些都是内置函数，可以在程序中直接使用。不需要from-input
print (abs(-100))


# 2. 函数的语法:
# def 函数名(参数列表):
#     //实现特定功能的多行代码
#     [return [返回值]]
# 使用*name作为参数可以将当前位置和后面的所有参数都认为成一个元组，从而实现可变参数
# *相当于把数据结构打散传入，那么在进行调用的时候也可以通过*将一个数据结构打散成多个单个元素
def get_sum(*nums):
    ans = 0
    for i in range(len(nums)):
        ans += nums[i]
    return ans


print get_sum(1, 2, 3, 4, 5)
print get_sum(*[num for num in range(101) if num % 2 == 0])


# 使用**name则可以传入一个dic，那么调用时就需要按照键值对的形式传入
def get_people(name, age, **other):
    one = {'name': name, 'age': age}
    if 'birthday' in other:
        one['birthday'] = other['birthday']
    if 'school' in other:
        one['school'] = other['school']
    return one


print get_people('benjamin', 21)
print get_people('benjamin', 21, birthday='0717')
print get_people('benjamin', 21, birthday='0717', firstname='lee')


# python中的函数可以有0至多个返回值，相当于返回了一个tuple
def swap(num1, num2):
    return num2, num1


print (swap(1, 2))


# python中的参数支持默认值的设置
# 需要注意：默认参数需要放在最后
def power(number, n=2):
    ans = 1
    while n > 0:
        ans *= number
        n -= 1

    return ans


print (power(2))
print (power(2, 3))


# 在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

# 如果想定义一个没有任何功能的空函数，可以使用 pass 语句作为占位符。
def method():
    pass
