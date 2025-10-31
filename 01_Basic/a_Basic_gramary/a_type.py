# -*- coding:utf-8 -*-
# Copyright (c) 2025 HuangJiaJie

# 赋值,多个变量同个值,仅创建了一个整型对象,三个变量被分配到相同的内存空间
a = b = c = 1

# 赋值,多个变量多个值,创建了2个整型对象和1个字符类型,三个变量被分配到不相的内存空间[相同值就是同个地址 - 减少创建 除非超过-5:256的动态运算]
# 常量无限制,多少都会相同
e, f, g = 1, 2, "john"

# 内存地址判断
print("内存地址判断:", id(a), id(e))

# 标准类型 - Number(不可改变的数据类型,改变数字数据类型会分配一个新的对象 -- 值相同的变量都是共用同地址,除非是动态变量并超过-5:256)
h = 257
i = 0
print("内存地址跃出判断:", id(h), id(i + h))

# 标准类型 - Number 对象删除,已删除后不能再删会报错 [前置,已经 del h]
del h, i

# 标准类型 - Number(int（有符号整型 - 长整型）,float（浮点型）,complex（复数）)
A = 1
B = 1.11
C = 3e+3j
D = complex(A, B)
print(D)

# 标准类型 - String(不可变类型,字符串或串(String)由数字、字母、下划线组成 -- 值相同的变量都是共用同地址)
E = 'ABCDEFG'
F = '' + E
print("内存地址判断:", id(E), id(F))

# 标准类型 - String(正向索引)  [首:末:步长]
result_1 = E[0:]
result_2 = E[:5:2]
result_3 = E[0:6]
result_4 = E[0:6:1]
result_5 = E[0:6:2]
result_6 = E[6:1:-1]
result_7 = E[:1:-2]
result_8 = E[6::-2]
print("result_1:", result_1, '\n', "result_2:", result_2, '\n', "result_3:", result_3, '\n', "result_4:", result_4,
      '\n', "result_5:", result_5, '\n', "result_6:", result_6, '\n', "result_7:", result_7, '\n', "result_8:",
      result_8)

# 标准类型 - String(反向索引)  [首:末:步长]
result_1 = E[-1:]
result_2 = E[:-1:1]
result_3 = E[-6:-1]
result_4 = E[-6:-1:1]
result_5 = E[-6:-1:2]
result_6 = E[-1:-6:-1]
result_7 = E[:-6:-2]
result_8 = E[-1::-2]
print("result_1:", result_1, '\n', "result_2:", result_2, '\n', "result_3:", result_3, '\n', "result_4:", result_4,
      '\n', "result_5:", result_5, '\n', "result_6:", result_6, '\n', "result_7:", result_7, '\n', "result_8:",
      result_8)

# 标准类型 - String(运算)
cal_1 = E * 2
cal_2 = E + E
print("cal_1:", cal_1, '\n', "cal_2:", cal_2, )

# 标准类型 - List(可变类型,复合数据类型的数据结构 -- 值相同的变量都地址不同,即使浅拷贝也只是内部常量相同)
List_1 = [1, "2", [3], {"4": 4}, (5,)]
List_2 = [1, "2", [3], {"4": 4}, (5,)]
print(id(List_1),id(List_2))

# 标准类型 - List(浅拷贝)
from copy import deepcopy
List_3 = deepcopy(List_2)
print(id(List_3),id(List_2))
