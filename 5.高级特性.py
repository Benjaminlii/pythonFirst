# /usr/bin/env python
# coding=UTF-8

# author:Benjamin
# date:2020.11.18 15:47

# 1. 切片
# 如果想取某一个list或者tuple中但某一段可以使用多种方式做到，python提供切片去完成。
# 使用listName[start:end:step]可以对list按照制定对规则进行切片，规则同range函数
# start默认为0，end默认为len(list)，step默认为1
listA = range(0, 20)
print (listA)
print (listA[5:10])
print (listA[5:15:3])
print (listA[::3])
print (listA[-1:0:-1])

# 2. 生成器
# 通过列表生成式，我们可以直接创建一个列表。
# 但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，占用很大的存储空间。
# 如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。

# 创建一个生成器：
# 元组的推导式生成的就是一个生成器
generatorA = (num for num in range(10) if num % 2 == 0)
for num in generatorA:
    print (num)


# 自定义函数生成器
# yield关键字可以使函数返回一个生成器，每次调用生成器next方法或者迭代生成器时都会运行这个函数直到遇到下一个yield关键字
# 生成器会返回yield关键字后的变量作为返回值
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


for i in fib(10):
    print (i)
