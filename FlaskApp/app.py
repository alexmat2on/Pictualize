from flask import escape, Flask, json, redirect, render_template, request, session, url_for

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

# INDEX PAGE
@app.route("/")
def main():
    # Check if a user is logged in and show the respective page
    if 'username' in session:
        links = ["http://lorempixel.com/640/480/food", "http://lorempixel.com/640/480/abstract", "http://lorempixel.com/640/480/sports", "http://lorempixel.com/640/480/car"]
        return render_template('home.html', picLinks = links)
    else:
        return render_template('registration.html')

@app.route("/signup", methods=['POST'])
def signup():
    # Store data from the form fields
    _firstname = request.form['createFirstName']
    _lastname = request.form['createLastName']
    _email = request.form['createEmail']
    _username = request.form['createUsername']

    # Insert the data into the Users table via a Stored Procedure
    cursor.callproc('createUser',(_firstname,_lastname,_email,_username))
    data = cursor.fetchall()
    if len(data) is 0:
        conn.commit()
        return redirect("/")
    else:
        return json.dumps({'error': str(data[0])})

@app.route("/login", methods=['GET', 'POST'])
def login():
    _username = request.form['inputUsername']

    # Verify the username is in the database
    cursor.execute("SELECT * FROM Users where userID=" + "'" + _username + "'")
    data = cursor.fetchone()
    if data is None:
        return "Invalid username"
    else:
        # When the username is in database, create a new session (cookie)
        #      for authenticating it on other pages
        if request.method == 'POST':
            session['username'] = _username;
            return redirect("/")

@app.route("/logout")
def logout():
    # Delete the user's session and return them to homepage
    session.pop('username', None)
    return redirect("/")

@app.route("/upload")
def upload():
    return render_template('upload.html')

# Secret key to encrypt session cookies
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT';

if __name__ == "__main__":
    app.run(debug=True)
