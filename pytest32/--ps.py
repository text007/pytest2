# pytest文档32-allure描述用例详细讲解

# allure用例描述
"""
使用方法	                    参数值	            参数说明
@allure.epic()	            epic描述	            敏捷里面的概念，定义史诗，往下是feature
@allure.feature()	        模块名称	            功能点的描述，往下是story
@allure.story()	            用户故事	            用户故事，往下是title
@allure.title(用例的标题)	    用例的标题	        重命名html报告名称
@allure.testcase()	        测试用例的链接地址	    对应功能测试用例系统里面的case
@allure.issue()	            缺陷	                对应缺陷管理系统里面的链接
@allure.description()	    用例描述	            测试用例的描述
@allure.step()	            操作步骤	            测试用例的步骤
@allure.severity()	        用例等级	            blocker，critical，normal，minor，trivial
@allure.link()	            链接	                定义一个链接，在测试报告展现
@allure.attachment()	    附件	                报告添加附件
"""


# 命令行参数
"""
选择运行你要执行epic的用例
-- pytest —alluredir ./report/allure —allure-epics=epic对大Story的一个描述性标签

选择运行你要执行features的用例
-- pytest —alluredir ./report/allure —allure-features=模块2

选择运行你要执行features的用例
-- pytest —alluredir ./report/allure —allure-stories=”用户故事：1”

test_01.py
"""
