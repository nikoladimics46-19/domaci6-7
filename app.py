from flask import Flask, render_template, json, request, redirect
from flask_mysqldb import MySQL, MySQLdb


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Nikola!123'
app.config['MYSQL_DB'] = 'raspored'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM raspored")
    raspored = cur.fetchall()
    return render_template('index.html', raspored=raspored)

if __name__ == "__main__":
    app.run(debug=True)