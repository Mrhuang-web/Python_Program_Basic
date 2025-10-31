#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 学习指南：从基础类型到多态

本脚本涵盖了Python编程的核心概念，从最基础的数据类型到面向对象编程的高级特性。
每个部分都包含详细的解释和实用的代码示例，帮助你逐步掌握Python编程。
"""

import sys
import os
import math
import random
import datetime
import collections
import re
import json
import csv
import argparse

# 打印欢迎信息
print("=" * 80)
print("Python 学习指南：从基础到多态".center(70))
print("=" * 80)


def section_header(title):
    """打印章节标题"""
    print(f"\n{'=' * 80}")
    print(f"{title}".center(75))
    print(f"{'=' * 80}\n")


# 第1章：Python基础类型
section_header("第1章：Python基础类型")

print("1.1 数字类型")
print("-" * 30)

# 整数
integer_example = 42
print(f"整数: {integer_example}, 类型: {type(integer_example).__name__}")

# 浮点数
float_example = 3.14159
print(f"浮点数: {float_example}, 类型: {type(float_example).__name__}")

# 复数
complex_example = 2 + 3j
print(f"复数: {complex_example}, 类型: {type(complex_example).__name__}")

# 数学运算
print(f"\n基本运算示例:")
print(f"42 + 18 = {42 + 18}")  # 加法
print(f"42 - 18 = {42 - 18}")  # 减法
print(f"42 * 18 = {42 * 18}")  # 乘法
print(f"42 / 18 = {42 / 18}")  # 除法（返回浮点数）
print(f"42 // 18 = {42 // 18}")  # 整除
print(f"42 % 18 = {42 % 18}")  # 取模
print(f"42 ** 3 = {42 ** 3}")  # 幂运算

# math库示例
print(f"\nmath库常用函数:")
print(f"math.sqrt(16) = {math.sqrt(16)}")  # 平方根
print(f"math.pow(2, 10) = {math.pow(2, 10)}")  # 幂运算
print(f"math.pi = {math.pi}")  # 圆周率
print(f"math.e = {math.e}")  # 自然对数的底
print(f"math.sin(math.pi/2) = {math.sin(math.pi / 2)}")  # 正弦函数

print("\n1.2 字符串类型")
print("-" * 30)

# 字符串定义
string1 = "Hello"
string2 = 'World'
string3 = '''多行
字符串
示例'''

print(f"单引号字符串: {string1}")
print(f"双引号字符串: {string2}")
print(f"三引号多行字符串:\n{string3}")

# 字符串连接和格式化
print(f"\n字符串连接: {string1 + ' ' + string2}")
print(f"字符串重复: {string1 * 3}")
print(f"f-string格式化: {string1} {string2}!")
print(f"format方法: {'{} {}'.format(string1, string2)}")
print(f"旧式格式化: %s %s" % (string1, string2))

# 字符串常用方法
text = "Python Programming is FUN!"
print(f"\n字符串方法示例 (原始字符串: '{text}'):")
print(f"text.lower(): {text.lower()}")  # 转为小写
print(f"text.upper(): {text.upper()}")  # 转为大写
print(f"text.title(): {text.title()}")  # 首字母大写
print(f"text.strip(): '{text.strip()}'")  # 去除首尾空白
print(f"text.split(): {text.split()}")  # 分割字符串
print(f"' '.join(['Python', 'is', 'awesome']): {' '.join(['Python', 'is', 'awesome'])}")  # 连接字符串
print(f"'Python' in text: {'Python' in text}")  # 检查子串
print(f"text.find('Pro'): {text.find('Pro')}")  # 查找子串位置
print(f"text.replace('FUN', 'amazing'): {text.replace('FUN', 'amazing')}")  # 替换子串

# re库示例 - 正则表达式
print(f"\nre库 - 正则表达式示例:")
pattern = r'\b\w+@\w+\.\w+\b'  # 简单的邮箱正则表达式
text_with_emails = "联系我们: admin@example.com 或 support@test.org"
matches = re.findall(pattern, text_with_emails)
print(f"找到的邮箱地址: {matches}")

print("\n1.3 布尔类型")
print("-" * 30)

# 布尔值
true_value = True
false_value = False

print(f"True类型: {type(true_value).__name__}")
print(f"False类型: {type(false_value).__name__}")

# 布尔运算
print(f"\n布尔运算:")
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")
print(f"5 > 3 = {5 > 3}")
print(f"5 == 3 = {5 == 3}")

# 真值测试
print(f"\nPython中的真值测试:")
print(f"bool(0) = {bool(0)}")
print(f"bool(1) = {bool(1)}")
print(f"bool('') = {bool('')}")
print(f"bool('hello') = {bool('hello')}")
print(f"bool([]) = {bool([])}")
print(f"bool([1, 2]) = {bool([1, 2])}")
print(f"bool(None) = {bool(None)}")

print("\n1.4 None值")
print("-" * 30)

# None值表示空或无
none_value = None
print(f"None类型: {type(none_value).__name__}")
print(f"None == False: {None == False}")
print(f"None == 0: {None == 0}")
print(f"None == '': {None == ''}")

# 第2章：容器类型
section_header("第2章：Python容器类型")

print("2.1 列表 (List)")
print("-" * 30)

# 列表定义
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "two", 3.0, [4, 5]]
empty_list = []

print(f"数字列表: {numbers}")
print(f"混合列表: {mixed_list}")
print(f"空列表: {empty_list}")

# 列表索引和切片
print(f"\n列表索引和切片:")
print(f"numbers[0] = {numbers[0]}")  # 第一个元素
print(f"numbers[-1] = {numbers[-1]}")  # 最后一个元素
print(f"numbers[1:3] = {numbers[1:3]}")  # 切片 [start:end)
print(f"numbers[:3] = {numbers[:3]}")  # 前三个元素
print(f"numbers[2:] = {numbers[2:]}")  # 从第三个元素开始
print(f"numbers[::2] = {numbers[::2]}")  # 步长为2

# 列表方法
print(f"\n列表方法:")
numbers.append(6)  # 添加元素
print(f"append(6)后: {numbers}")

numbers.insert(0, 0)  # 插入元素
print(f"insert(0, 0)后: {numbers}")

numbers.remove(3)  # 删除特定值
print(f"remove(3)后: {numbers}")

popped = numbers.pop()  # 弹出末尾元素
print(f"pop()后: {numbers}, 弹出的值: {popped}")

numbers.sort(reverse=True)  # 排序
print(f"sort(reverse=True)后: {numbers}")

print(f"\n列表推导式:")
squares = [x ** 2 for x in range(1, 6)]
print(f"[x**2 for x in range(1, 6)] = {squares}")

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"[x**2 for x in range(1, 11) if x % 2 == 0] = {even_squares}")

print("\n2.2 元组 (Tuple)")
print("-" * 30)

# 元组定义（不可变序列）
tuple1 = (1, 2, 3)
tuple2 = 4, 5, 6  # 可以不加括号
empty_tuple = ()
single_element_tuple = (42,)

print(f"元组1: {tuple1}")
print(f"元组2: {tuple2}")
print(f"空元组: {empty_tuple}")
print(f"单元素元组: {single_element_tuple}")

# 元组操作（与列表类似，但不可修改）
print(f"\n元组操作:")
print(f"tuple1[0] = {tuple1[0]}")
print(f"tuple1 + tuple2 = {tuple1 + tuple2}")
print(f"tuple1 * 2 = {tuple1 * 2}")

# 元组解包
print(f"\n元组解包:")
x, y, z = tuple1
print(f"x = {x}, y = {y}, z = {z}")

# 交换变量值
print(f"\n使用元组交换变量:")
a, b = 10, 20
print(f"交换前: a = {a}, b = {b}")
a, b = b, a
print(f"交换后: a = {a}, b = {b}")

print("\n2.3 集合 (Set)")
print("-" * 30)

# 集合定义（无序、唯一元素）
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
empty_set = set()  # 注意不能用 {}

print(f"集合1: {set1}")
print(f"集合2: {set2}")
print(f"空集合: {empty_set}")

# 集合操作
print(f"\n集合操作:")
print(f"交集: {set1 & set2}")
print(f"并集: {set1 | set2}")
print(f"差集: {set1 - set2}")
print(f"对称差集: {set1 ^ set2}")

# 集合方法
print(f"\n集合方法:")
set1.add(6)
print(f"add(6)后: {set1}")

set1.remove(1)
print(f"remove(1)后: {set1}")

print(f"2 in set1: {2 in set1}")

# 集合推导式
print(f"\n集合推导式:")
squared_set = {x ** 2 for x in range(1, 6)}
print(f"{{x**2 for x in range(1, 6)}} = {squared_set}")

print("\n2.4 字典 (Dictionary)")
print("-" * 30)

# 字典定义（键值对）
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

empty_dict = {}
another_dict = dict(a=1, b=2, c=3)

print(f"人员字典: {person}")
print(f"空字典: {empty_dict}")
print(f"使用dict()创建: {another_dict}")

# 访问字典
print(f"\n访问字典:")
print(f"person['name'] = {person['name']}")
print(f"person.get('age') = {person.get('age')}")
print(f"person.get('country', 'Unknown') = {person.get('country', 'Unknown')}")  # 安全访问

# 修改字典
print(f"\n修改字典:")
person['email'] = 'alice@example.com'  # 添加键值对
print(f"添加email后: {person}")

person['age'] = 31  # 更新值
print(f"更新age后: {person}")

# 字典方法
print(f"\n字典方法:")
print(f"keys(): {list(person.keys())}")
print(f"values(): {list(person.values())}")
print(f"items(): {list(person.items())}")

# 遍历字典
print(f"\n遍历字典:")
for key, value in person.items():
    print(f"{key}: {value}")

# 字典推导式
print(f"\n字典推导式:")
squared_dict = {x: x ** 2 for x in range(1, 6)}
print(f"{{x: x**2 for x in range(1, 6)}} = {squared_dict}")

# collections库 - defaultdict示例
print(f"\ncollections.defaultdict示例:")
from collections import defaultdict

word_counts = defaultdict(int)
words = ['hello', 'world', 'hello', 'python']
for word in words:
    word_counts[word] += 1
print(f"单词计数: {dict(word_counts)}")

# collections库 - OrderedDict示例（Python 3.7+ 字典已保持插入顺序）
print(f"\ncollections.OrderedDict示例:")
from collections import OrderedDict

ordered = OrderedDict()
ordered['a'] = 1
ordered['b'] = 2
ordered['c'] = 3
print(f"有序字典: {dict(ordered)}")

# 第3章：控制流
section_header("第3章：Python控制流")

print("3.1 条件语句 (if-elif-else)")
print("-" * 30)

# if-elif-else示例
age = 25
print(f"年龄: {age}")

if age < 18:
    print("未成年")
elif 18 <= age < 65:
    print("成年人")
else:
    print("老年人")

# 嵌套条件
x = 10
y = 5
print(f"\nx = {x}, y = {y}")

if x > 0:
    if y > 0:
        print("x和y都是正数")
    else:
        print("x是正数，y不是正数")
else:
    print("x不是正数")

# 条件表达式（三元运算符）
result = "正数" if x > 0 else "非正数"
print(f"\n条件表达式: {result}")

print("\n3.2 循环语句")
print("-" * 30)

print("3.2.1 for循环")
# for循环遍历列表
print(f"遍历列表 [1, 2, 3, 4, 5]:")
for i in [1, 2, 3, 4, 5]:
    print(i, end=" ")
print()

# range函数
print(f"\n使用range(5):")
for i in range(5):
    print(i, end=" ")
print()

print(f"\n使用range(2, 10, 2):")
for i in range(2, 10, 2):
    print(i, end=" ")
print()

# 遍历字典
print(f"\n遍历字典:")
for key in person:
    print(f"{key}: {person[key]}")

# enumerate函数
print(f"\n使用enumerate:")
for index, value in enumerate(['a', 'b', 'c', 'd']):
    print(f"索引 {index}: 值 {value}")

# zip函数
print(f"\n使用zip:")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

print("\n3.2.2 while循环")
# while循环
count = 1
print(f"while循环计数到5:")
while count <= 5:
    print(count, end=" ")
    count += 1
print()

print("\n3.2.3 循环控制语句")
# break和continue
print(f"使用break:")
for i in range(1, 11):
    if i == 6:
        break
    print(i, end=" ")
print()

print(f"\n使用continue:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# else子句在循环中的使用
print(f"\n循环中的else子句:")
for i in range(1, 4):
    print(i)
else:
    print("循环正常结束")

# 无限循环示例（注释掉防止执行）
# while True:
#     user_input = input("输入'quit'退出: ")
#     if user_input.lower() == 'quit':
#         break


# 第4章：函数
section_header("第4章：Python函数")

print("4.1 函数定义与调用")
print("-" * 30)


# 基本函数定义
def greet(name):
    """这是一个简单的问候函数"""
    return f"Hello, {name}!"


print(f"函数调用: {greet('World')}")
print(f"函数文档: {greet.__doc__}")


# 无参数函数
def say_hello():
    print("Hello, Python!")


print(f"\n无参数函数调用:")
say_hello()


# 带默认参数的函数
def greet_with_default(name="Guest"):
    return f"Hello, {name}!"


print(f"\n默认参数函数:")
print(f"greet_with_default(): {greet_with_default()}")
print(f"greet_with_default('Alice'): {greet_with_default('Alice')}")

# 可变参数
print(f"\n4.2 可变参数函数")
print("-" * 30)


def sum_numbers(*args):
    """计算任意数量数字的和"""
    return sum(args)


print(f"sum_numbers(1, 2, 3) = {sum_numbers(1, 2, 3)}")
print(f"sum_numbers(1, 2, 3, 4, 5) = {sum_numbers(1, 2, 3, 4, 5)}")


# 关键字参数
def print_person_info(**kwargs):
    """打印人员信息"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print(f"\n关键字参数函数:")
