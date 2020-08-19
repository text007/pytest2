# fixture参数scope=”module”，module作用是整个.py文件都会生效，用例调用时，参数写上函数名称就行
# scope=”module” 只会在第一个用例前执行一次
# scope=”module”  yield  在第一个用例后执行一次
# 如果其中一个用例出现异常，不影响yield后面的teardown执行,运行结果互不影响，并且在用例全部执行完之后，会呼唤teardown的内容
# 如果在setup就异常了，那么是不会去执行yield后面的teardown内容了

import pytest

@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并打开百度首页")

    yield
    print("执行 teardown!")
    print("最后关闭浏览器")

def test_s1(open):
    print("用例1：搜索python-1")

    # 如果第一个用例异常，不影响其他用例执行
    raise NameError # m模拟异常

def test_s2(open):
    print("用例2：搜索python-2")

def test_s3(open):
    print("用例3：搜索python-3")

if __name__ == "__main__":
    pytest.main(["-s", "test_f1.py"])
