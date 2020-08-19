# skip:

# 跳过测试函数的最简单方法是使用跳过装饰器标记它，可以传递一个可选的原因
"""
@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    ...
"""


# 通过调用来在测试执行或设置期间强制跳过pytest.skip（reason）功能：
"""
def test_function():
    if not valid_config():
        pytest.skip("unsupported configuration")
"""


# 使用pytest.skip（reason，allow_module_level = True）跳过整个模块级别：
"""
import pytest
if not pytest.config.getoption("--custom-flag"):
    pytest.skip("--custom-flag is missing, skipping tests", allow_module_level=True)
"""


# skipif

# 有条件地跳过某些内容，则可以使用skipif代替。 这是标记测试的示例在Python3.6之前的解释器上运行时要跳过的函数
"""
import sys
@pytest.mark.skipif(sys.version_info < (3,6),
reason="requires python3.6 or higher")
def test_function():
    ...
如果条件在收集期间评估为True，则将跳过测试函数，具有指定的原因使用-rs时出现在摘要中。
"""

# 模块之间共享skipif标记
"""
import mymodule
minversion = pytest.mark.skipif(mymodule.__versioninfo__ < (1,1),
reason="at least mymodule-1.1 required")
@minversion
def test_function():
    ...
"""


# 导入标记并在另一个测试模块中重复使用它：
"""
from test_mymodule import minversion
@minversion
def test_anotherfunction():
    ...
"""


# skip类或模块

# 可以在类上使用skipif标记（与任何其他标记一样）：
"""
@pytest.mark.skipif(sys.platform == 'win32',
reason="does not run on windows")
class TestPosixCalls(object):
    def test_function(self):
        "will not be setup or run under 'win32' platform"

如果条件为True，则此标记将为该类的每个测试方法生成跳过结果
"""


# 要跳过模块的所有测试功能，可以在全局级别使用pytestmark名称
"""
pytestmark = pytest.mark.skipif(...)

如果将多个skipif装饰器应用于测试函数，则如果任何跳过条件为真，则将跳过它
"""


# skip文件或目录
"""
有时您可能需要跳过整个文件或目录，
例如，如果测试依赖于特定于Python的版本功能或包含您不希望pytest运行的代码。
在这种情况下，您必须排除文件和目录来自收藏。
"""


# skip缺少导入依赖项

# 可以在模块级别或测试或测试设置功能中使用以下帮助程序
"""
docutils = pytest.importorskip("docutils")
如果无法在此处导入docutils，则会导致测试跳过结果。 你也可以跳过库的版本号
docutils = pytest.importorskip("docutils", minversion="0.3")
将从指定模块的version属性中读取版本。
"""


# 跳过模块中的测试
"""
无条件地跳过模块中的所有测试：
--pytestmark = pytest.mark.skip(“test”)

根据某些条件跳过模块中的所有测试:
--pytestmark = pytest.mark.skipif(sys.platform == “win32”, “tests for linux
  ˓→ only”
  
如果缺少某些导入，则跳过模块中的所有测试:
--pexpect = pytest.importorskip(“pexpect”)
"""
