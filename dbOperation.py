import pymysql


def connectDb():
    conn = pymysql.connect(host = "localhost",
                       user = "root",
                       password = "root",
                       database = "python_test",
                       charset = "utf8mb4")
    return conn


def insertData(conn, values):
    cursor = conn.cursor()
    sql = "insert into house_info(price)values('2');"
    cursor.execute(sql)
    conn.commit()