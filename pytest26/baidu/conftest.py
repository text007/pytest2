
import pytest

@pytest.fixture(scope="session")
def open_baidu01():
    print("打开百度首页_session")
