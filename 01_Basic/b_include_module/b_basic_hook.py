"""
    钩子：
        原理都是如此
        hook,把函数注册到某个位置，等框架/库在特定点调用(在预留的位置插入我的代码) - 语法糖/装饰器
        框架作者提前在代码里埋好了“插桩点” [会对自己定义的函数进行处理]
        用户可以“挂”自己的函数进去到框架中定义好的里面，从而不改变框架源码就能扩展行为

    flask：自带钩子
    register：函数化钩子(把函数注册到列表中,在通过特定调用去执行)
    HookManager：自定义钩子
"""

from flask import Flask, g, request
from b_basic_hook_define import hooks
import time
import b_basic_hook_define as b_hook

app = Flask(__name__)


@app.before_request
def start_timer():
    g.start = time.time()


@app.after_request
def print_cost(response):
    cost = (time.time() - g.start) * 1000
    print(f"[{request.method}] {request.path} -> {response.status_code}  {cost:.2f}ms")
    return response


@app.route("/")
def index():
    return "hello"


# app.run()


@b_hook.register
def my_hook_function(param: int) -> str:
    print(f"函数钩子_Hook called with param: {param}")
    return f"Hook called with param: {param}"


@b_hook.register_start
def my_hook_function_start(param: int) -> str:
    print(f"函数钩子_Hook called with param start: {param}")
    return f"Hook called with param start: {param}"


if __name__ == '__main__':
    b_hook.run_hooks(2)
    print(f"函数钩子_Hook执行完成", "\n")


@hooks.register('before_save', priority=1)
def validate(obj):
    print('[类钩子_通过slot-before_save键拿函数_校验]', obj)


@hooks.register('before_save', priority=10)
def fill_default(obj):
    print('[类钩子_通过slot-before_save键拿函数填默认值]', obj)


# 框架内部触发
class Model:
    def save(self):
        hooks.run('before_save', self)
        print('类钩子_真正写数据库')
        hooks.run('after_save', self)
        print(f"类钩子_Hook执行完成", "\n")


Model().save()
