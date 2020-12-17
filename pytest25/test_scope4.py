# scope=”session”
# 可以跨.py模块调用
# 当我们有多个.py文件的用例时候，如果多个用例只需调用一次fixture，那就可以设置为scope=”session”，并且写到conftest.py文件里


import pytest


def test_1(first):
    print("测试账号：%s" % first)
    assert first == "yoyo"


if __name__ == "__main__":
    pytest.main(["-s", "test_scope4.py"])
