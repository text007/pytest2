# pytest 文档19-doctest 测试框架

#放到 xxx 函数的注释里
"""
只识别“>>>”这种符号
doctest1.py

编辑器执行
verbose参数，设置为True则在执行测试的时候会输出详细信息
--doctest.testmod(verbose=True)

cmd执行
-- python -m doctest -v doctest1.py
-- m 参数指定运行方式doctest
-- -v参数是verbose，带上-v参数相当于verbose=True

pytest运行
-- pytest -v --doctest-modules  xxx.py

"""


# doctest独立文件
"""
doctest内容也可以和代码抽离开，单独用一个.txt文件保存
在当前xxx.py同一目录新建一个xxx.txt文件，写入测试的文档，要先导入该功能，导入代码前面也要加>>>
doctest.txt
python -m doctest -v doctest.txt
"""
