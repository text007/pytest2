# setup_function/teardown_function  每个用例开始和结束调用一次
# setup_module 是所有用例开始前只执行一次，teardown_module 是所有用例结束后只执行一次
# setup_module/teardown_module的优先级是最大的，
# --然后函数里面用到的setup_function/teardown_function与类里面的setup_class/teardown_class互不干涉

import pytest


def setup_module():
    print("setup_module:整个.py模块只执行一次")
    print("比如：所有用例开始前打开一次浏览器")

def teardown_module():
    print("teardown_module:整个.py模块只执行一次")
    print("比如：所有用例结束后关闭浏览器次浏览器")

def setup_function():
    print("setup_function:每个用例开始前都会执行")

def teardown_function():
    print("teardown_function:每个用例结束后都会执行")

def test_one():
    print("正在执行----test_one")
    x = "this"
    assert "h" in x

def test_two():
    print("正在执行----test_two")
    x = "hello"
    assert hasattr(x, "check")


class TestCase():

    def setup_class(self):
        print("setup_class:所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之后")

    def test_three(self):
        print("正在执行----test_three")
        a = "hello"
        b = "hello world"
        assert a in b

    def test_four(self):
        print("正在执行----test_four")
        x = "hello"
        assert hasattr(x, "check")


if __name__ == "__main__":
    pytest.main(["-s", "test_fixt.py"])
