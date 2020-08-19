# pytest 文档4-测试用例 setup 和 teardown

# 用例运行级别
"""
模块级（setup_module/teardown_module）开始于模块始末，全局的
函数级（setup_function/teardown_function）只对函数用例生效（不在类中）
类级（setup_class/teardown_class）只在类中前后运行一次(在类中)
方法级（setup_method/teardown_method）开始于方法始末（在类中）
类里面的（setup/teardown）运行在调用方法的前后
"""


# 函数式
"""
setup_function/teardown_function    每个用例开始和结束调用一次
--用例执行顺序：setup_function》用例1》teardown_function， setup_function》用例2》teardown_function， setup_function》用例3》teardown_function

setup_module 是所有用例开始前只执行一次，teardown_module 是所有用例结束后只执行一次
--运行的优先级：setup_class》setup_method》setup 》用例》teardown》teardown_method》teardown_class
--备注：这里setup_method和teardown_method的功能和setup/teardown功能是一样的，一般二者用其中一个即可

setup_module/teardown_module 的优先级是最大的，然后函数里面用到的 setup_function/teardown_function 与类里面的 setup_class/teardown_class 互不干涉
"""
