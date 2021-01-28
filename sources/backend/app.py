from flask import Flask, request, jsonify
from flask_mysql_connector import MySQL
from config import *

app = Flask(__name__)
app.config['MYSQL_USER'] = mysql_user
app.config['MYSQL_DATABASE'] = mysql_database
app.config['MYSQL_PASSWORD'] = mysql_password
app.config['MYSQL_HOST'] = mysql_host

mysql = MySQL(app)

EXAMPLE_SQL = 'select * from sys.user_summary'

@app.route('/')
def index():
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute(EXAMPLE_SQL)
    output = cur.fetchall()
    return str(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)