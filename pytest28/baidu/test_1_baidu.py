
import pytest
import time


def test_01(start02, open_baidu02):
    print("测试用例test_01")
    time.sleep(1)
    assert start02 == "yoyo"


@pytest.mark.repeat(5)
def test_02(start02, open_baidu02):
    print("测试用例test_02")
    time.sleep(1)
    assert start02 == "yoyo"


if __name__=="__main__":
    pytest.main(["-s", "test_1_baidu.py"])
