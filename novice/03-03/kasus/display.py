from flask import Flask, render_template, request
import mysql.connector as mariadb

app=Flask(__name__)

@app.route('/')
def list():
    conn=mariadb.connect(user='anan', password='anan', database='Movie')

    cur=conn.cursor()
    cur.execute("Select*from Member")

    rows=cur.fetchall()

    return render_template("display.html", rows=rows)

if __name__=='__main__':
    app.run(debug=True)