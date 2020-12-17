# pytest文档18-配置文件 pytest.ini

# ini配置文件
"""
pytest里面有些文件是非test文件:
--pytest.ini pytest的主配置文件，可以改变pytest的默认行为
--conftest.py 测试用例的一些fixture配置
--_init_.py 识别该文件夹为python的package包
--tox.ini 与pytest.ini类似，用tox工具时候才有用
--setup.cfg 也是ini格式文件，影响setup.py的行为

pytest.ini
"""


# mark 标记
"""
test_mark.py

有时候标签多了，不容易记住，为了方便后续执行指令的时候能准确使用mark的标签，可以写入到pytest.ini文件
pytest.ini

查看 ini 配置文件:pytest --markers
"""


# 禁用 xpass
"""
设置xfail_strict = true可以让那些标记为@pytest.mark.xfail但实际通过的测试用例被报告为失败
pytest.ini
"""

# addopts
"""
addopts参数可以更改默认命令行选项，这个当我们在cmd输入指令去执行用例的时候，会用到，比如我想测试完生成报告，指令比较长
输入指令添加到 pytest.ini 文件中
pytest.ini
打开cmd，直接输入pytest，它就能默认带上这些参数了
"""