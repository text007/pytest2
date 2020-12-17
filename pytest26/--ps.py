# pytest文档26-conftest.py作用范围
# 在不同的测试子目录也可以放conftest.py，作用范围只在该层级以及以下目录生效

# scope="session"
"""
session级别的，只运行一次
test_1_baidu.py
"""

# scope="function"
"""
function级别，每个用例调用一次。
test_2_blog.py
"""
