# --*-- coding: utf-8 --*--
"""
    typing
        用于静态代码中捕获异常,黄色波浪线提示,会有对应的类型问题(但必须按照下面的格式书写才有 - 变量:类型   函数->类型)

        结合注意：
            单独typing结合类型注解,只是提示作用
            结合mypy - 那么运行需要在终端执行 mypy xxx.py  -- 才能在执行时报类型错误
            结合typeguard - 则是根据装饰器进行运行时判断(一般使用typing+类型注解就可以了,不需要再运行期间再校验)

    collections(多理解 - 很重要)
        标注可调用对象-给函数/方法/lambda 等“能被调用”的东西加上类型注解，让IDE 知道(变量里存的是一个函数,接受哪些参数、返回什么类型)
        可以理解为函数类型别名 - 限制传入的函数[仅指定输入类型和返回类型] - 与typing相比,层次不一样,这个是专门用于函数类型
        补充知识：
            回调、钩子、策略模式、依赖注入 & 可测试性、高阶函数、并行 & 异步框架

    区分：
        typing：List, Dict, Optional 等其他类型的数据类型注释 标签别名，为原类型的别名(或新类型)，底层类型不变，可以与原类型互操作 - 数据
        Callable：一个标签，上面写着：“这是个函数”的函数类型注释，指定了这个函数的参数和返回值类型 - 行为/函数(装饰器时不能带参)
    共同点：
        均可用于函数参数、返回值、变量等的类型注解
"""
from typing import List, NewType
from typeguard import typechecked
from collections.abc import Callable

Inter = List[int]
Length = NewType("Length", int)
Width = NewType("Width", Length)
collections_1 = Callable[int, int]


@typechecked
def surface_area(edge_length: float) -> float:
    return edge_length


print("输入为int,输出为str-不按规则会有黄色波浪线提示_且报错:", surface_area(5.0), "\n")


@typechecked
def surface_area_alias(edge_length: Inter) -> Inter:
    return edge_length


print(
    "Inter = List[int]-定义原类型别名_相互等价_Inter_使用原类型List(int)-不按规则会有黄色波浪线提示_且报错:",
    surface_area_alias([1, 2]), "\n")


@typechecked
def surface_area_new(edge_length: Length) -> Length:
    return edge_length


print(
    "NewType(‘Length’, int)-定义新类型_相当于子类型_Length_使用必须Length(value)而非原类型-不按规则会有黄色波浪线提示_且报错:",
    surface_area_new(Length(1)))
print(
    "NewType(‘Width’, Length)-新类型上再定义_相当于子类型_Width_底层还是原来类型,可与原类型运算-不按规则会有黄色波浪线提示_且报错:",
    surface_area_new(Width(1) + Length(1) + 1))
print(
    "定义新类型_相当于子类型_Length_底层还是原来类型,可与原类型运算-不按规则会有黄色波浪线提示_且报错:",
    surface_area_new(Length(1)), "\n")


@typechecked
def collections_func(func: collections_1) -> int:
    return func(1)


@typechecked
def collections_func_quote(number: int) -> int:
    return number + 1


print(
    "collections_1 = Callable[int, int]-可调用对象标注-函数类型别名_即collections_1接收一个int类型,返回int类型的函数_只传名",
    collections_func(collections_func_quote))
print(
    "collections_1 = Callable[int, int]-可调用对象标注-函数类型别名_即collections_1接收一个int类型,返回int类型的函数_lambda包装",
    collections_func(lambda x: x + 1))
print(
    "collections_1 = Callable[int, int]-可调用对象标注-函数类型别名_即collections_1接收一个int类型,返回int类型的函数_lambda包装",
    collections_func(lambda x: x + collections_func_quote(1)))
print("collections_1 = Callable[int, int]-回调", collections_func(collections_func_quote))
