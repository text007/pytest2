

import pytest
import time

def test_03(start1, open_biog):
    print("测试用例test_03")
    time.sleep(1)
    assert start1 == "yoyo"

def test_04(start1, open_biog):
    print("测试用例 test_04")
    time.sleep(1)
    assert start1 == "yoyo"

def test_05(start1, open_biog):
    """跨模块调用baidu模块下的conftest"""
    print("测试用例test_05,跨模块调用baidu")
    time.sleep(1)
    assert start1 == "yoyo"


if __name__ == "__main__":
    pytest.main(["-s", "test_2_blog.py"])
