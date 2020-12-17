# pytest文档17-fixture 之 autouse=True


# 调用 fixture 三种方法
"""
1.函数或类里面方法直接传fixture的函数参数名称
2.使用装饰器@pytest.mark.usefixtures()修饰
3.autouse=True自动使用
"""


# 用例传 fixture 参数
"""
先定义start功能，用例全部传start参数，调用该功能
@pytest.fixture(scope="function")
test_06.py
"""


# 装饰器 usefixtures
"""
使用装饰器@pytest.mark.usefixtures()修饰需要运行的用例
@pytest.mark.usefixtures("start")
test_07.py
"""

# 设置autouse=True
"""
autouse设置为True，自动调用fixture功能
tart设置scope为module级别，在当前.py用例模块只执行一次，autouse=True自动使用
open_home设置scope为function级别，每个用例前都调用一次，自动使用
test_08.py
test_09.py
"""
