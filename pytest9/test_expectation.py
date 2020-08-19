# 实现检查一定的输入和期望输出测试功能的典型例子

import pytest
@pytest.mark.parametrize("test_input, expected",
                         [("3+5", 8),
                         ("2+4", 6),
                         ("6 * 9", 42),
                         ])

def test_eval(test_input,expected):
    assert eval(test_input) == expected # eval() 返回表达式计算结果

if __name__ == "main":
    pytest.main(["-s", "test_canshu1.py"])
