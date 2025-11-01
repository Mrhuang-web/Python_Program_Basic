编写规范
    # 79 列、4 空格、空两行、别用 Tab
    # 类与类之间空两行
    # 类里方法空一行(其余都是空1行)
    # 一行显示多条语句,用分号 ; 分开

    命名规范
    | 类型 | 正确示例            | 错误示例           | 记忆口溜      |
    | -- | --------------- | -------------- | --------- |
    | 模块 | user\_utils.py  | userUtils.py   | 全小写，下划线   |
    | 类  | UserService     | userService    | 首字母大写，驼峰  |
    | 函数 | get\_user\_id() | getUserID()    | 全小写，下划线   |
    | 常量 | MAX\_RETRY = 3  | max\_retry = 3 | 全大写，下划线   |
    | 私有 | \_internal()    | internal()     | 前加 1 个下划线 |

    | 类型        | 正确示例                     | 错误/不建议                  | 记忆口溜              |
    | --------- | ------------------------ | ----------------------- | ----------------- |
    | 私有变量（强私有） | `self.__secret`          | `self._secret`（仍可被外部访问） | “双下划线，真隐藏”        |
    | 魔术方法      | `__len__(self)`          | 自己随便起名 `length()`       | “双前后，Python 找”, Python 自动调用，别自己发明    |
    | 公有/保护     | `update()` / `_update()` | `__update__()` 除非刻意重整   | “单下划，保护圈；双下划，重整圈” |


    注释规范
    # 单行注释：写“为什么”而不是“做什么”  -- 加在语句上面
    # 块注释：用 # 统一缩进  -- 加在语句上面
    # 文档字符串（docstring）：三引号必写，放函数/类/文件最上面


    文件头规范
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    # Copyright (c) 2025 你的名字 <你的邮箱@example.com>
    # 许可证：MIT
    创建文件自动生成方式：File - Editor - File-and-Code Template
    已创建文件自动不全：
        Settings | Editor | Live Templates - Python 分组
        点右上角 + → Live Template
        缩写（Abbreviation）写个短的，比如 pyhead
        把 EMAIL 变量设成 default value="yourmail@example.com"
        回到代码里输入 pyhead + Tab，整段就出来。


    编码格式(3.8以后默认utf-8无需指定)
    # Python中默认的编码格式是 ASCII 格式
    # 默认在开头加上  # -*- coding: UTF-8 -*- 或者 # coding=utf-8  [= 号两边不要空格]
    # Pycharm 设置步骤 - file > Settings - encoding - Editor > File encodings - IDE Encoding 和 Project Encoding设为utf-8

    规范扩展工具
    # pip install ruff
    # ruff format 你的文件.py
    # ruff check 你的文件.py

    Pycharm消除缓存
    #重启 PyCharm 缓存（File → Invalidate Caches / Restart）

    # Python 代码整洁之道


基础知识
    对象与地址
        id() 函数可以查看对象的地址
        is 运算符可以判断两个变量是否引用同一个对象

        | 概念  | 类比           |
        | --- | ------------ |
        | 对象  | 房子本体（真正的数据）  |
        | 地址  | 门牌号（找到房子的坐标） |
        | 变量名 | 贴在门牌上的标签     |

        # 地址相同 → 同一个对象 → 一改全改；
        # 地址不同 → 不同对象 → 互不影响

