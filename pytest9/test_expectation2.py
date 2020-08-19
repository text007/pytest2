#标记单个测试实例在参数化，例如使用内置的mark.xfail

import pytest
@pytest.mark.parametrize("test_input, expected",
                         [("3+5", 8),
                         ("2+4", 6),
                         pytest.param("6 * 9", 42, marks=pytest.mark.xfail),
                         ])

def test_eval(test_input,expected):
    print("------开始用例------")
    assert eval(test_input) == expected # eval() 返回表达式计算结果

if __name__ == "main":
    pytest.main(["-s", "test_canshu1.py"])
