# pytest文档28-重复执行用例（pytest-repeat）


# pytest-repeat
"""
pytest-repeat是pytest的一个插件，用于重复执行单个用例，或多个测试用例，并指定重复次数
支持：
Python 2.7, 3.4+ 或 PyPy
py.test 2.8或更高

使用pip安装pytest-repeat：
pip install pytest-repeat
"""


# 重复执行—count
"""
重复执行5次（1111122222）
pytest baidu/test_1_baidu.py -s —count=5
"""


# —repeat-scope
"""
循环重复5次（1212121212）
pytest baidu/test_1_baidu.py -s —count=5 —repeat-scope=session
"""


# @pytest.mark.repeat(count)
"""
@pytest.mark.repeat(count)
@pytest.mark.repeat(5)
test_1_baidu.py
"""


# 重复测试直到失败
"""
尝试运行test_file.py 1000次，但一旦发生故障就会停止
pytest --count=1000 -x test_file.py
"""
