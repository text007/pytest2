# pytest文档16-标记失败 xfail


# 标记为 xfail
"""
当用例a失败的时候，如果用例b和用例c都是依赖于第一个用例的结果，那可以直接跳过用例b和c的测试，直接给他标记失败 xfail
pytest.xfail(“登录不成功, 标记为xfail”)

test_05.py
"""