# pytest 文档1-环境准备与入门

# pytest 简介
"""
非常容易上手，入门简单，文档丰富，文档中有很多实例可以参考
能够支持简单的单元测试和复杂的功能测试
支持参数化
执行测试过程中可以将某些测试跳过（--ps.py），或者对某些预期失败的 case 标记成失败
支持重复执行 (rerun) 失败的 case
支持运行由 nose, unittest 编写的测试 case
可生成 html 报告
方便的和持续集成工具 jenkins 集成
可支持执行部分用例
具有很多第三方插件，并且可以自定义扩展
"""


# 安装 pytest
"""
pip install -U pytest   安装
pip show pytest     查看安装版本
pytest —version     查看安装的版本
"""


# pytest 运行规则
"""
查找当前目录及其子目录下以 test_*.py 或 *_test.py 文件，找到文件后，在文件中找到以 test 开头函数并执行。
"""


# pytest 用例规则
"""
测试文件以 test_ 开头（以 _test 结尾也可以）
测试类以 Test 开头，并且不能带有 init 方法
测试函数以 test_ 开头
断言使用 assert
"""
