
import pytest


def test_01(start01, open_baidu01):
    print("测试用例test_01")
    assert 1


def test_02(start01, open_baidu01):
    print("测试用例test_01")
    assert 1


if __name__=="__main__":
    pytest.main(["-s", "test_1_baidu.py"])
