# python文档25-fixture的作用范围(scope)


# fixture作用范围
"""
fixture里面有个scope参数可以控制fixture的作用范围:session > module > class > function
-- function 每一个函数或方法都会调用
-- class  每一个类调用一次，一个类可以有多个方法
-- module，每一个.py文件调用一次，该文件内又有多个function和class
-- session 是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
"""


# scope=”function”
"""
@pytest.fixture()如果不写参数，默认就是scope=”function”，它的作用范围是每个测试用例来之前运行一次，销毁代码在测试用例运行之后运行。
test_scope1.py
"""


# scope=”class”
"""
fixture为class级别的时候，如果一个class里面有多个用例，都调用了此fixture，那么此fixture只在该class里所有用例开始前执行一次
test_scope2.py
"""


# scope=”module”
"""
fixture为module级别时，在当前.py脚本里面所有用例开始前只执行一次
test_scope3.py
"""


# scope=”session”
"""
fixture为session级别是可以跨.py模块调用的,也就是当我们有多个.py文件的用例时候，如果多个用例只需调用一次fixture，那就可以设置为scope=”session”，并且写到conftest.py文件里
conftest.py文件名称是固定的，pytest会自动识别该文件。放到工程的根目录下，就可以全局调用了，如果放到某个package包下，那就只在该package内有效
conftest.py
test_scope4.py
test_scope5.py
"""
