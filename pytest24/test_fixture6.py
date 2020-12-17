# fixture与fixture互相调用

import pytest


@pytest.fixture()
def first():
    print("获取用户名")
    a = "yoyo"
    return a


@pytest.fixture()
def sencond(first):
    """sencond 调用 first fixture"""
    a = first
    b = "123456"
    return (a, b)


def test_1(sencond):
    """用例传 fixture"""
    print("测试账号：%s, 密码：%s" % (sencond[0], sencond[1]))

    assert sencond[0] == "yoyo"


if __name__ == "__main__":
    pytest.main(["-s", "test_fixture6.py"])
