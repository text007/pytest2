# 首先需要在contetest.py 添加命令行选项,命令行传入参数”—cmdopt“,
# 用例如果需要用到从命令行传入的参数，就调用 cmdopt 函数

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")