print_person_info(name="Bob", age=30, city="Boston")


# 组合使用
def complex_function(arg1, arg2, *args, **kwargs):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


print(f"\n组合参数函数:")
complex_function(1, 2, 3, 4, name="Charlie", age=35)

print(f"\n4.3 作用域")
print("-" * 30)

# 全局变量
global_var = "I am global"


def function_with_scope():
    # 局部变量
    local_var = "I am local"
    print(f"局部变量: {local_var}")
    print(f"访问全局变量: {global_var}")

    # 修改全局变量需要使用global关键字
    global global_var
    global_var = "I am modified global"


print(f"调用前全局变量: {global_var}")
function_with_scope()
print(f"调用后全局变量: {global_var}")

print(f"\n4.4 内置函数")
print("-" * 30)

print(f"len([1, 2, 3, 4, 5]) = {len([1, 2, 3, 4, 5])}")
print(f"max([3, 1, 4, 1, 5, 9]) = {max([3, 1, 4, 1, 5, 9])}")
print(f"min([3, 1, 4, 1, 5, 9]) = {min([3, 1, 4, 1, 5, 9])}")
print(f"sum([1, 2, 3, 4, 5]) = {sum([1, 2, 3, 4, 5])}")
print(f"sorted([3, 1, 4, 1, 5, 9]) = {sorted([3, 1, 4, 1, 5, 9])}")
print(f"list(range(5)) = {list(range(5))}")
print(f"tuple([1, 2, 3]) = {tuple([1, 2, 3])}")
print(f"set([1, 2, 2, 3, 3, 3]) = {set([1, 2, 2, 3, 3, 3])}")
print(f"dict(a=1, b=2) = {dict(a=1, b=2)}")
print(f"str(42) = {str(42)}")
print(f"int('42') = {int('42')}")
print(f"float('3.14') = {float('3.14')}")
print(f"bool(1) = {bool(1)}")
print(f"abs(-5) = {abs(-5)}")
print(f"round(3.14159, 2) = {round(3.14159, 2)}")

