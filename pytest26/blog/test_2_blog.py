
import pytest

def test_03(start01, open_biog01):
    print("测试用例test_03")
    assert 1

def test_04(start01, open_biog01):
    print("测试用例test_04")
    assert 1

def test_05(start01, open_baidu01):
    print("测试用例test_05")
    assert 1

if __name__=="__main__":
    pytest.main(["-s", "test_2_blog.py"])