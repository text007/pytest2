# pytest文档7-生成 html 报告

# pytest-html
"""
pip install pytest-html     安装 html
pytest —html=report.html    执行方法
"""


# html报告
"""
1.打开cmd，cd 到需要执行pytest用例的目录，执行指令：pytest —html=report.htm
2.执行完之后，在当前目录会生成一个 report.html 的报告文件
"""


# 指定报告路径
"""
1.直接执行”pytest —html=report.html”生成的报告会在当前脚本的同一路径，如果想指定报告的存放位置，放到当前脚本的同一目录下的report文件夹里
2.如果想指定执行某个.py文件用例或者某个文件夹里面的所有用例，需加个参数。具体规则参考【pytest文档2-用例运行规则】
--pytest pytest6/test_f1.py --html=./pytest7/report/report.html
--(指定运行 pytest6 文件夹下的 test_f1.py 文件，生成 html 报告，保存在 pytest7 文件夹下 report 文件夹下 report.html)
"""