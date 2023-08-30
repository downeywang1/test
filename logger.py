"""日志展示"""
# import logging
# import os
# import time
# import schedule
#
#
# class WorkLogger():
#     def __init__(self, path, claevel=logging.INFO, Flevel=logging.ERROR):
#         log_folder = os.path.dirname(path)
#         os.makedirs(log_folder, exist_ok=True)
#         log_file = f"{os.path.splitext(path)[0]}_{time.strftime('%Y%m%d%H%M%S')}.log"
#
#         self.logger = logging.getLogger(path)
#         self.logger.setLevel(logging.DEBUG)
#         fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#         # 终端显示
#         sh = logging.StreamHandler()
#         sh.setFormatter(fmt)
#         sh.setLevel(claevel)
#
#         # 添加日志处理器到logger
#         self.logger.addHandler(sh)
#
#         # 日志文件
#         fh = logging.FileHandler(log_file, encoding="utf-8", mode="a")
#         # fh = logging.FileHandler(path, encoding="utf-8", mode="a")
#         fh.setFormatter(fmt)
#         fh.setLevel(Flevel)
#
#         self.logger.addHandler(sh)
#         self.logger.addHandler(fh)
#
#     def debug(self, message):
#         self.logger.debug(message)
#
#     def info(self, message):
#         self.logger.info(message)
#
#     def war(self, message):
#         self.logger.warning(message)
#
#     def error(self, message):
#         self.logger.error(message)
#
#     def cri(self, message):
#         self.logger.critical(message)
#
#
# work_logger = WorkLogger("./img/test_DTC.log", logging.DEBUG, logging.INFO,)

# schedule.every().week.do(self.run_cleanup_job, log_folder)

# def run_cleanup_job(self, log_folder):
#     now = time.time()
#     days_to_keep = 1
#     for file_name in os.listdir(log_folder):
#         file_path = os.path.join(log_folder, file_name)
#         if os.path.isfile(file_path):
#             # 获取文件创建时间
#             creation_time = os.path.getctime(file_path)
#             # 计算文件存在的天数
#             days_since_creation = (now - creation_time) / (24 * 60 * 60)
#             if days_since_creation >= days_to_keep:
#                 # 删除过期的日志文件
#                 os.remove(file_path)



# 在需要记录日志的地方使用 work_logger 对象
# work_logger.debug("Debug message")
# work_logger.info("Info message")
# work_logger.war("Warning message")
# work_logger.error("Error message")
#
# # 循环执行定时任务
# while True:
#     schedule.run_pending()
#     if not schedule.jobs:
#         break



#
# def cleanup_old_logs(log_folder, days_to_keep=7):
#     now = time.time()
#     for file_name in os.listdir(log_folder):
#         file_path = os.path.join(log_folder, file_name)
#         if os.path.isfile(file_path):
#             # 获取文件创建时间
#             creation_time = os.path.getctime(file_path)
#             # 计算文件存在的天数
#             days_since_creation = (now - creation_time) / (24 * 60 * 60)
#             if days_since_creation >= days_to_keep:
#                 # 删除过期的日志文件
#                 os.remove(file_path)
#
#
# def run_cleanup_job(log_folder):
#     cleanup_old_logs(log_folder)
#
#
# # 配置日志记录器
# log_folder = "./img"
# log_file = os.path.join(log_folder, "test_DTC.log")
#
# logging.basicConfig(filename=log_file, level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')
#
# # 启动定时任务，每周执行一次清理任务
# schedule.every().week.do(run_cleanup_job, log_folder)
#
# # 在需要记录日志的地方使用 logger
# logger = logging.getLogger(__name__)
# logger.debug("Debug message")
# logger.info("Info message")
# logger.warning("Warning message")
# logger.error("Error message")
#
# # 循环执行定时任务
# while True:
#     schedule.run_pending()
#     time.sleep(1)


# 读取EXCEL实现（data）

##import pandas as pd
#
# def read_excel(file, **kwargs):
#     data_dict = []
#     try:
#         data = pd.read_excel(file, **kwargs)
#         data_dict = data.to_dict('records')
#     finally:
#         return data_dict
# ————————————————

# 调用方法
# sheet1 = read_excel('baidu_fanyi.xlsx')
# sheet2 = read_excel('baidu_fanyi.xlsx', sheet_name='Sheet2')
# print(sheet1)
# print(sheet2)


# data = pd.read_excel('baidu_fanyi.xlsx')
# data['sign'] = data["req.from"] +'.aaaaa.' + data["req.to"]
# data_dict = data.to_dict('records')
# print(data_dict)

import logging
import os
import time


class WorkLogger():
    def __init__(self, path, claevel=logging.INFO, Flevel=logging.ERROR):
        log_folder = os.path.dirname(path)
        os.makedirs(log_folder, exist_ok=True)
        log_file = f"{os.path.splitext(path)[0]}_{time.strftime('%Y%m%d%H%M%S')}.log"

        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # 终端显示
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(claevel)


        # 添加日志处理器到logger
        self.logger.addHandler(sh)

        # 日志文件
        fh = logging.FileHandler(log_file, encoding="utf-8", mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

        # 记录当前测试用例的标识符
        self.test_case_identifier = None

    def set_test_case_identifier(self, identifier):
        self.test_case_identifier = identifier

    def debug(self, message):
        self.logger.debug(self._add_test_case_identifier(message))

    def info(self, message):
        self.logger.info(self._add_test_case_identifier(message))
        return message

    def war(self, message):
        self.logger.warning(self._add_test_case_identifier(message))

    def error(self, message):
        self.logger.error(self._add_test_case_identifier(message))

    def cri(self, message):
        self.logger.critical(self._add_test_case_identifier(message))

    def _add_test_case_identifier(self, message):
        if self.test_case_identifier:
            return f"{self.test_case_identifier} - {message}"
        return message


work_logger = WorkLogger("./log/test_CB.log", logging.DEBUG, logging.INFO)







#
# @classmethod
# def setUpClass(cls):
#     # 配置日志
#     logging.basicConfig(filename='test.log', level=logging.INFO,
#                         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# def setUp(self):
#     self.setUpClass()
#     self.logger = logging.getLogger(__name__)
#     # 获取Logger对象