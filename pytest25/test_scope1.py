# scope=”function”
# 默认就是scope=”function”
# 作用范围是每个测试用例来之前运行一次，销毁代码在测试用例运行之后运行。


import pytest


@pytest.fixture()
def first():
    print("\n获取用户名")
    a = "yoyo"
    return a


@pytest.fixture(scope="function")
def sencond():
    print("\n获取密码")
    b = "123456"
    return b


class TestCase():
    def test_1(self, first):
        print("测试账号：%s" % first)
        assert first == "yoyo"

    def test_2(self, sencond):
        print("测试密码：%s" % sencond)
        assert sencond == "123456"


if __name__ == "__main__":
    pytest.main(["-s", "test_scope1.py"])
