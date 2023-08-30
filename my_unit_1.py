"""框架程序"""

import time
import unittest
from base_page import BasePage



class MyUnin(unittest.TestCase):
    def setUp(self) -> None:
        self.bp = BasePage()
        self.ab = self.bp.open_browser()
        self.bp.get('https://wallet.dev.cb-web3.com/login')
        self.ab.implicitly_wait(15)
        # self.ab = webdriver.Chrome()
        # self.bp = BasePage()
        # self.bp.open_browser()
        # self.bp.get('https://wallet.dev.dtcpayment.net/login')

        print(self.bp.print_separator(),"开始测试")

    def tearDown(self) -> None:
        time.sleep(5)
        self.ab.close()

        print(self.bp.print_separator(),"在测试用例之后执行：关闭浏览器")



    @classmethod
    def setUpClass(cls) -> None:

        print("在每个类之前执行：初始化日志对象，创建数据库连接-----")

    @classmethod
    def tearDownClass(cls) -> None:
        print("在每个类之后执行：销毁日志对象，销毁数据库连接-----")
