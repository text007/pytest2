# python文档23-fixture作为参数传入,error和failed区别


import pytest

@pytest.fixture()
def user():
    print("获取用户名")
    a = "yoyo"
    assert a == "yoyo111"
    return a

def test_1(user):
    assert user == "yoyo"

if __name__ == "__main__":
    pytest.main(["-s", "test_fixture1.py"])
