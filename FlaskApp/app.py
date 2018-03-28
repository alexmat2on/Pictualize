from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'Pictualize'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

conn = mysql.connect()
cursor=conn.cursor()

print(conn)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/signup",methods=['POST'])
def signup():
    _firstname = request.form['inputFirstName']
    _lastname = request.form['inputLastName']
    _email = request.form['intputEmail']
    _username = request.form['inputUsername']



    cursor.callproc('createUser',(_firstname,_lastname,_email,_username))

    data = cursor.fetchall()
    if len(data) is 0:
        conn.commit()
        return json.dumps({'message':'User created successfully !'}), 200
    else:
        return json.dumps({'errorrrr': str(data[0])})


if __name__ == "__main__":
    app.run()
