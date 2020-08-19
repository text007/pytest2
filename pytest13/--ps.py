# pytest文档13-allure2 生成html报告

# pytest-allure-adaptor 下载
"""
pip install pytest-allure-adaptor
"""


# 生成 xml 报告
"""
pytest -s -q --alluredir report
如果不指定路径，默认在当前目录下新建一个report目录
"""


# 安装 Command Tool
"""
https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.7.0/allure-2.7.0.zip
\allure-2.7.0\bin文件夹下路径设置为系统环境变量path

依赖java环境
"""


# 运行allure2
"""
allure generate report/ -o report/html
"""
