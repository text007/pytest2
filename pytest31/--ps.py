# pytest文档31-allure标记用例级别severity

# 用例等级
"""
allure对用例的等级划分成五个等级

-- blocker　   阻塞缺陷（功能未实现，无法下一步）
-- critical　　严重缺陷（功能点缺失）
-- normal　　  一般缺陷（边界情况，格式错误）
-- minor　     次要缺陷（界面错误与ui需求不符）
-- trivial　　 轻微缺陷（必须项无提示，或者提示不规范）

pytest —alluredir ./report/allure
allure serve ./report/allure

重新执行用例，查看报告-图表
"""


# allure命令行参数allure-severities
"""
critical级别的测试用例

-- pytest —alluredir ./report/allure —allure-severities blocker,critical

也可以这样写

-- pytest —alluredir=./report/allure —allure-severities=blocker,critical

如果只执行blocker级别的用例

-- pytest —alluredir=./report/allure —allure-severities=blocker
"""
