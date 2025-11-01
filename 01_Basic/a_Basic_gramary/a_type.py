# -*- coding:utf-8 -*-
# Copyright (c) 2025 HuangJiaJie

# 赋值,多个变量同个值,仅创建了一个整型对象,三个变量被分配到相同的内存空间
a = b = c = 1

# 赋值,多个变量多个值,创建了2个整型对象和1个字符类型,三个变量被分配到不相的内存空间[相同值就是同个地址 - 减少创建 除非超过-5:256的动态运算]
# 常量无限制,多少都会相同
e, f, g = 1, 2, "john"

# 内存地址判断
print("内存地址判断:", id(a), id(e), "\n")

# 标准类型 - Number(不可改变的数据类型,改变数字数据类型会分配一个新的对象 -- 值相同的变量都是共用同地址,除非是动态变量并超过-5:256)
h = 257
i = 0
print("内存地址跃出判断:", id(h), id(i + h), "\n")

# 标准类型 - Number 对象删除,已删除后不能再删会报错 [前置,已经 del h]
del h, i

# 标准类型 - Number(int（有符号整型 - 长整型）,float（浮点型）,complex（复数）)
A = 1
B = 1.11
C = 3e+3j
D = complex(A, B)
print(D, "\n")

# 标准类型 - String(不可变类型,字符串或串(String)由数字、字母、下划线组成 -- 值相同的变量都是共用同地址)
E = 'ABCDEFG'
F = '' + E
print("内存地址判断:", id(E), id(F), "\n")

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
      result_8, "\n")

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
      result_8, "\n")

# 标准类型 - String(运算)
cal_1 = E * 2
cal_2 = E + E
print("cal_1:", cal_1, '\n', "cal_2:", cal_2, "\n")

# 标准类型 - List(可变类型,复合数据类型的数据结构 -- 值相同的变量都地址不同,即使浅拷贝也只是内部常量相同)
List_1 = [1, "2", [3], {"4": 4}, (5,)]
List_2 = [1, "2", [3], {"4": 4}, (5,)]
List_3 = [1, "2", [3], {"4": 4}, (5,), [1, 2, 3, [4, 5]]]
List_4 = [1, "2", [3], {"4": 4}, (5,), [1, 2, 3, [4, 5]]]
List_5 = [1, 2, 3]
List_6 = ["1", "2", "3"]
List_7 = [[1, 2], [2, 3], [3, 4]]
print(id(List_1), id(List_2), "\n")

# 标准类型 - List(浅拷贝)  - 拷贝出一个新对象，内容一样但地址不同（外层地址不同,内层都是一样 - 地址相同修改变量会影响前面的变量） - 其余方式
import copy

List_copy_1 = copy.copy(List_1)
List_copy_2 = List_1[:]
List_copy_3 = list(List_1)
List_copy_4 = [i for i in List_1]
print("copy浅拷贝-方式1", id(List_copy_1), id(List_1))
print("copy浅拷贝-方式1", id(List_copy_1[2]), id(List_1[2]))
print("copy浅拷贝-方式2", id(List_copy_2), id(List_copy_2))
print("copy浅拷贝-方式2", id(List_copy_2[2]), id(List_copy_2[2]))
print("copy浅拷贝-方式3", id(List_copy_3), id(List_copy_3))
print("copy浅拷贝-方式3", id(List_copy_3[2]), id(List_copy_3[2]))
print("copy浅拷贝-方式4", id(List_copy_4), id(List_copy_4))
print("copy浅拷贝-方式4", id(List_copy_4[2]), id(List_copy_4[2]), "\n")

# 标准类型 - List(深拷贝)  - 递归拷贝所有层，地址全不同（内外层不一样-除常量,但内层对象里还有内层就还是一样 - 地址相同修改变量会影响上个变量值）
from copy import deepcopy

List_deepcopy_1 = deepcopy(List_1)
List_deepcopy_2 = deepcopy(List_3)
print("copy深拷贝-方式2之1", id(List_deepcopy_1), id(List_1))
print("copy深拷贝-方式2之1", id(List_deepcopy_1[1]), id(List_1[1]))
print("copy深拷贝-方式2之1", id(List_deepcopy_1[2]), id(List_1[2]))
print("copy深拷贝-方式2之1", id(List_deepcopy_2[-1][-1]), id(List_1[-1][-1]), "\n")

