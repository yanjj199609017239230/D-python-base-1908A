import allure

@allure.feature('模块名1')
@allure.story('接口名1')
@allure.title("我是VIP的方法1")
def test_demo1():
    print("我是demo1")
    allure.step('断言')
    allure.attach("实际结果:1,预期结果:1","断言",allure.attachment_type.TEXT)
    assert 1==1
# 给测试用例设计优先级 blocker  critical  normal minor  trivial
@allure.testcase("https://www.baidu.com",'百度vip')
@allure.issue("https://www.baidu.com",'百度')
@allure.severity('critical')
@allure.feature('模块名1')
@allure.story('接口名2')
@allure.title("我是VIP的方法2")

def test_demo2():
    print("我是demo2")
    assert 1==1

