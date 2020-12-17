# python文档24-使用多个fixture和fixture互相调用


# 使用多个fixture
"""
如果用例需要用到多个fixture的返回数据，fixture也可以return一个元组、list或字典，然后从里面取出对应数据。
test_fixture4.py

当然也可以分开定义成多个fixture，然后test_用例传多个fixture参数
test_fixture5.py
"""


# fixture与fixture互相调用
"""
fixture与fixture直接也能互相调用的
test_fixture6.py
"""
