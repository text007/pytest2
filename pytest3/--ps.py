# pytest 文档3-pycharm 运行 pytest

# pycharm 运行三种fs
"""
1.以 xx.py 脚本方式直接执行，当写的代码里面没用到 unittest 和 pytest 框架时，并且脚本名称不是以 test_ 开头命名的，此时 pycharm 会以 xx.py 脚本方式运行
2.当脚本命名为test_xx.py时，用到 unittest 框架，此时运行代码，pycharm会自动识别到以unittest 方式运行
3.以 pytest 方式运行，需要改该工程设置默认的运行器：file->Setting->Tools->Python Integrated Tools->项目名称->Default test runner->选择 py.test
备注：pytest 是可以兼容 unittest 框架代码的
"""


# pycharm 写 pytest 代码
"""
1.在 pycharm 里面写 pytest 用例，先导入 pytest (import pytest)
2.运行结果 “.F. ”  点是代表测试通过，F是 Fail 的意思，1 warnings 是用于 pytest.main(‘-q test_class.py’)里面参数需要传 list，多个参数放 list 就不会有警告了
"""


# pycharm 设置 pytest
"""
1.新建一个工程后，左上角file->Setting->Tools->Python Integrated Tools->项目名称->Default test runner->选择py.test
2.改完之后，再重新建个脚本（注意是先改项目运行方式，再写代码才能出来），接下来右键运行就能出来pytest运行了
3.pytest是可以兼容unittest脚本的，之前写的unittest用例也能用pytest框架去运行
"""
