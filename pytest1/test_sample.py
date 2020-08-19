# 测试函数

# pytest 用例规则
# 测试文件以 test_ 开头（以 _test 结尾也可以）
# 测试类以 Test 开头，并且不能带有 init 方法
# 测试函数以 test_ 开头
# 断言使用 assert


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
