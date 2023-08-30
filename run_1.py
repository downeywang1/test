import logging
import time
import unittest
from BeautifulReport import BeautifulReport
from logger import work_logger
from UI.Conf import send_mail
# BeautifulReportHTML报告：
if __name__ == '__main__':
    work_logger.info("生成测试脚本日志开始")

    test_a1 = unittest.defaultTestLoader.discover("C:\\Users\\bob\\PycharmProjects\\pythonProject1\\UI",
                                                  pattern="test_*.py")
    onw_time = time.strftime("%y%m%d%H%M%S", time.localtime())  # 2222
    resulu = BeautifulReport(test_a1)
    report_name = 'CB-' + str(onw_time) + '.html'
    resulu.report(filename=report_name, description='CB测试报告', report_dir='report', theme='theme_memories')
    # repott()#调用测试报告
    work_logger.info("生成测试脚本日志结束")
    work_logger.set_test_case_identifier("----------------test_0_Fiat_Deposit--------------------")  # 添加日志标识
    # send_mail.send_mail(report_name)
