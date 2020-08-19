# 多个fixtrue: 用例上面是可以同时放多个fixture的，也就是多个前置操作，可以支持装饰器叠加，
# 使用parametrize装饰器叠加时，用例组合是2个参数个数相乘

import pytest

# 测试账号数据
test_user = ["admin1", "admin2"]
test_psw = ["111111", "222222"]


# 登录账号
@pytest.fixture(scope="module")
def input_user(request):
    user = request.param
    print("登录账号：%s" % user)
    return user


# 登录密码
@pytest.fixture(scope="module")
def input_psw(request):
    psw = request.param
    print("登录密码：%s" % psw)
    return psw


@pytest.mark.parametrize("input_user", test_user, indirect=True)
@pytest.mark.parametrize("input_psw", test_psw, indirect=True)
def test_login(input_user, input_psw):
    """登录用例"""
    a = input_user
    b = input_psw
    print("测试数据a-> %s, b->%s" % (a, b))
    assert b


if __name__ == '__main__':
    pytest.main(["-s", "test_04.py"])
