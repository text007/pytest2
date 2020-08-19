# pytest文档10-命令行传参 addoption


# contetest 配置参数
"""
首先需要在 contetest.py 添加命令行选项,命令行传入参数 ”—cmdopt“, 用例如果需要用到从命令行传入的参数，就调用 cmdopt 函数
pytest -s test_sample.py —cmdopt=type2 `带参数启动
"""
