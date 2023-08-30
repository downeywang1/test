from selenium.webdriver.common.by import By
from UI.my_unit_1 import MyUnin
import unittest
from UI.base_page import BasePage
# class TestAssertions():
#     def testdy(YS):
#         try:
#
#             assertTrue(self.bp.find_element(By.XPATH, '%s' % YS).is_enabled())
#             print('断言通过')
#         except Exception:
#             print('断言失败')


# a = b
def my_assertEqual(a,b):
    try:
        assert a == b
        print('√√√断言成功，%s 与 %s 相等' % (a,b))
    except AssertionError:
        print('！！！断言失败，%s 不等于 %s' % (a,b))

# 预设文本不应该出现在响应信息中
def my_assertNotIn(a,b):
    try:
        assert a not in b
        print('√√√断言成功，%s 不在html页面资源中' % a)
    except AssertionError:
        print('！！！断言失败,%s 意外出现在html页面资源中' % a)

# 预设文应该出现在响应信息中
def my_assertIn(a,b):
    try:
        assert a in b
        print('√√√断言成功，%s 在html页面资源中' % a)
    except AssertionError:
        print('！！！断言失败,%s 没有出现在html页面资源中' % a)