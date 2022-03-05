import pymysql


def mysql_01(sql,ip = '114.55.250.67',use = 'app',pswd = 'H2YtoxVrjV2e',mysql='xybot',port='3306'):
    # 1.连接数据库：
    con = pymysql.connect(ip,use,pswd,mysql,port)
    # 2.使用连接创建一个游标,游标可用执行sql语句
    cur = con.cursor()
    # 3.写sql语句
    # 4.执行sql
    cur.execute(sql)  #返回的结构是受影响的行数 #查询执行后会将查询结果封装到游标中
    data = cur.fetchall() #取出所有值
    # 5.提交事物
    con.commit()
    # 6.关闭游标和连接
    cur.close()
    con.close()
    return data


sql = """ select uuid,"name",encrypted_password from xybot."user"where uuid like "%24" """
data_n = mysql_01(sql)
print(data_n)