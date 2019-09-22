import pytest
# 先执行方法然后调用这方法最后输入命令allure generate ./report/xml -o ./report/html --clean
pytest.main(["allure_demo/",'-v','--alluredir','report/xml'])
# 显示测试用例报告
