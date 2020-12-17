# 装饰器 usefixtures


import time
import pytest

@pytest.fixture(scope="function")
def start(request):
    print("\n---开始执行 function ---")


@pytest.mark.usefixtures("start")
def test_a():
    print("---用例 a 执行---")

@pytest.mark.usefixtures("start")
class Test_aaa():

    def test_01(self):
        print("---用例 01---")

    def test_02(self):
        print("---用例 02---")


if __name__ == "__main__":
    pytest.main(["-s", "test_07.py"])
