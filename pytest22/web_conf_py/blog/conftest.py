

import pytest

@pytest.fixture(scope="function")
def open_biog():
    print("打开biog页面_function")
