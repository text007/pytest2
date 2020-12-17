# scope=”class”
# class级别
#只在class里所有用例开始前执行一次

import pytest


@pytest.fixture(scope="class")
def first():
    print("\n获取用户名，scope 为 class级别只运行一次")
    a = "yoyo"
    return a

class TestCase():
    def test_1(self, first):
        print("测试账号：%s" % first)
        assert first == "yoyo"

    def test_2(self, first):
        print("测试账号：%s" % first)
        assert first == "yoyo"


if __name__ == "__main__":
    pytest.main(["-s", "test_scope2.py"])
