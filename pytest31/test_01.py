
import pytest
import allure

"""
@allure.severity 装饰器按严重级别来标记 case
执行指定测试用例  --allure-severities blocker
BLOCKER = "blocker"     阻塞缺陷
CRITICAL = "critical"   严重缺陷
NORMAL = "normal"       一般缺陷
MINOR = "minor"         次要缺陷
TRIVIAL = "trivial"     轻微缺陷　
"""

@allure.severity("normal")
def test_case_1():
    """修改个人信息-sex参数为空"""
    print("test case 111111")


@allure.severity("critical")
def test_case_2():
    """修改个人信息-sex参数传F和M两种类型，成功(枚举类型)"""
    print("test case 222222")


@allure.severity("critical")
def test_case_3():
    """修改个人信息-修改不是本人的用户信息，无权限操作"""
    print("test case 333333")


@allure.severity("blocker")
def test_case_4():
    """修改个人信息-修改自己的个人信息，修改成功"""
    print("test case 444444")
    assert 1 == 2


def test_case_5():
    """没标记severity的用例默认为normal"""
    print("test case 555555")
    assert 1 == 2
