# 若要获得多个参数化参数的所有组合，可以堆叠参数化装饰器

import pytest
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])

def test_foo(x, y):
    print("测试数据组合：x->%s，y->%s" % (x, y))

if __name__ == '__main__':
    pytest.main(["-s", "test_canshu1.py"])