# 标准类型 - List(切片索引-正向)  [首:末:步长] - 步长默认1
List_search_1 = List_1[:]
List_search_2 = List_1[0:]
List_search_3 = List_1[:5]
List_search_4 = List_1[::1]
List_search_5 = List_1[1::2]
List_search_6 = List_1[:5:2]
List_search_7 = List_1[:1:-2]
List_search_8 = List_1[6::-2]
List_search_9 = List_1[0]
print("List_search_1:", List_search_1, '\n', "List_search_2:", List_search_2, '\n', "List_search_3:", List_search_3,
      '\n', "List_search_4:", List_search_4, '\n', "List_search_5:", List_search_5, '\n', "List_search_6:",
      List_search_6, '\n', "List_search_7:", List_search_7, '\n', "List_search_8:", List_search_8, '\n',
      "List_search_9:", List_search_9, '\n')

# 标准类型 - List(切片索引-负向)  [首:末:步长] - 首默认第一位,末默认最后位-1,步长默认1
List_search_1 = List_1[-1:]
List_search_2 = List_1[:-2]
List_search_3 = List_1[::-1]
List_search_4 = List_1[-1::-2]
List_search_5 = List_1[:-6:-2]
List_search_6 = List_1[:-1:2]
List_search_7 = List_1[-6::2]
List_search_8 = List_1[::]
List_search_9 = List_1[0]
print("List_search_1:", List_search_1, '\n', "List_search_2:", List_search_2, '\n', "List_search_3:", List_search_3,
      '\n', "List_search_4:", List_search_4, '\n', "List_search_5:", List_search_5, '\n', "List_search_6:",
      List_search_6, '\n', "List_search_7:", List_search_7, '\n', "List_search_8:", List_search_8, '\n',
      "List_search_9:", List_search_9, '\n')

# 标准类型 - List(值修改)
List_1[0] = 2
print("List值单修改:", List_1)
List_1[0:2] = 2, 3, 4
print("List值范围修改:", List_1)
List_1[0:2] = [1]
print("List值范围修改*_重点_范围只能用对象代替不能用单个常量值:", List_1)
List_1.append(0)
print("List值修改_append加最后:", List_1)
List_1.append([1, 2])
print("List值修改_append加最后:", List_1)
List_1.insert(0, [1, 2])
print("List值修改_insert加指定:", List_1)
List_1.extend([2, 3])
print("List值修改_extend加最后_自动分解出单个:", List_1)
List_1 += List_1 + List_1
print("List值修改_+相加:", List_1)
List_1 = List_1 * 2
print("List值修改_*:", List_1)
print("List原来值:", List_1, "\n")

# 标准类型 - List(值删除)
del List_1[-1:-4:-1]
print("List值删除_del_移除范围:", List_1)
del List_1[-1]
print("List值删除_del_移除单个:", List_1)
List_1.remove([1, 2])
print("List值删除_remove_移除首个指定值:", List_1)
List_1.pop()
print("List值删除_pop_默认移除最后:", List_1)
List_1.pop(0)
print("List值删除_pop_移除指定位置:", List_1)
print("List原来值:", List_1)
List_1.clear()
print("List值删除_clear_清空所有:", List_1, "\n")

# 标准类型 - List(列表比较)
import operator

print("List列表比较_operator_列表内部对象_元素值和顺序:", operator.eq(List_3, List_4))
print("List列表比较_==:", List_3 == List_4)
print("List列表比较_id_列表地址:", id(List_3), id(List_4))
print("List列表比较_operator:", operator.eq(List_1, List_2))
print("List列表比较_==:", List_1 == List_2)
print("List列表比较_id:", id(List_1), id(List_2), "\n")

# 标准类型 - List(列表方法)
print("List_max_最大值_仅支持列表都是同个类型", max(List_5), max(List_6), max(List_7))
print("List_min_最小值_仅支持列表都是同个类型", min(List_5), min(List_6), min(List_7))
print("List_len_长度", len(List_7))
print("List_count_统计某个元素", List_5.count(1))
print("List_reverse_反向元素_不返回", List_5.reverse(), List_5)
print("List_sort_排序元素_默认降序_不返回", List_5.sort(), List_5)
