# pytest文档14-函数传参和 fixture 传参数 request

# 函数传参
"""
测试用例传参需要用装饰器 @pytest.mark.parametrize，里面写两个参数:
--第一个参数是字符串，多个参数中间用逗号隔开
--第二个参数是list,多组数据用元祖类型

test_01.py
"""


# request 参数
"""
user = request.param 这一步是接收传入的参数
添加indirect=True参数是为了把login当成一个函数去执行，而不是一个参数

test_02.py
"""


# request 传2个参数
"""
如果用到@pytest.fixture，里面用2个参数情况，可以把多个参数用一个字典去存储，这样最终还是只传一个参数
不同的参数再从字典里面取对应key值就行，如： user = request.param[“user”]

test_03.py
"""


# 多个fixtrue
"""
用例上面是可以同时放多个fixture的，也就是多个前置操作，可以支持装饰器叠加，使用parametrize装饰器叠加时，用例组合是2个参数个数相乘

test_04.py
"""