"""
    钩子：定义

    想埋钩子 → 提前留空列表/字典/优先级队列。
    想挂代码 → 提供 register / decorator / += 等接口。
    想触发 → 到点遍历执行，别忘了 try/except 防止一个钩子崩掉全挂。


    register：
        自定义函数化钩子(register → 收集;run_hooks → 触发) 收集的时候可以进行排序_根据钩子里面定制的收集函数判定
    HookManager：
        自定义类钩子(优先级队列) register → 收集;run_hooks → 触发  register(self, slot, fn=None, priority=0)
        slot - > 键名; fn - > 函数(钩子下的函数); priority - > 优先级 越小越先执行
    MyHook：
        自定义类钩子(__import__,导入钩子) 拦截 import 语句，实现自动安装依赖
        导入钩子就是“在别人写 import xxx 的那一瞬间，你横插一脚，想干啥干啥”
        作用：
            在文件到导入定义好的导入钩子类,随后import的包,每个都会被截断去判断,并给到假包或自动安装等操作

"""
from collections.abc import Callable
from collections import defaultdict
import sys
import importlib.abc
import importlib.machinery

__all__ = ['register', 'run_hooks']
_hooks = []
fns = Callable[int, str]


def register(fn: fns) -> None:
    _hooks.append(fn)
    return fn


def register_start(fn: fns) -> None:
    _hooks.insert(0, fn)
    return fn


def run_hooks(*args, **kwargs):
    for fn in _hooks:
        fn(*args, **kwargs)


class HookManager:
    def __init__(self):
        self._slot = defaultdict(list)

    def register(self, slot, fn=None, priority=0):
        """支持装饰器/直接调用，priority 越小越先执行"""

        def decorator(func):
            self._slot[slot].append((priority, func))
            # 保持有序
            self._slot[slot].sort(key=lambda x: x[0])
            return func

        # 装饰器用法
        if fn is None:
            return decorator
        # 普通用法
        return decorator(fn)

    def run(self, slot, *args, **kwargs):
        for _, fn in self._slot[slot]:
            fn(*args, **kwargs)

    def remove(self, slot, fn):
        self._slot[slot] = [(p, f) for p, f in self._slot[slot] if f != fn]


# 全局单例，方便随时用
hooks = HookManager()


class MyHook(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_spec(self, fullname, path, target=None):
        if fullname == 'fake':
            # 返回一个假的模块
            print(fullname, self)
            return importlib.machinery.ModuleSpec(fullname, self)
        return None

    def create_module(self, spec):
        return None  # 使用默认模块

    def exec_module(self, module):
        # 动态生成模块内容
        module.hello = lambda: print('this is a fake module!')


# 把钩子塞进 meta_path
sys.meta_path.insert(0, MyHook())

if __name__ == '__main__':
    import fake
    fake.hello()  # 成功运行，尽管磁盘上根本没有 fake.py
