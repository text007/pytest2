# 当断言失败的时候，会给出自己写的失败原因了E

def f():
    return 3

def test_function():
    # assert f() == 4
    a = f()
    assert a % 2 == 0, "判断 a 为偶数，当前 a 的值为：%s" %a