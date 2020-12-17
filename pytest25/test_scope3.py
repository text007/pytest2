# scope=”module”
# module级别
# 在当前.py脚本里面所有用例开始前只执行一次


import pytest


@pytest.fixture(scope="module")
def first():
    print("\n获取用户名，scope 为 module 级别当前 .py 模块只运行一次")
    a = "yoyo"
    return a


def test_1(first):
    print("测试账号：%s" % first)
    assert first == "yoyo"


class TestCase():
    def test_2(self, first):
        print("测试账号：%s" % first)
        assert first == "yoyo"


if __name__ == "__main__":
    pytest.main(["-s", "test_scope3.py"])
