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

print(conn)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/",methods=['POST'])
def signUp():

    _firstname = request.form['inputFirstName']
    _lastname = request.form['inputLastName']
    _email = request.form['intputEmail']
    _username = request.form['inputUsername']

    # validate the received values
    if _firstname and _lastname and _email and _username:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})



if __name__ == "__main__":
    app.run()
