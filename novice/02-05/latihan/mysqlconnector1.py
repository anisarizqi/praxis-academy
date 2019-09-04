import mysql.connector

cnx = mysql.connector.connect(user='anan', password='anan',
                              host='127.0.0.1',
                              database='db_anan')  
cnx.close()