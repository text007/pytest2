# pytest 文档5-fixture 之 conftest.py

# fixture 优势
"""
firture 相对于 setup 和 teardown 来说应该有以下几点优势:
--命名方式灵活，不局限于 setup 和 teardown 这几个命名
--conftest.py 配置里可以实现数据共享，不需要 import 就能自动找到一些配置
--scope=”module” 可以实现多个.py跨文件共享前置
--scope=”session” 以实现多个.py跨文件使用一个 session 来完成多个用例

fixture(scope="function", params=None, autouse=False, ids=None, name=None):
'''使用装饰器标记fixture的功能
    可以使用此装饰器（带或不带参数）来定义fixture功能。 fixture功能的名称可以在以后使用
    引用它会在运行测试之前调用它：test模块或类可以使用pytest.mark.usefixtures（fixturename标记。
    测试功能可以直接使用fixture名称作为输入参数，在这种情况下，夹具实例从fixture返回功能将被注入。

    :arg scope: scope 有四个级别参数 "function" (默认), "class", "module" or "session".

    :arg params: 一个可选的参数列表，它将导致多个参数调用fixture功能和所有测试使用它

    :arg autouse:  如果为True，则为所有测试激活fixture func 可以看到它。 如果为False（默认值）则显式需要参考来激活fixture

    :arg ids: 每个字符串id的列表，每个字符串对应于params 这样他们就是测试ID的一部分。 如果没有提供ID它们将从params自动生成

    :arg name:   fixture的名称。 这默认为装饰函数的名称。 如果fixture在定义它的同一模块中使用，夹具的功能名称将被请求夹具的功能arg遮蔽; 解决这个问题的一种方法是将装饰函数命名
                       “fixture_ <fixturename>”然后使用”@ pytest.fixture（name ='<fixturename>'）'''
"""


# fixture 参数传入（scope=”function”）
"""
test_fixt.py
"""


# conftest.py 配置
"""
conftest.py 配置需要注意以下点：
--conftest.p y配置脚本名称是固定的，不能改名称
--conftest.py 与运行的用例要在同一个 pakage 下，并且有 init.py 文件
--不需要import导入 conftest.py，pytest 用例会自动查找

conftest.py
"""
