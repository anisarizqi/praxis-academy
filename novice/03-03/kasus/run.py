from flask import Flask, render_template
import pymysql
app = Flask(__name__)
class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "anan"
        password = "anan"
        db = "Movie"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                       DictCursor)
        self.cur = self.con.cursor()
    def list_movie(self):
        self.cur.execute("SELECT id_number, f_name, p_address, id_salute FROM Member")
        result = self.cur.fetchall()
        return result
@app.route('/')
def movie():
    def db_query():
        db = Database()
        emps = db.list_movie()
        return emps
    res = db_query()
    return render_template('movie.html', result=res, content_type='application/json')