print(f"\n4.5 高阶函数")
print("-" * 30)

# map函数
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"map(lambda x: x**2, [1, 2, 3, 4, 5]) = {squared}")

# filter函数
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) = {evens}")

# reduce函数（需要从functools导入）
from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
print(f"reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]) = {product}")

print(f"\n4.6 匿名函数（lambda）")
print("-" * 30)

# lambda函数
square = lambda x: x ** 2
print(f"lambda x: x**2 (5) = {square(5)}")

# 在排序中使用lambda
people = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
people_sorted_by_age = sorted(people, key=lambda person: person[1])
print(f"按年龄排序: {people_sorted_by_age}")

print(f"\n4.7 闭包")
print("-" * 30)


def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


add_five = outer_function(5)
print(f"闭包示例 - add_five(3) = {add_five(3)}")

print(f"\n4.8 装饰器")
print("-" * 30)

import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行时间: {end_time - start_time:.6f} 秒")
        return result

    return wrapper


@timer_decorator
def slow_function():
    time.sleep(0.1)
    return "完成"


print(f"装饰器示例:")
result = slow_function()
print(f"函数返回: {result}")

# 第5章：面向对象编程基础
section_header("第5章：Python面向对象编程基础")

print("5.1 类和对象")
print("-" * 30)


# 类定义
class Person:
    """人员类"""

    # 类变量
    species = "Human"

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name  # 实例变量
        self.age = age

    def greet(self):
        """问候方法"""
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def celebrate_birthday(self):
        """庆祝生日方法"""
        self.age += 1
        return f"Happy Birthday! Now I am {self.age} years old."


