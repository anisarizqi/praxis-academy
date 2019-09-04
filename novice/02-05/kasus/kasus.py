import pymysql

db = pymysql.connect("localhost","anan","anan","Movie")

cursor = db.cursor()

sql = "SELECT Member.f_name, Movie.n_movie from Member INNER JOIN Movie ON Member.id_member = Movie.id_member WHERE Member.f_name = 'Janet Jones'"

try :
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)

except:
    print("Error: unable to fetch data")

db.close()