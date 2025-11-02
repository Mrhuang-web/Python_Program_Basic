"""
    回调：函数 A 当做参数传给函数 B，B 在某个时刻回头调用 A，A 就是回调函数，B 就是高阶函数(在B中直接就完成A,不用等待) - 等待被调取无需装饰器

    阻塞：程序停下来等待某个操作完成，CPU 空转等待结果(例如socket接收,input等待接收这些,程序必须依次进行)

    轮询：程序不断询问某个操作是否完成，CPU 忙等(直接接收不到就会一直去检测状态 - 也就是轮询 - 一般配置循环实现轮询)

"""
import time
from collections.abc import Callable
from typeguard import typechecked
import socket

collections_1 = Callable[int, int]
sock = socket.socket()
sock.connect(('www.example.com', 80))


@typechecked
def collections_func_b(func: collections_1) -> int:
    return func(1)


@typechecked
def collections_func_quote_a(number: int) -> int:
    return number + 1


print("collections_1 = Callable[int, int]_B函数内部调用参数传入的A函数_回调",
      collections_func_b(collections_func_quote_a), "\n")


def socket_func():
    data = sock.recv(1024)
    print("socket_func_阻塞_接收不到不会进行下一步:", data)


# socket_func()


def socket_func_f():
    sock_ = socket.socket()
    sock_.setblocking(False)
    try:
        sock_.connect(('www.example.com', 80))
    except BlockingIOError:
        pass
    print("socket_func_非阻塞_还能建立完直接下一步:")
    while True:
        try:
            sock_.recv(1024)
            break
        except BlockingIOError:
            continue
    print("socket_func_未连接_非阻塞+轮询_接收不到一直去检测状态_直到接收到_不然会一直下去:")


# socket_func_f()


def socket_func_t():
    sock.setblocking(False)
    while True:
        try:
            sock.recv(1024)
            break
        except BlockingIOError:
            time.sleep(2)
            print("socket_func_已连接_非阻塞+轮询_接收不到一直去检测状态_直到接收到_不然会一直下去:每2s轮询")
            continue


socket_func_t()
