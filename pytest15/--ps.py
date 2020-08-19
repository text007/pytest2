# pytest文档15-使用自定义标记 mark


# mark标记
"""
运行标记
标记表达式：@pytest.mark.xxx
cmd：pytest -v -m xxx

不运行标记
cmd：pytest -v -m “not xxx”
"""


# -v 指定的函数节点id
"""
运行某一条用例
cmd:pytest -v test_server.py::TestClass::test_method

运行整个 class
cmd：pytest -v test_server.py::TestClass

选择多个节点运行，多个节点中间空格隔开
cmd:pytest -v test_server.py::TestClass test_server.py::test_send_http

test_server.py
"""


# -k 匹配用例名称
"""
使用-k命令行选项指定在匹配用例名称的表达式
cmd:pytest -v -k http

运行所有的测试，根据用例名称排除掉某些用例：
cmd:pytest -k “not send_http” -v

同时选择匹配 “http” 和“quick”
cmd:pytest -k “http or quick” -v

test_server.py
"""
