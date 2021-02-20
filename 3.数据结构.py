# /usr/bin/env python
# coding=UTF-8

# author:Benjamin
# date:2020.11.17 21:02

# list 列表
print ('==================== list ====================')
# 相当于Java中的ArrayList，但这里是语言原生支持的。
listA = [1, 2, 3, 'a', 'b', 'c', 10.0, True]
for one in listA:
    print (one)
# 列表推导
# 基本格式：
# list = [out_exp_res for out_exp in input_list if out_exp == 2]
#   out_exp_res：列表生成元素表达式，可以是有返回值的函数。
#   for out_exp in input_list：迭代input_list将out_exp传入out_exp_res表达式中。
#   if out_exp == 2：根据条件过滤哪些值可以。
print ([i for i in range(10) if i % 2 == 0])

# tuple元组
print ('==================== tuple ====================')
# 就是不可变的列表，在使用中尽量使用tuple代替list以保证安全
tupleA = (1, 2, 3, 4, 5)
print (type(tupleA))
# 元组推导
# 基本格式：
# tuple = (out_exp_res for out_exp in input_list if out_exp == 2)
generatorB = (i for i in range(10) if i % 2 == 0)
print (type(generatorB))
# 这里得到的是一个生成器，可以通过遍历访问内部元素
# 如果我们想要使用元组推导式获得新元组或新元组中的元素，有以下三种方式：
#   使用 tuple() 函数，可以直接将生成器对象转换成元组，例如：
print (tuple(generatorB))
#   直接使用 for 循环遍历生成器对象，可以获得各个元素，例如：
for num in generatorB:
    print (num)
#   使用 __next__() 方法遍历生成器对象，也可以获得各个元素，例如：
#   注意，无论是使用 for 循环遍历生成器对象，还是使用 __next__() 方法遍历生成器对象，遍历后原生成器对象将不复存在，这就是遍历后转换原生成器对象却得到空元组的原因。
a = (x for x in range(3))
print(a.next())
print(a.next())
print(a.next())
a = tuple(a)
print('转换后的元组：%s' % str(a))

# dic字典
print ('==================== dic ====================')
# 相当于伪随机探测再散列实现的map，只有可哈希的对象才能作为字典的键
dic = {'name': 'benjamin', 'age': 21, 'birthday': '7.17'}
# 遍历方法
print ('使用key遍历：')
for key in dic:
    print ('key = %s, val = %s' % (key, dic[key]))

print ('使用value遍历：')
for val in dic.values():
    print ('val = %s' % val)

print ('使用item遍历key和val：')
for key, val in dic.items():
    print ('keu = %s, val = %s' % (key, val))

print ('使用item遍历：')
for item in dic.items():
    print ('key = %s' % item[0])
# 缺陷：因为是哈希存储的数据结构，所以内部数据无序
# python 标准库的collections模块提供了名为OrderedDict的有序字典，相当于Java中的TreeMap
# 字典推导
# 基本格式：
# dir = { key_expr: value_expr for value in collection if condition }
print ({key: val for key, val in dic.items() if key != 'birthday'})

# set集合
print ('==================== set ====================')
# python的内置集合类型有两种：
#   set(): 一种可变的、无序的、有限的集合，其元素是唯一的、不可变的（可哈希的）对象。
#   frozenset(): 一种不可变的、可哈希的、无序的集合，其元素是唯一的，不可变的哈希对象。
# 要创建一个set，需要提供一个list作为输入集合：
print ({1, 2, 3, 4, 5, 5, 5, 5})
# 集合推导
# 集合推导式跟列表推导式也是类似的。 唯一的区别在于它使用大括号{ }。
# 基本格式：{ expr for value in collection if condition }
print ({num ** 2 for num in [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9] if num < 5})
