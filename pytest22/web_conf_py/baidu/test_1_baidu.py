

import pytest
import time

def test_01(start1, open_baidu):
    print("测试用例test_01")
    time.sleep(1)
    assert start1 == "yoyo"

def test_02(start1, open_baidu):
    print("测试用例test_02")
    time.sleep(1)
    assert start1 == "yoyo"


if __name__ == "__main__":
    pytest.main(["-s", "test_1_baidu.py"])