# 创建对象
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(f"对象创建:")
print(f"person1: {person1.name}, {person1.age} 岁")
print(f"person2: {person2.name}, {person2.age} 岁")

# 调用方法
print(f"\n方法调用:")
print(f"person1.greet(): {person1.greet()}")
print(f"person2.greet(): {person2.greet()}")
print(f"person1.celebrate_birthday(): {person1.celebrate_birthday()}")

# 访问类变量
print(f"\n类变量访问:")
print(f"Person.species: {Person.species}")
print(f"person1.species: {person1.species}")
print(f"person2.species: {person2.species}")

print(f"\n5.2 继承")
print("-" * 30)


# 父类
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

    def eat(self):
        return f"{self.name} is eating"


# 子类
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 调用父类构造函数
        self.breed = breed

    def speak(self):  # 重写父类方法
        return "Woof!"

    def fetch(self):  # 子类特有方法
        return f"{self.name} is fetching the ball"


class Cat(Animal):
    def speak(self):  # 重写父类方法
        return "Meow!"

    def purr(self):  # 子类特有方法
        return f"{self.name} is purring"


# 创建子类对象
rover = Dog("Rover", "Golden Retriever")
whiskers = Cat("Whiskers")

print(f"继承示例:")
print(f"rover.name: {rover.name}")
print(f"rover.breed: {rover.breed}")
print(f"rover.speak(): {rover.speak()}")  # 重写的方法
print(f"rover.eat(): {rover.eat()}")  # 继承的方法
print(f"rover.fetch(): {rover.fetch()}")  # 子类特有方法

