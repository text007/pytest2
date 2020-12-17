

import pytest
import time


def test_06(start1, open_baidu):
    print("测试用例test_06")
    time.sleep(1)
    assert start1 == "yoyo"

def test_07(start1, open_baidu):
    print("测试用例test_07")
    time.sleep(1)
    assert start1 == "yoyo"


if __name__ == "__main__":
    pytest.main(["-s", "test_2.py"])
