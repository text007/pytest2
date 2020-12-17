# 用例传 fixture 参数


import time
import pytest

@pytest.fixture(scope="function")
def start(request):
    print("\n---开始执行 function ---")

def test_a(start):
    print("---用例 a 执行---")


class Test_aaa():

    def test_01(self):
        print("---用例 01---")

    def test_02(self, start):
        print("---用例 02---")


mark标记

