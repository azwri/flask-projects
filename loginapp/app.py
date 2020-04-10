from flask import Flask, render_template, request
import pymysql
import yaml

# Configure db
db = pymysql.connect('localhost', 'user', 'password', 'databasename')

# flask app
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    cursor = db.cursor()
    if request.method == 'POST':
        user_detail = request.form
        name = user_detail['name']
        email = user_detail['email']
        cursor.execute('INSERT INTO users(name, email) VALUES(%s, %s)',(name, email))
        db.commit()
        result = cursor.execute('SELECT * FROM users')
        if result > 0:
            detail = cursor.fetchall()
            cursor.close()
            return render_template('users.html', detail=detail)
    return render_template('index.html')

@app.route('/users/')
def users():
    cursor = db.cursor()
    result = cursor.execute('SELECT * FROM users')
    if result > 0:
        detail = cursor.fetchall()
        return render_template('users.html', detail=detail)
    return render_template('users.html')
    
if __name__ == '__main__':
    app.run(debug=True)