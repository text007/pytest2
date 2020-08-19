# pytest 文档2-用例运行规则

# 用例设计原则
"""
文件名以 test_*.py 文件和 *_test.py
以test_ 开头的函数
以Test 开头的类
以test_ 开头的方法
所有的包 pakege 必须要有 __init__.py 文件
"""


# help 帮助
"""
pytest -h 或 pytest —help 查看 pytest 命令行参数
pytest 文件名/    执行某个目录下所有的用例
pytest 脚本名称.py    执行某一个py文件下用例
pytest test_mod.py::test_func    运行 .py 模块里面的某个函数
pytest test_mod.py::TestClass::test_method    运行.py 模块里面,测试类里面的某个方法
pytest -m slow  将运行用 @ pytest.mark.slow    装饰器修饰的所有测试。
pytest -x test_class.py    遇到错误时停止测试
pytest --maxfail=1    当用例错误个数达到指定数量时，停止测试
"""