
import pytest

@pytest.fixture(scope="session")
def start02():
    print("\n打开首页")
    return "yoyo"
