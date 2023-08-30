import configparser


"""调用config.ini"""

config = configparser.ConfigParser()
config.read("Conf/config.ini", encoding="utf-8-sig")
smtp_cfg = config['smtp']
email_cfg = config['email']

