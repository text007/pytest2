
import pytest

@pytest.fixture(scope="session")
def start01():
    print("\n打开首页")
