# /usr/bin/env python
# coding=UTF-8

# author:Benjamin
# date:2020.11.18 17:06

# 1.高阶函数
# python中将能传入函数的函数称为高阶函数。
# map()函数能接收一个函数和一个序列，返回的结果是将序列中每一个元素按照传入函数进行运算之后的结果组成的序列。
def fun1(num):
    return num ** 2


print (map(fun1, [1, 2, 3, 4, 5]))


# reduce()函数可以对传入序列的每一个元素进行累积计算
def fun2(num1, num2):
    return num1 * 10 + num2


print (reduce(fun2, [1, 2, 3, 4, 5]))


# filter()函数具有过滤功能，传入一个函数和一个序列，按照对每一个序列进行函数计算的结果的返回值是True还是False进行判断是否保留该元素。
def fun3(num):
    return num % 2 == 0


print (filter(fun3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# sorted()函数用于列表排序，接收一个列表和一个比较函数
# 比较函数接收两个数值，如果需要交换两个元素的位置，返回正数
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


print sorted([36, 5, 12, 9, 21], reversed_cmp)


# 2. 函数作为返回值与闭包
# python中函数的返回值也可以是函数
def get_fun1():
    def my_fun1(a, b):
        return a + b

    return my_fun1


fun1 = get_fun1()
print (fun1(1, 2))


# 返回的函数中可以随意的使用外层函数中的变量，这种函数和外部变量座椅一个整体存在的结构被称为闭包
def get_fun2(num1, num2):
    def my_fun2():
        return num1 + num2

    return my_fun2


fun2 = get_fun2(2, 3)
print (fun2())


# 闭包中使用外层函数中的变量是通过引用去访问的，所以在生成一个闭包后，如果外层函数中的变量值发生了变化，那么之前的闭包会使用新的值进行计算。
def get_fun3():
    num = 1

    def my_fun3():
        return num ** 2

    fun3_1 = my_fun3
    num += 1
    fun3_2 = my_fun3
    num += 1
    fun3_3 = my_fun3
    return fun3_1, fun3_2, fun3_3


fun3_1, fun3_2, fun3_3 = get_fun3()
print (fun3_1(), fun3_2(), fun3_3())

# 3. 匿名函数
# 相当于Java中的lambda表达式
print (map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 4. 装饰器 decorator
# 功能上相当于代理
# 本质上，decorator就是一个返回函数的高阶函数。
# 首先创建一个装饰器
def log(func):
    def wrapper(*args, **kw):
        print 'before'
        ans = func(*args, **kw)
        print 'after'
        return ans

    return wrapper


# 通过@装饰给一个方法就可以在不该动原有代码的基础上增加功能
@log
def func():
    print ('do something')


func()
