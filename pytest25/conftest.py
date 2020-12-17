
import pytest


@pytest.fixture(scope="session")
def first():
    print("\n获取用户名，scope 为 session 级别多个 .py 模块只运行一次")
    a = "yoyo"
    return a
