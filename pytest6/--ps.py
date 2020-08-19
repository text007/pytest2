# pytest 文档6-fixture 之 yield 实现 teardown

# scope=”module”
"""
1.fixture参数scope=”module”，module作用是整个.py文件都会生效，用例调用时，参数写上函数名称就行
2.module 级别的 fixture 在当前.py 模块里，只会在用例第一次调用前执行一次
"""


# yield 执行 teardown
"""
fixture 里面的 teardown 用 yield 来唤醒 teardown 的执行

test_f1.py
"""