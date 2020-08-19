# fixture参数传入（scope=”function”）
# 此时的级别的function，针对函数有效;默认scope=”function”
# function 级别为用例之前的操作

import pytest

@pytest.fixture()
def login():
    print("输入账号，密码先登录")

def test_s1(login):
    print("用例1：登录之后其他动作111")

def test_s2():
    print("用例2：不需要登录，操作222")

def test_s3(login):
    print("用例3：登录后其他操作333")

if __name__ == "__main__":
    pytest.main(["-s", "test_fixt.py"])