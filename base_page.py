"""动作封装"""
import os
import string
import time
import random
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
import unittest

# 打开浏览器
class BasePage:
    def open_browser(self):
        self.ad = webdriver.Chrome()
        self.ad.maximize_window()
        time.sleep(5)
        return self.ad
    # 加载网页
    def get(self, url):
        self.ad.get(url)

    #  元素定位
    def locator_element(self, args):
        return self.ad.find_element(*args)

    # 一组元素定位
    def locator_elements(self, args):
        return self.ad.find_elements(*args)

    # 设置值
    def send_keys(self, args, value):
        self.locator_element(args).send_keys(value)

    # 单击
    def click(self, args):
        self.locator_element(args).click()

    # 退出框架
    def switch_to_default_content(self):
        self.ad.switch_to.default_content()

    # 进入框架
    def switch_to_frame(self, frame_name):
        self.ad.switch_to.frame(frame_name)
    #打开新tab页
    def newtab(self,address):
        js = "window.open('%s')" % address
        self.ad.execute_script(js)
    #切换新的tab页
    def switchtab(self,j):
        self.ad.switch_to.window(self.ad.window_handles[j])

    # 模拟滚轮向下滑动
    def scroll_down(self, args):
        element = self.locator_element(args)
        actions = ActionChains(self.ad)
        actions.move_to_element(element).send_keys(Keys.ARROW_DOWN).perform()
        # self.ad.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #  滑动底部
    def scroll_to_bottom(self):
        actions = ActionChains(self.ad)
        actions.move_to_element(self.ad.find_element_by_tag_name('body'))
        actions.send_keys(Keys.END)
        actions.perform()

    #  滑动测数 10次
    def scroll_down1(self, args, repetitions=14):
        element = self.locator_element(args)
        actions = ActionChains(self.ad)
        for _ in range(repetitions):
            actions.move_to_element(element).send_keys(Keys.ARROW_DOWN)
        actions.perform()

    # 模拟滚轮向上滑动
    def scroll_up(self):
        actions = ActionChains(self.ad)
        actions.send_keys(Keys.ARROW_UP).perform()

    # 模拟滚轮向左滑动
    def scroll_left(self):
        actions = ActionChains(self.ad)
        actions.send_keys(Keys.ARROW_LEFT).perform()

    # 模拟滚轮向右滑动
    def scroll_right(self):
        actions = ActionChains(self.ad)
        actions.send_keys(Keys.ARROW_RIGHT).perform()

    #截图
    def screenshot(self, filename):  # filename图片名称
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        self.ad.save_screenshot(
            "C:\\Users\\bob\\PycharmProjects\\pythonProject1\\UI\\img\\" + filename+now +'.png'
        )
    #截图
    def save_img(self, img_name):
        self.ad.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"C:\\Users\\bob\\PycharmProjects\\pythonProject1\\UI\\img\\"), img_name))
    #获取登录验证码
    def redis(self):
        import redis
        # try:
        redis_conn = redis.Redis(host='ec2-18-140-205-254.ap-southeast-1.compute.amazonaws.com', port=6379, db=0)
        redis_conn.execute_command('SELECT', 11)
        keys = redis_conn.scan(match="OE_3_*", count=10000)  # 返回的是一个元组，默认count返回是10个
        # scan中count：向Redis提供有关每批要返回的密钥数的提示，此处要注意返回的数量
        # print(keys)
        a = str(keys[1])
        d = redis_conn.get(a[3:21])
        # print(a[3:21])
        s = str(d)
        # print(s[3:9])
        return s[3:9]
    #获取bank验证码
    def redisbank(self):

        import redis

        # 使用 Redis() 构造函数连接到 Redis
        redis_conn = redis.Redis(host='ec2-18-140-205-254.ap-southeast-1.compute.amazonaws.com', port=6379, db=0)

        # 读取数据
        # value1 = redis_conn.get('key1')
        # print(value1)

        # 切换到数据库 1
        redis_conn.execute_command('SELECT', 11)

        # 从数据库 1 中读取数据
        value2 = redis_conn.get('OE_8_666666@66.com')
        s = str(value2)
        # print(s[3:9])
        return s[3:9]
    def rediswithdraw(self):
        import redis

        # 使用 Redis() 构造函数连接到 Redis
        redis_conn = redis.Redis(host='ec2-18-140-205-254.ap-southeast-1.compute.amazonaws.com', port=6379, db=0)
        # 切换到数据库 11
        redis_conn.execute_command('SELECT', 11)
        # 从数据库 11 中读取数据
        value2 = redis_conn.get('OE_7_666666@66.com')
        s = str(value2)
        return s[3:9]
    #加密提现验证码
    def crypto_withdraw(self):
        import redis
        # 使用 Redis() 构造函数连接到 Redis
        redis_conn = redis.Redis(host='ec2-18-140-205-254.ap-southeast-1.compute.amazonaws.com', port=6379, db=0)
        # 切换到数据库 11
        redis_conn.execute_command('SELECT', 11)
        # 从数据库 11 中读取数据
        value2 = redis_conn.get('OE_6_666666@66.com')
        s = str(value2)
        # print(s[3:9])
        return s[3:9]
    #添加白名单验证码
    def add_address(self):
        import redis

        # 使用 Redis() 构造函数连接到 Redis
        redis_conn = redis.Redis(host='ec2-18-140-205-254.ap-southeast-1.compute.amazonaws.com', port=6379, db=0)

        # 读取数据
        # value1 = redis_conn.get('key1')
        # print(value1)

        # 切换到数据库 1
        redis_conn.execute_command('SELECT', 11)

        # 从数据库 1 中读取数据
        value2 = redis_conn.get('OE_10_666666@66.com')
        s = str(value2)
        # print(s[3:9])
        return s[3:9]
    #登录top端验证码
    def toplogin(self):
        import redis

        # 使用 Redis() 构造函数连接到 Redis
        redis_conn = redis.Redis(host='ec2-18-140-205-254.ap-southeast-1.compute.amazonaws.com', port=6379, db=0)

        # 读取数据
        # value1 = redis_conn.get('key1')
        # print(value1)

        # 切换到数据库 1
        redis_conn.execute_command('SELECT', 7)

        # 从数据库 1 中读取数据
        value2 = redis_conn.get('OE_100000024')
        s = str(value2)
        # print(s[3:9])
        return s[3:9]
    #注册手机号验证码
    def phone(self):
        import redis

        from redis import StrictRedis

        # try:
        redis_conn = redis.Redis(host='ec2-18-140-205-254.ap-southeast-1.compute.amazonaws.com', port=6379, db=0)
        redis_conn.execute_command('SELECT', 11)
        keys = redis_conn.scan(match="OS_1_+*", count=10000)  # 返回的是一个元组，默认count返回是10个
        # scan中count：向Redis提供有关每批要返回的密钥数的提示，此处要注意返回的数量
        # print(keys)
        a = str(keys[1])
        d = redis_conn.get(a[3:22])
        s = str(d)
        # print(s[3:9])
        return s[3:9]
    def email_1(self):
        import redis

        # try:
        redis_conn = redis.Redis(host='ec2-18-140-205-254.ap-southeast-1.compute.amazonaws.com', port=6379, db=0)
        redis_conn.execute_command('SELECT', 11)
        keys = redis_conn.scan(match="OE_1_*@gmail.com", count=10000)  # 返回的是一个元组，默认count返回是10个
        # scan中count：向Redis提供有关每批要返回的密钥数的提示，此处要注意返回的数量
        # print(keys)
        a = str(keys[1])
        d = redis_conn.get(a[3:26])
        s = str(d)
        # print(s[3:9])
        return s[3:9]
    #print
    def print_separator(self):
        separator = "─" * 40  # 30 Unicode horizontal line characters (─)
        return separator
    #向下滑动
    def terdown(self,d):
        js = "var q=document.documentElement.scrollTop=%d" %d
        self.ad.execute_script(js)
    # 模拟滚轮滑动到指定元素
    def scroll_to_element(self, locator):
        element = self.locate_element(locator)
        actions = ActionChains(self.ad)
        actions.move_to_element(element).perform()

    # 模拟鼠标悬停在元素上
    def hover_over_element(self, locator):
        element = self.locate_element(locator)
        actions = ActionChains(self.ad)
        actions.move_to_element(element).perform()

    # 模拟鼠标拖拽操作
    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.locate_element(source_locator)
        target_element = self.locate_element(target_locator)
        actions = ActionChains(self.ad)
        actions.drag_and_drop(source_element, target_element).perform()

    def generate_random_text(self, length):
        """
        生成指定长度的随机文本（字母和数字的组合）
                # input_box_locator = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/input')
        # figure = self.bp.generate_random_text(6)
        # self.bp.send_keys(input_box_locator, figure)方法
        """
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def generate_random_number(self, min_value, max_value):
        """
        生成指定范围内的随机整数
        """
        return random.randint(min_value, max_value)

        # prefix = "137"
        # random_number = random.randint(0, 99999999)
        # formatted_number = "{:08d}".format(random_number)
        # return int(prefix + formatted_number)

    def generate_random_number1(self, min_value, max_value):
        """
        生成指定范围内的随机整数
        """
        prefix = "137"
        random_number = random.randint(0, 99999999)
        formatted_number = "{:08d}".format(random_number)
        return int(prefix + formatted_number)

        #  生成以固定前缀"137"开头并且后面加上八位随机数字的整数
        #   random_number = self.bp.generate_random_number(0, 99999999)
        #   self.bp.send_keys((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/input'), str(random_number))
        #  方法

    def generate_random_number2(self, min_value, max_value):
        """
        生成指定范围内的随机整数
        """
        # prefix = "137"
        random_number = random.randint(0, 999)
        formatted_number = "{:08d}".format(random_number)
        return int(formatted_number)
    def fill_input_box(self, locator, text_length, min_number, max_number):
        """
        使用随机生成的文本和数字填充输入框
                self.bp.fill_input_box((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/input'),
                text_length=6,
                               min_number=0, max_number=99999999)方法
        """
        text = self.generate_random_text(text_length)
        number = self.generate_random_number(min_number, max_number)

        input_box = self.ad.find_element(*locator)
        input_box.send_keys(text)
        input_box.send_keys(str(number))

    """
            gmail_1 = self.bp.generate_random_email()
        self.bp.send_keys((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/input'), gmail_1)
        调用方法
    """

    def generate_random_email(self):
        username = ''.join(random.choices(string.ascii_lowercase, k=8))
        domain = "gmail.com"
        email = f"{username}@{domain}"
        return email







