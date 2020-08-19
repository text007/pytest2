# setup/teardown    每个用例开始和结束执行
# setup_class/teardown_class    所有用例执行之前和之后
# setup_method/teardown_method  每个用例开始和结束执行
# setup_method 和 teardown_method 的功能和setup/teardown 功能是一样的，一般二者用其中一个即可
# 优先级：setup_class》setup_method》setup 》用例》teardown》teardown_method》teardown_class

import pytest


class TestCase():

    def setup(self):
        print("setup:每个用例开始前执行")

    def teardown(self):
        print("teardown:每个用例结束后执行")

    def setup_class(self):
        print("setup_class:所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之后")

    def setup_method(self):
        print("setup_method:每个用例开始前执行")

    def teardown_method(self):
        print("teardown_method:每个用例结束后执行")

    def test_one(self):
        print("正在执行----test_one")
        x = "this"
        assert "h" in x

    def test_two(self):
        print("正在执行----test_two")
        x = "hello"
        assert hasattr(x, "check")

    def test_three(self):
        print("正在执行----test_three")
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == "__main__":
    pytest.main(["-s", "test_fixtclass.py"])