# python文档23-fixture作为参数传入,error和failed区别


# fixture简介
"""
有独立的命名，并通过声明它们从测试函数、模块、类或整个项目中的使用来激活。
按模块化的方式实现，每个fixture都可以互相调用。
fixture的范围从简单的单元扩展到复杂的功能测试，允许根据配置和组件选项对fixture和测试用例进行参数化，或者跨函数 function、类class、模块module或整个测试会话sessio范围。
"""


# fixture作为参数传入
"""
定义fixture跟定义普通函数差不多，唯一区别就是在函数上加个装饰器@pytest.fixture()，fixture命名不要用test开头，跟用例区分开。用例才是test开头的命名。
fixture是可以有返回值的，如果没return默认返回None。用例调用fixture的返回值，直接就是把fixture的函数名称当成变量名称.
"""


# error和failed区别
"""
测试结果一般有三种：passed、failed、error。（skip的用例除外）
测试通过passed

如果在test_用例里面断言失败，那就是failed

如果在fixture里面断言失败了，那就是error
"""
