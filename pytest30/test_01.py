import allure

@allure.feature("编辑分类文章")
class TestArticleclassify():
    '''编辑文章分类'''

    @allure.story("登录-编辑文章分类，重复保存，保存失败")
    @allure.issue("http://49.235.92.12:8080/zentao/bug-view-1.html")  # 禅道bug地址
    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-5-1.html")  # 禅道用例连接地址
    def test_edit_classify5(self, login):
        '''用例描述：编辑文章分类-输入重复的分类，保存失败，不能添加重复的
        setup: 登录login
        step1: 编辑文章分类，输入文章类别，如：计算机
        step2: 点保存按钮
        step3: 重新打开编辑页，输入：计算机
        step4: 再次点保存按钮
        assert: 保存失败，提示：已存在
        '''
        driver = login
        edit = ArticleclassifyPage(driver)
        edit.click_classify_nav()
        edit.edit_classify("计算机")
        res2 = edit.is_edit_classify_success("计算机")
        print("编辑是否成功：%s"%res2)
        assert res2  # 断言

class LoginPage(Base):

    loc_用户名 = ("id", "id_username")
    loc_密码 = ("id", "id_password")
    loc_登录按钮 = ("xpath", "//*[text()='登录']")

    # 判断登录成功
    loc_后台页面 = ("xpath", "//*[text()='后台页面']")

    @allure.step("登录")
    def login(self, username="admin", password="yoyo123456"):
        '''登录'''
        self.driver.get(login_url)
        self.send(self.loc_用户名, username)
        self.send(self.loc_密码, password)
        self.click(self.loc_登录按钮)

    @allure.step("登录结果判断")
    def is_login_success(self):
        '''判断是否登录成功 True  False'''
        result = self.is_element_exist(self.loc_后台页面)
        return result
