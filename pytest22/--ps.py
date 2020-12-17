# pytest文档22-pytest分布式执行（pytest-xdist）

# pytest-xdist
"""
安装：pip install pytest-xdist
"""


# 并行测试
"""
多cpu并行执行用例，直接加个-n参数即可，后面num参数就是并行数量，比如num设置为3:
pytest -n 3
"""


# 测试报告
"""
使用pytest-xdist插件也能生成html报告,完美支持pytest-html插件
pytest -n 3 —html=report.html —self-contained-html
"""
