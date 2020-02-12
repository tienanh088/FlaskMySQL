from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'flaskmysql.c71lmanenhst.ap-southeast-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'akagami08'
app.config['MYSQL_DB'] = 'flaskmysql'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/add', methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        try:
            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            address = request.form.get('address')
            city = request.form.get('city')
            gender = request.form.get('gender')
            pin = request.form.get('pin')

            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO Users (firstname, lastname, address, city, gender, pin) VALUES (%s, %s, %s, %s, %s, %s)', (firstname, lastname, address, city, gender, pin))
            mysql.connection.commit()
            msg = 'Record successfully added'
        except:
            msg = 'Error in insert operation'
        finally:
            return render_template('result.html', msg = msg)

@app.route('/list')
def list():
    cur = mysql.connection.cursor()
    cur.execute('select * from Users')
    rows = cur.fetchall()
    return render_template('list.html', users = rows)