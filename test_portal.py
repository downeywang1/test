"""测试用例"""

import time
import unittest
from BeautifulReport import BeautifulReport
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from my_unit_1 import MyUnin
from logger import work_logger,WorkLogger
class TetePoratl(MyUnin):
    pass
    age = 16
    @unittest.skipIf(age <= 18, reason="忽略--用户侧注册")
    @BeautifulReport.add_test_img('Wallet-Register')
    def test_01_Register(self):
        try:
            work_logger.set_test_case_identifier("----------------test_01_Wallet_Register--------------------")
            self.bp.click((By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/span[1]/span'))
            work_logger.info('点击注册')
            print(self.bp.print_separator(),'点击注册')
            time.sleep(2)
            self.bp.click((By.XPATH,'/html/body/div[1]/div/div[3]/div[3]/div[1]/div/div/div/img[1]'))
            work_logger.info('点击个人')
            print(self.bp.print_separator(),'点击个人')
            time.sleep(2)
            self.bp.click((By.XPATH,'(//input[@type="text"])[1]'))
            work_logger.info('点击Nationality输入框')
            print(self.bp.print_separator(),'点击Nationality输入框')
            time.sleep(2)
            self.bp.send_keys((By.XPATH,'(//label[@class="search-section "])[2]'),'SGP')
            work_logger.info('搜索SGP')
            print(self.bp.print_separator(),'搜索SGP')
            time.sleep(2)
            self.bp.click((By.XPATH,'(//span[text()="SGP - Singapore"])[2]'))
            work_logger.info('选择SGP')
            print(self.bp.print_separator(),'选择SGP')
            time.sleep(2)
            self.bp.click((By.XPATH,'(//input[@type="text"])[2]'))
            work_logger.info('点击Residence输入框')
            print(self.bp.print_separator(),'点击Residence输入框')
            time.sleep(2)
            self.bp.send_keys((By.XPATH,'(//label[@class="search-section "])[2]'),'SGP')
            work_logger.info('搜索SGP')
            print(self.bp.print_separator(),'搜索SGP')
            time.sleep(2)
            self.bp.click((By.XPATH,'(//span[text()="SGP - Singapore"])[2]'))
            work_logger.info('选择SGP')
            print(self.bp.print_separator(),'选择SGP')
            time.sleep(2)
            self.bp.click((By.XPATH,'//span[text()="Next"]'))
            work_logger.info('点击提交')
            print(self.bp.print_separator(),'点击提交')
            time.sleep(2)
            self.bp.click((By.XPATH,'//input[@readonly="readonly"]'))
            work_logger.info('选择手机号')
            print(self.bp.print_separator(),'选择手机号')
            time.sleep(2)
            self.bp.send_keys((By.XPATH,'//label[@class="search-section "]'),'Singapore')
            work_logger.info('搜索新加坡区号')
            print(self.bp.print_separator(),'搜索新加坡区号')
            time.sleep(2)
            self.bp.click((By.XPATH,'//span[@style="float: left;"]'))
            work_logger.info('选择新加坡区号')
            print(self.bp.print_separator(),'选择新加坡区号')
            time.sleep(2)
            number6=self.bp.generate_random_number1(0,9)
            self.bp.send_keys((By.XPATH,'(//input[@autocomplete="off"])[2]'),number6)
            work_logger.info('注册手机号为：%s'%number6)
            print(self.bp.print_separator(),'注册手机号为：%s'%number6)
            time.sleep(2)
            self.bp.click((By.XPATH,'(//span[text()="Get Code"])[1]'))
            work_logger.info('获取注册手机号验证码')
            print('获取手机号验证码')
            time.sleep(3)
            self.bp.send_keys((By.XPATH,'(//input[@autocomplete="off"])[3]'),self.bp.phone())
            work_logger.info('验证码为：'+self.bp.phone())
            print(self.bp.print_separator(),'验证码为'+self.bp.phone())
            time.sleep(2)
            Email=self.bp.generate_random_email()
            self.bp.send_keys((By.XPATH,'(//input[@type="text"])[4]'),Email)
            work_logger.info('注册邮箱为：%s'%Email)
            print('注册邮箱为：%s'% Email)
            time.sleep(2)
            self.bp.click((By.XPATH,'(//span[text()="Get Code"])[1]'))
            work_logger.info('获取验证码')
            print(self.bp.print_separator(),'获取验证码')
            time.sleep(3)
            self.bp.send_keys((By.XPATH,'(//input[@type="text"])[5]'),self.bp.email_1())
            work_logger.info('验证码为：'+self.bp.email_1())
            print(self.bp.print_separator(),'验证码为：'+self.bp.email_1())
            time.sleep(2)
            self.bp.click((By.XPATH,'(//span[@class="el-checkbox__inner"])'))
            work_logger.info('点击同意用户协议')
            print(self.bp.print_separator(),'点击同意用户协议')
            time.sleep(2)
            self.bp.click((By.XPATH,'//span[text()="Next"]'))
            work_logger.info('点击提交')
            print(self.bp.print_separator(),'点击提交')
            time.sleep(2)
            self.bp.send_keys((By.XPATH,'//input[@type="password"]'),'Downeywang123')
            work_logger.info('输入密码')
            print(self.bp.print_separator(),'输入密码')
            time.sleep(2)
            self.bp.send_keys((By.XPATH,'//input[@type="text"]'),'Downeywang123')
            work_logger.info('输入反钓鱼码')
            print(self.bp.print_separator(),'输入反钓鱼码')
            time.sleep(2)
            self.bp.click((By.XPATH,'(//span[text()="Next"])'))
            work_logger.info('点击提交')
            print(self.bp.print_separator(),'点击提交')
            '''注册成功'''
            self.bp.save_img('Wallet-Register')
            work_logger.info('截图')
        except Exception:
            self.bp.save_img('Register-false-01')
            # 捕获你期望的异常类型
            work_logger.error("Deposit_USD-------Error message")
            self.fail("Test case failed: " + str(Exception()))

    @unittest.skipIf(age<=18,reason='展示--kyc认证')
    @BeautifulReport.add_test_img('KYC-SUCCESS')
    def test_02_KYC(self):
        try:
            work_logger.set_test_case_identifier("----------------test_01_Portal_KYC--------------------")
            self.bp.newtab('https://portal.dev.cb-web3.com/login')
            self.bp.switchtab(1)
            time.sleep(1)
            self.bp.click((By.XPATH,
                           '/html/body/div[1]/div/div/div/div/section/main/div/div/div[2]/form/div[1]/div/div[2]/div/div/span/input'))
            work_logger.info('点击Email输入框')
            print(self.bp.print_separator(),'点击Email输入框')
            time.sleep(1)
            self.bp.send_keys((By.XPATH,
                               '/html/body/div[1]/div/div/div/div/section/main/div/div/div[2]/form/div[1]/div/div[2]/div/div/span/input'),
                              '1234@dtc.com')
            work_logger.info('输入Email')
            print(self.bp.print_separator(),'输入Email')
            time.sleep(2)
            self.bp.click((By.XPATH,
                           '/html/body/div[1]/div/div/div/div/section/main/div/div/div[2]/form/div[2]/div/div[2]/div/div/span/input'))
            work_logger.info('点击Password输入框')
            print(self.bp.print_separator(),'点击Password输入框')
            time.sleep(1)
            self.bp.send_keys((By.XPATH, '//*[@id="pd"]'), 'Downeywang123')
            work_logger.info('输入密码')
            print(self.bp.print_separator(),'输入密码')
            time.sleep(1)
            self.bp.click((By.XPATH,
                           '//*[@id="root"]/div/div/div/div/section/main/div/div/div[2]/form/div[3]/div/div/div/div/button/span'))
            work_logger.info('点击Log In')
            print(self.bp.print_separator(),'点击Log In')
            time.sleep(2)
            self.bp.send_keys((By.XPATH, '(//input[@class="ant-input css-15alr0j otp-code-input"])[1]'),
                              self.bp.toplogin())
            work_logger.info('验证码为：' + self.bp.toplogin())
            print(self.bp.print_separator(),'验证码为：' + self.bp.toplogin())
            work_logger.info('登陆成功，进入首页')
            print(self.bp.print_separator(),'登陆成功，进入首页')
            time.sleep(2)
            self.bp.click((By.XPATH,'//img[@alt="risk"]'))
            work_logger.info('点击进入财务系统')
            print(self.bp.print_separator(),'点击进入财务系统')
            time.sleep(2)
            self.bp.click((By.XPATH,'(//span[@class="ant-menu-title-content"])[1]'))
            work_logger.info('点击Onboarding KYC')
            print(self.bp.print_separator(),'点击Onboarding KYC')
            time.sleep(2)
            self.bp.click((By.XPATH,'//span[text()="Individual Client"]'))
            work_logger.info('点击Individual Client')
            print(self.bp.print_separator(),'点击Individual Client')
            time.sleep(3)
            self.bp.click((By.XPATH,'/html/body/div[1]/div/div/div/div/main/div/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[1]/div/div/button/span'))
            work_logger.info('点击Verify')
            print(self.bp.print_separator(),'点击Verify')
            time.sleep(2)
            first=self.bp.generate_random_text(4)
            self.bp.send_keys((By.XPATH,'(//input[@type="text"])[2]'),first)
            work_logger.info('输入First Name')
            print(self.bp.print_separator(),'输入First Name')
            time.sleep(2)
            last = self.bp.generate_random_text(4)
            self.bp.send_keys((By.XPATH,'(//input[@type="text"])[3]'),last)
            work_logger.info('输入Last Name')
            print(self.bp.print_separator(),'输入Last Name')
            time.sleep(2)
            full = self.bp.generate_random_text(4)
            self.bp.send_keys((By.XPATH,'(//input[@type="text"])[4]'),full)
            work_logger.info('输入Full Name')
            print(self.bp.print_separator(),'输入Full Name')
            time.sleep(2)
            self.bp.click((By.XPATH,'(//input[@type="search"])[6]'))
            work_logger.info('点击Gender')
            print(self.bp.print_separator(),'点击Gender')
            time.sleep(2)
            self.bp.click((By.XPATH,'(//div[@class="ant-select-item-option-content"])[1]'))
            work_logger.info('选择Male')
            print(self.bp.print_separator(),'选择Male')
            time.sleep(2)
            self.bp.click((By.XPATH,'(//input[@placeholder="Select date"])[1]'))
            work_logger.info('点击Date of Birth')
            print(self.bp.print_separator(),'点击Date of Birth')
            time.sleep(2)
            self.bp.click((By.XPATH,'(//div[@class="ant-picker-cell-inner"])[33]'))
            work_logger.info('选择27号')
            print(self.bp.print_separator(),'选择27号')
            time.sleep(2)
            Email = self.bp.generate_random_email()
            self.bp.send_keys((By.XPATH,'(//input[@type="text"])[12]'),Email)
            work_logger.info('输入Email')
            print(self.bp.print_separator(),'输入Email')
            time.sleep(2)
            self.bp.click((By.XPATH,'(//input[@type="search"])[9]'))
            work_logger.info('点击ID Type')
            print(self.bp.print_separator(),'点击ID Type')
            time.sleep(2)
            self.bp.click((By.XPATH,'(//div[@class="ant-select-item-option-content"])[5]'))
            work_logger.info('选择Other ID')
            print(self.bp.print_separator(),'选择Other ID')
            time.sleep(2)
            number=self.bp.generate_random_number2(0,9999)
            self.bp.send_keys((By.XPATH,'(//input[@type="text"])[14]'),number)
            work_logger.info('ID Number为：%s' % number)
            print(self.bp.print_separator(),'ID Number为：%s' % number)
            time.sleep(2)
            self.bp.click((By.XPATH,'(//input[@type="search"])[11]'))
            work_logger.info('点击Country')
            print(self.bp.print_separator(),'点击Country')
            time.sleep(2)
            self.bp.click((By.XPATH,'(//div[text()="AFG - Afghanistan"])[1]'))
            work_logger.info('选择AFG - Afghanistan')
            print(self.bp.print_separator(),'选择AFG - Afghanistan')
            time.sleep(2)
            self.bp.send_keys((By.XPATH,'(//input[@type="text"])[18]'),'Singapore')
            work_logger.info('Address line1输入Singapore')
            print(self.bp.print_separator(),'Address line1输入Singapore')
            time.sleep(2)
            self.bp.click((By.XPATH,'(//button[@type="button"])[7]'))
            work_logger.info('点击提交')
            print(self.bp.print_separator(),"点击提交")
            time.sleep(2)
            self.bp.save_img('KYC-SUCCESS')
            work_logger.info('截图')
        except Exception:
            self.bp.save_img('Register-false-02')
            # 捕获你期望的异常类型
            work_logger.error("Deposit_USD-------Error message")
            self.fail("Test case failed: " + str(Exception()))