# --*-- coding: utf-8 --*--
"""
    typing - 用于在静态代码中就能提示对应类型问题(默认python是不会进行提示的,需要指定对应类型)
    typing - 当前默认的类型比较少且无复核类型,因此需要借助typing,来指定自己想要的类型格式或其他分类类型,从而进行静态代码中捕获
    typing - 所谓的捕获就是黄色波浪线,会有对应的类型问题(但必须按照下面的格式书写才有 - 变量:类型   函数->类型)
    typing - 重点：设置的新类型还以自定义名称,就类似结构体

    注意：
        如果内网可以pip,那么结合mypy使用,可以进行更严格的类型检查[即运行输入和返回类型有误会报错],否则只能看黄色波浪线去判断
        需要：类型注解 - 这个只是为了清晰定位 + 静态检查（mypy）- 这个决定是否会执行后报错

    结合注意：
        结合mypy - 那么运行需要在终端执行 mypy xxx.py
        结合typeguard - 则是根据装饰器进行运行时判断
"""
from typing import List, NewType
from typeguard import typechecked
from collections.abc import Callable, Awaitable

Inter = List[int]
Length = NewType("Length", int)


@typechecked
def surface_area(edge_length: float) -> float:
    return edge_length


print("surface_area函数-输入为int,输出为str-不按规则会有黄色波浪线提示_且报错:", surface_area(5.0))


@typechecked
def surface_area_alias(edge_length: Inter) -> Inter:
    return edge_length


print("surface_area函数-定义新类型别名_Inter-不按规则会有黄色波浪线提示_且报错:", surface_area_alias([1]))


@typechecked
def surface_area_new(edge_length: Length) -> Length:
    return edge_length


print("surface_area函数-定义新类型别名_Length-不按规则会有黄色波浪线提示_且报错:", surface_area_new(Length(1)))
