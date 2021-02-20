#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author:Benjamin
# date:2020.11.18 21:06

# 面向对象的含义不多做赘述
# 类和实例：
# class关键字后面表示类名，在后面的括号中表示该类继承自那个类，也就是这个类的父类。
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)


# 随后就可以实例化出一个实例对象
student = Student('benjamin', 100)
# 可以自由地给一个实例变量绑定属性
student.name = 'Benjamin'


# __init__方法规定了这个类在实例化时必须具备的属性，其中self参数解释器会自行传入。
# 这里相当于构造方法

# 访问限制：
# print_score()方法是一个成员方法
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，这里的限制是解释器将__name在解释之前变成了_className_name

# 方法：
# 成员方法：类中的普通方法都是成员方法，第一个参数需要是self，在方法内部通过self访问对象的属性或者其他方法
# 类方法：通过使用@classmethod进行修饰来做到，方法需要一个入参为class对象，可以访问类属性（即在类中直接书写的属性）
# 静态方法：通过@staticmethod进行定义，仅仅提供函数功能，不能访问实例属性或类属性
class TestMethod(object):
    field = 'field'

    def __init__(self):
        self._value = 'value'

    # 实例方法
    def obj_method(self):
        print(self._value)

    # 类方法
    @classmethod
    def class_method(cls):
        print (cls.field)

    # 静态方法
    @staticmethod
    def static_method():
        print (1)


test_method = TestMethod()
test_method.obj_method()
test_method.class_method()
test_method.static_method()

# 继承和多态:
# python中的继承可以继承父类的一切，而多态和Java中实现方式一致

# 获取对象信息:
# type(obj)可以得到对象的类型
print (type('abc') == type('xyz'))
# isinstance(obj, Object)可以判断obj对象是否是Object类型
# dir(obj):可以得到obj对象的所有属性组成的一个list
print (dir(student))
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
# 所以，下面的代码是等价的：
print (len('ABC'))
print ('ABC'.__len__())
# 那么我们自己写的类中如果也想使用len之类的方法，就可以自定义__len__()方法
# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
# hasattr()方法
print (hasattr(student, 'name'))
setattr(student, 'name', 'ben')
print (getattr(student, 'name'))
print (student.name)
