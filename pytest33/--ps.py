# pytest文档33-Hooks函数获取用例执行结果(pytest_runtest_makereport)


# pytest_runtest_makereport
"""
这里item是测试用例，call是测试步骤，具体执行过程如下：
-- 先执行when=’setup’ 返回setup 的执行结果
-- 然后执行when=’call’ 返回call 的执行结果
-- 最后执行when=’teardown’返回teardown 的执行结果
"""


# 运行案例
"""
conftest.py
test_hooks_1.py

运行用例的过程会经历三个阶段:setup-call-teardown,每个阶段都会返回的 Result 对象和 TestReport 对象，以及对象属性。
setup和teardown上面的用例默认都没有，结果都是passed
"""


# setup和teardown
"""
conftest.py
test_hooks_1.py
"""


# setup失败情况
"""
conftest.py
test_hooks_1.py
"""


# call失败情况
"""
conftest.py
test_hooks_1.py
"""


# teardown失败了
"""
conftest.py
test_hooks_1.py
"""


# 只获取call的结果
"""
conftest.py
test_hooks_1.py
"""
