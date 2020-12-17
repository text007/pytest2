
import pytest


@pytest.fixture(scope="function")
def open_biog01():
    print("打开blog页面_function")
