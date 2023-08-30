import pymysql
def testmysql():
    try:
        #连接数据库
        conn = pymysql.connect(
            host='ec2-18-140-205-254.ap-southeast-1.compute.amazonaws.com',#地址
            user='qianyi-product',#username
            password='D9W4Vai!zgR5Nr2',#密码
            database='portal',#库名
            charset='utf8'
        )
        print('数据库连接成功')
        cursor = conn.cursor()#创建游标
        cursor.execute("SELECT * FROM portal_user WHERE email='summer.li@chang-e.cn'")#SQL语句
        # print(data)
        conn.commit()
        print(cursor)
        # result = cursor.fetchall()
        for row in cursor:
            print(row)
    except Exception:
        print('数据库连接失败')

