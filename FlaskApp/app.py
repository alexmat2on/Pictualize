import os
from flask import escape, Flask, json, redirect, render_template, request, send_from_directory, session, url_for
from flask.ext.mysql import MySQL
from werkzeug.utils import secure_filename

app = Flask(__name__)
mysql = MySQL()

# Secret key to encrypt session cookies
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT';

# File upload directory
UPLOAD_FOLDER = "static/img_user_gen";
MEME_TEMPLATES = "static/img_base";
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MEME_TEMPLATES'] = MEME_TEMPLATES

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'Pictualize'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

# INDEX PAGE
@app.route("/")
def main():
    # Check if a user is logged in and show the respective page
    if 'username' in session:
        links = []
        for filename in os.listdir("static/img_base/"):
            links.append('/uploads/' + filename)
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
        session['username'] = _username;
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
        #      for authenticating it on other pages.
        # Then return the authenticated user back to the index.
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

## UPLOAD FILE TEST!! ----------------------------------------------------------
## -----------------------------------------------------------------------------
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uptest', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['MEME_TEMPLATES'],
                               filename)

if __name__ == "__main__":
    app.run(debug=True)
