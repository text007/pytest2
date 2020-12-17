# pytest文档29-allure-pytest

# allure-pytest 环境准备
"""
windows环境相关：

python 3.6版本
pytest 3.6.3版本
allure-pytest 2.8.6 最新版

使用pip安装pytest和allure-pytest,加上—index-url地址，下载会快一些
-- pip install pytest==3.6.3 —index-url https://pypi.douban.com/simple
-- pip install allure-pytest==2.8.6 —index-url https://pypi.douban.com/simple
"""


# allure命令行工具
"""
github上下载最新版https://github.com/allure-framework/allure2/releases
解压后把bin目录添加到环境变量Path下
"""


# allure使用
"""
import allure

@allure.step("xxx")

cd:pytest —alluredir ./report/allure_raw
cd:allure serve report/allure_raw

查看报告:
点 EN 按钮可以查看中文报告
打开测试套件，可以查看报告的详情，显示的还是很详细的
"""
