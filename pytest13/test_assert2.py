# 异常断言:断言异常信息是否正确

# 常用断言
# assert  xx  判断xx为真
# assert not xx 判断xx不为真
# assert a in b  判断b包含a
# assert a == b 判断a等于b
# assert a != b  判断a不等于b

import pytest

def test_zero_division():
    """断言异常"""
    with pytest.raises(ZeroDivisionError) as excinfo:
        1 / 0

    # 断言异常类型 type
    assert excinfo.type == ZeroDivisionError
    # 断言异常 value 值
    assert "division by zero" in str(excinfo.value)