print(f"\nwhiskers.name: {whiskers.name}")
print(f"whiskers.speak(): {whiskers.speak()}")  # 重写的方法
print(f"whiskers.eat(): {whiskers.eat()}")  # 继承的方法
print(f"whiskers.purr(): {whiskers.purr()}")  # 子类特有方法

print(f"\n5.3 多态")
print("-" * 30)


# 多态示例 - 同一个接口，不同实现
def animal_sound(animal):
    """接收任何Animal类型或其子类"""
    print(f"{animal.name} says: {animal.speak()}")


print(f"多态示例:")
animal_sound(rover)  # 传递Dog对象
animal_sound(whiskers)  # 传递Cat对象

# 列表中的多态
animals = [rover, whiskers]
print(f"\n遍历动物列表:")
for animal in animals:
    animal_sound(animal)

print(f"\n5.4 封装")
print("-" * 30)


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # 私有属性（以双下划线开头）

    def deposit(self, amount):
        """存款方法"""
        if amount > 0:
            self.__balance += amount
            return f"存款 {amount} 成功，当前余额: {self.__balance}"
        else:
            return "存款金额必须大于0"

    def withdraw(self, amount):
        """取款方法"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"取款 {amount} 成功，当前余额: {self.__balance}"
        else:
            return "取款金额无效或余额不足"

    def get_balance(self):
        """获取余额的公共方法"""
        return f"当前余额: {self.__balance}"


# 创建银行账户
account = BankAccount("Alice", 1000)

print(f"封装示例:")
print(f"account.owner: {account.owner}")  # 公共属性可以直接访问
# print(account.__balance)  # 尝试直接访问私有属性会引发错误
print(f"account.get_balance(): {account.get_balance()}")  # 通过方法访问
print(f"account.deposit(500): {account.deposit(500)}")
print(f"account.withdraw(200): {account.withdraw(200)}")
print(f"account.withdraw(2000): {account.withdraw(2000)}")  # 尝试超额取款

print(f"\n5.5 特殊方法")
print("-" * 30)


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """字符串表示，使用str()或print()时调用"""
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        """官方表示，直接显示对象时调用"""
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    def __len__(self):
        """长度，使用len()时调用"""
        return self.pages

    def __eq__(self, other):
        """相等性比较，使用==时调用"""
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title == other.title and
                self.author == other.author and
                self.pages == other.pages)


# 创建Book对象
book1 = Book("Python Basics", "John Smith", 300)
book2 = Book("Python Basics", "John Smith", 300)
book3 = Book("Learning Python", "Mark Johnson", 450)

print(f"特殊方法示例:")
print(f"str(book1): {str(book1)}")  # 调用__str__
print(f"repr(book1): {repr(book1)}")  # 调用__repr__
print(f"len(book1): {len(book1)}")  # 调用__len__
print(f"book1 == book2: {book1 == book2}")  # 调用__eq__
print(f"book1 == book3: {book1 == book3}")  # 调用__eq__

print(f"\n5.6 抽象类和接口")
print("-" * 30)

from abc import ABC, abstractmethod


class Shape(ABC):  # 抽象基类
    @abstractmethod
    def area(self):
        """计算面积的抽象方法"""
        pass

    @abstractmethod
    def perimeter(self):
        """计算周长的抽象方法"""
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# 创建具体形状对象
rectangle = Rectangle(5, 3)
circle = Circle(4)

print(f"抽象类示例:")
print(f"矩形面积: {rectangle.area():.2f}")
print(f"矩形周长: {rectangle.perimeter()}")
print(f"圆形面积: {circle.area():.2f}")
print(f"圆形周长: {circle.perimeter():.2f}")

# 多态应用 - 同一接口处理不同类型
shapes = [rectangle, circle]
print(f"\n遍历形状列表:")
for shape in shapes:
    print(f"面积: {shape.area():.2f}, 周长: {shape.perimeter():.2f}")

# 第6章：Python高级特性
section_header("第6章：Python高级特性")

print("6.1 模块和包")
print("-" * 30)

print(f"Python模块示例:")
print(f"当前模块名称: {__name__}")
print(f"导入的math模块: math.pi = {math.pi}")
print(f"导入的random模块: random.randint(1, 10) = {random.randint(1, 10)}")

# 文件操作示例
print(f"\n6.2 文件操作")
print("-" * 30)

# 创建一个临时文件进行演示
temp_file = "temp_example.txt"
print(f"文件操作示例 (使用临时文件: {temp_file}):")

# 写入文件
with open(temp_file, "w", encoding="utf-8") as f:
    f.write("Hello, Python!\n")
    f.write("这是Python文件操作示例。\n")
print(f"✓ 文件写入完成")

# 读取文件
print(f"\n读取文件内容:")
with open(temp_file, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 逐行读取
print(f"\n逐行读取:")
with open(temp_file, "r", encoding="utf-8") as f:
    for line in f:
        print(f"行: {line.strip()}")

# 删除临时文件
os.remove(temp_file)
print(f"✓ 临时文件已删除")

# 处理JSON
print(f"\n6.3 JSON处理")
print("-" * 30)

# JSON序列化
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Java", "C++"],
    "is_student": False
}

json_string = json.dumps(data, indent=2, ensure_ascii=False)
print(f"JSON序列化:")
print(json_string)

# JSON反序列化
json_data = json.loads(json_string)
print(f"\nJSON反序列化:")
print(f"name: {json_data['name']}")
print(f"age: {json_data['age']}")
print(f"skills: {json_data['skills']}")

# 异常处理
print(f"\n6.4 异常处理")
print("-" * 30)

print(f"基本异常处理:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("错误: 除数不能为零")

print(f"\n多异常处理:")
try:
    value = int(input("请输入一个数字: "))  # 这里使用示例值代替实际输入
    value = 42  # 示例值
    result = 10 / value
except ValueError:
    print("错误: 请输入有效的数字")
except ZeroDivisionError:
    print("错误: 除数不能为零")
else:
    print(f"计算结果: {result}")
finally:
    print("异常处理完成")

print(f"\n自定义异常:")


class NegativeNumberError(Exception):
    """自定义异常类"""
    pass


try:
    number = -5
    if number < 0:
        raise NegativeNumberError("数字不能为负数")
except NegativeNumberError as e:
    print(f"自定义异常: {e}")

# 上下文管理器
print(f"\n6.5 上下文管理器")
print("-" * 30)

# 使用with语句（文件操作就是典型的上下文管理器）
print(f"使用with语句管理资源:")
try:
    with open(temp_file, "w") as f:
        f.write("使用上下文管理器")
    print(f"✓ 文件操作成功")
except Exception as e:
    print(f"错误: {e}")


# 创建自定义上下文管理器
class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print(f"执行时间: {self.end_time - self.start_time:.6f} 秒")
        return False  # 不抑制异常


print(f"\n自定义上下文管理器示例:")
with Timer():
    time.sleep(0.1)
    print("在上下文管理器中执行操作")

# 生成器和迭代器
print(f"\n6.6 生成器和迭代器")
print("-" * 30)


# 生成器函数
def count_up_to(n):
    """生成1到n的数字"""
    i = 1
    while i <= n:
        yield i
        i += 1


print(f"生成器示例:")
generator = count_up_to(5)
print(f"next(generator): {next(generator)}")
print(f"next(generator): {next(generator)}")
print(f"剩余值: {list(generator)}")

# 生成器表达式
squares_gen = (x ** 2 for x in range(1, 6))
print(f"\n生成器表达式: {list(squares_gen)}")


# 迭代器
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


print(f"\n自定义迭代器:")
my_iterator = MyIterator([10, 20, 30, 40, 50])
for item in my_iterator:
    print(item, end=" ")
print()

# 日期和时间
print(f"\n6.7 日期和时间")
print("-" * 30)

# 当前日期和时间
current_datetime = datetime.datetime.now()
print(f"当前日期和时间: {current_datetime}")
print(f"当前年份: {current_datetime.year}")
print(f"当前月份: {current_datetime.month}")
print(f"当前日期: {current_datetime.day}")
print(f"当前小时: {current_datetime.hour}")
print(f"当前分钟: {current_datetime.minute}")
print(f"当前秒数: {current_datetime.second}")

# 格式化日期时间
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"\n格式化日期时间: {formatted_date}")

# 日期计算
tomorrow = current_datetime + datetime.timedelta(days=1)
yesterday = current_datetime - datetime.timedelta(days=1)
print(f"\n明天: {tomorrow.strftime('%Y-%m-%d')}")
print(f"昨天: {yesterday.strftime('%Y-%m-%d')}")

# 参数解析
print(f"\n6.8 命令行参数解析")
print("-" * 30)

print(f"argparse示例:")
# 创建一个简单的解析器用于演示
parser = argparse.ArgumentParser(description='示例命令行程序')
parser.add_argument('--name', type=str, help='您的姓名')
parser.add_argument('--age', type=int, help='您的年龄')

# 不实际解析参数，仅展示用法
print(f"\n用法示例:")
print(f"python script.py --name Alice --age 30")

# 总结
section_header("Python学习总结")

print("恭喜你完成了Python从基础到高级的学习！")
print("\n以下是你已经掌握的主要内容:")
print("1. 基础类型: 数字、字符串、布尔值、None")
print("2. 容器类型: 列表、元组、集合、字典")
print("3. 控制流: 条件语句、循环语句、循环控制")
print("4. 函数: 定义与调用、参数类型、作用域、高阶函数、装饰器")
print("5. 面向对象编程: 类与对象、继承、多态、封装、特殊方法")
print("6. 高级特性: 模块与包、文件操作、异常处理、上下文管理器、生成器")

print("\n内置库使用:")
print("- math: 数学运算")
print("- random: 随机数生成")
print("- datetime: 日期和时间处理")
print("- collections: 高级数据结构")
print("- re: 正则表达式")
print("- json: JSON数据处理")
print("- argparse: 命令行参数解析")

print("\n继续学习的建议:")
print("1. 练习编写小型项目")
print("2. 学习Python标准库的更多功能")
print("3. 探索流行的第三方库（如NumPy、Pandas、Django等）")
print("4. 参与开源项目")
print("5. 学习Python的最佳实践和设计模式")

print("\nHappy Python coding! 🐍")
print("=" * 80)