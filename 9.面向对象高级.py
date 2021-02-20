#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author:Benjamin
# date:2020.11.18 21:06

# 使用__slots__
# 在类内部定义__slots__属性为一个字符串元组可以限制类的属性
class Student(object):
    __slots__ = ('name', 'age')


student = Student()


# student.score = 100

# 使用@property
# 在python中使用set_xxx()或者get_xxx()方法对属性进行操作灵活性不如直接对属性进行操作，但直接操作属性有会有安全问题。
# python提供了@property来将一个与方法变成属性，直接取属性就可以转化为调用方法进行get
# 相应的，提供了@xxx.setter装饰器来代替set方法
class People(object):
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError('age must be an integer!')
        elif age < 0 or age > 150:
            raise ValueError('age must between 0 ~ 150!')
        self._age = age


people = People(120)
print (people.age)


# 多继承
# python支持多继承，在类名后面的小括号中添加多个父类名即可

# 定制类
# 之前了解了__slots__这种形如__xxx__的方法或属性的作用
# 还有很多类似的用法
# __str__(self):相当于Java中的toString()方法
# __iter__(self):如果想通过for-in迭代该对象，则需要在__iter__(self)方法中返回该对象本身，
# 并且需要提供一个next(self)方法返回迭代得到的每一个过程量，直到遇到StopIteration错误时退出循环（即在外部进行迭代的循环）
# __getitem__(self, n):如果要将对象按照list一样使用[]根据下标随机访问，需要提供__getitem__(self, n)方法返回sub下表处的元素。
# 如果要处理切片，则需要对n参数进行类型判断
# __getattr__(self, attr):当查找属性时，如果没有找到，就会尝试去__getattr__(self, attr)方法中寻找
# 要让class只响应特定的几个属性，需要在其他的情况下抛出AttributeError的错误，否则会默认返回None
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path


# 类似链表的结构，每一个Chain对象在访问不存在的属性时，都会创造新的chain对象封装一段属性名
# 并通过str进行拼接
chain = Chain().status.user.timeline.list
print (chain)
print (type(chain))

# __call__(self):直接将对象本身作为方法执行时会调用该方法
