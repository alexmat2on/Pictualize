from flask import Flask, render_template, json, request, redirect
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

@app.route("/home")
def home():
    links = ["http://lorempixel.com/640/480/food", "http://lorempixel.com/640/480/abstract", "http://lorempixel.com/640/480/sports", "http://lorempixel.com/640/480/"]
    return render_template('homepage.html', picLinks = links)


@app.route("/signup", methods=['POST'])
def signup():
    _firstname = request.form['createFirstName']
    _lastname = request.form['createLastName']
    _email = request.form['createEmail']
    _username = request.form['createUsername']

    cursor.callproc('createUser',(_firstname,_lastname,_email,_username))

    data = cursor.fetchall()
    if len(data) is 0:
        conn.commit()
        return redirect("/home")
        #return json.dumps({'message':'User created successfully !'}), 200
    else:
        return json.dumps({'errorrrr': str(data[0])})

@app.route("/login", methods=['POST'])
def login():
    # _username = "Aidan.Marks"
    _username = request.form['inputUsername']

    cursor.execute("SELECT * FROM Users where userID=" + "'" + _username + "'")
    data = cursor.fetchone()
    if data is None:
        return "Invalid username"
    else:

        return redirect("/home")

@app.route("/upload")
def upload():
    return render_template('upload.html')


        return redirect("/home")
if __name__ == "__main__":
    app.run(debug=True)
