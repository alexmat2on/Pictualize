import os
import hashlib
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from math import ceil

from random import randint
from flask import escape, Flask, json, redirect, render_template, request, send_from_directory, session, url_for, flash
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

# APP ROUTES -------------------------------------------------------------------
@app.route("/")
def main():
    # Check if a user is logged in and show the respective page
    if 'username' in session:
        links = []
        for filename in os.listdir("static/img_base/"):
            links.append('/static/img_base/' + filename)
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
    cursor.callproc('createUser', (_firstname,_lastname,_email,_username))
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
        return render_template('registration.html', errors="Invalid username")
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

@app.route("/new")
def new():
    if 'username' in session:
        cursor.execute("SELECT imageID FROM Images WHERE img_type='TEMPL'")
        data = cursor.fetchall()
        templates = []
        for row in data:
            templates.append(row[0])

        return render_template('create.html', templates = templates)
    else:
        return redirect("/")

@app.route("/makePost", methods=['POST'])
def makePost():
    if 'username' in session:
        # Fetch values from request
        topString = request.form['top_text']
        botString = request.form['bot_text']
        imageID = request.form['image_id']

        # Build an ID/filename for the post-processed image
        postImageID = session['username'] + topString + botString + imageID
        postExtension = imageID[-4:]
        postFilename = hashlib.md5(postImageID.encode('utf-8')).hexdigest() + postExtension

        # Draw the text onto the image
        print(imageID)
        print("static/img_base/" + imageID)
        openTemplate = Image.open("static/img_base/" + imageID)
        drawTemplate = ImageDraw.Draw(openTemplate)

        drawText(openTemplate, drawTemplate, topString, "TOP")
        drawText(openTemplate, drawTemplate, botString, "BOT")

        openTemplate.save('static/img_user_gen/' + postFilename)

        # Store the results as a post in the database
        query = "SELECT"
        cursor.callproc('uploadImage', (postFilename, 'MACRO', session['username']))
        cursor.callproc('makePost', (session['username'], postFilename, imageID, topString, botString))
        conn.commit()

        return redirect("/")

@app.route("/following")
def following():
    if 'username' in session:
        return render_template('following.html')
    else:
        return redirect("/")

@app.route("/profile")
def profile():
    if 'username' in session:
        return render_template("profile.html")
    else:
        return redirect("/")

@app.route("/godview")
def godview():
    cursor.execute("SHOW TABLES")
    showTables = cursor.fetchall()

    description = "GodView is a nifty developer's web tool to dump and inspect the state of all the tables in the database. With great power comes great responsibility, young padawan."

    return render_template("godview.html", showTables = showTables, description = description)

@app.route("/godview/<tableName>")
def godviewTable(tableName):
    if 'username' in session:
        cursor.execute("SHOW TABLES")
        showTables = cursor.fetchall()

        getTable = "SELECT * FROM " + tableName;
        cursor.execute(getTable)
        table = cursor.fetchall()
        tableMeta = cursor.description

        return render_template("godview.html", \
                                showTables = showTables, \
                                table = table, \
                                tableMeta = tableMeta, \
                                tableName = tableName)
    else:
        return redirect("/")

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if 'username' in session:
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            # file = request.files['file']
            filelist = request.files.getlist("file")
            print(len(filelist))
            print(filelist)
            for file in filelist:
                # if user does not select file, browser also
                # submit a empty part without filename
                if file.filename == '':
                    flash('No selected file')
                    return redirect(request.url)
                if file and allowed_file(file.filename):
                    # filename = secure_filename(file.filename)
                    stringToHash = file.filename + session['username'] + str(randint(0, 10000))
                    fileExtension = "." + file.filename.rsplit('.', 1)[1].lower()

                    filename = hashlib.md5(stringToHash.encode('utf-8')).hexdigest() + fileExtension
                    file.save(os.path.join(app.config['MEME_TEMPLATES'], filename))

                    cursor.callproc('uploadImage', (filename, 'TEMPL', session['username']))
                    conn.commit()

            return redirect(url_for('uploaded_template',
                                 filename=filename))

        return render_template('upload.html')
    else:
        return redirect("/")

@app.route('/templates/<filename>')
def uploaded_template(filename):
    return send_from_directory(app.config['MEME_TEMPLATES'],
                               filename)

## END APP ROUTES --------------------------------------------------------------

# AUXILLIARY FUNCTIONS ---------------------------------------------------------
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def drawText(img, draw, textstr, position):
    # Make font size 7% of the image width
    font = ImageFont.truetype("static/impact.ttf", ceil(img.size[0] * 0.07))

    text_x = font.getsize(textstr)[0]
    text_y = font.getsize(textstr)[1]
    x = (img.size[0] - text_x) / 2

    if position == "TOP":
        y = 5
    elif position == "BOT":
        y = img.size[1] - text_y - 10

    if text_x >= img.size[0]:
        sp = textstr.split()
        words = len(sp)
        topline = ""
        nextline = ""
        for i in range(0, words // 2):
            topline += sp[i] + " "

        for i in range(words // 2, words):
            nextline += sp[i] + " "

        nextx = (img.size[0] - font.getsize(nextline)[0]) / 2
        draw.text((nextx + 2, y + text_y + 8), nextline, (0, 0, 0), font=font)
        draw.text((nextx, y + text_y + 5), nextline, (255, 255, 255), font=font)

        textstr = topline
        x = (img.size[0] - font.getsize(textstr)[0]) / 2

    draw.text((x + 2, y + 2), textstr, (0, 0, 0), font=font)
    draw.text((x, y), textstr, (255, 255, 255), font=font)

if __name__ == "__main__":
    app.run(debug=True)
