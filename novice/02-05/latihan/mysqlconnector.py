
from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='an', password=' ',
                                 host='127.0.0.1',
                                 database='testDB')
cnx.close()