

import pytest

@pytest.fixture(scope="session")
def login03():
    print("用例先登录")
