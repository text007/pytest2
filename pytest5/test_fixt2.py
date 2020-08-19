import pytest


def test_s4(login):
    print("用例4：登录之后其他动作111")


def test_s5(): # 不传 login
    print("用例5：登录之后其他动作111")


if __name__ == "__main__":
    pytest.main(["-s", "test_fix2.py"])
