

import pytest

@pytest.fixture(scope="session")
def start1():
    print("\n打开首页")
    return "yoyo"