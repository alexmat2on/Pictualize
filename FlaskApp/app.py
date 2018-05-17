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
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# File upload directory
USER_FOLDER = "static/img_user_gen"
MEME_TEMPLATES = "static/img_base"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['USER_FOLDER'] = USER_FOLDER
app.config['MEME_TEMPLATES'] = MEME_TEMPLATES
app.config['USER_ASSETS'] = "static/img_user_assets"
app.config['APP_ASSETS'] = "static/img_assets"

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
        # Get the 30 most recent posts
        cursor.execute("SELECT postID, userID, post_image FROM Posts ORDER BY post_ts DESC LIMIT 30")
        data = cursor.fetchall()
        posts = []

        for row in data:
            posts.append(row)

        return render_template('home.html', recentPosts = posts)
    else:
        return render_template('registration.html')

@app.route("/save/<postID>")
def savePost(postID):
    if 'username' in session:
        cursor.execute("SELECT post_image FROM Posts WHERE postID='" + postID + "'")
        postimg = cursor.fetchone()[0]
        cursor.execute("INSERT INTO SavedImages VALUES('" + session['username'] + "', '" + postimg + "')")
        conn.commit()
        return redirect("/profile/saved")
    else:
        return redirect("/")

@app.route("/fork/<postID>")
def forkPost(postID):
    if 'username' in session:
        cursor.execute("SELECT template_image, text_top, text_bot FROM Posts WHERE postID='" + postID + "'")
        data = cursor.fetchone()
        print(data)
        ti = data[0]
        tt = data[1]
        tb = data[2]

        cursor.execute("SELECT imageID FROM SavedImages JOIN Images ON SavedImages.saved_imageID=Images.imageID WHERE img_type='TEMPL' AND userID='" + session['username'] + "'")
        data = cursor.fetchall()
        templates = []
        for row in data:
            templates.append(row[0])

        return render_template('create.html', templates = templates, selected_image = ti, topTxt = tt, botTxt = tb)
    else:
        return redirect("/")

@app.route("/reply/<postID>")
def replyPost(postID):
    if 'username' in session:
        return redirect("/profile/saved")
    else:
        return redirect("/")


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
        cursor.execute("SELECT imageID FROM SavedImages JOIN Images ON SavedImages.saved_imageID=Images.imageID WHERE img_type='TEMPL' AND userID='" + session['username'] + "'")
        data = cursor.fetchall()
        templates = []
        for row in data:
            templates.append(row[0])

        return render_template('create.html', templates = templates, selected_image = templates[0])
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

        print("MAKE TESTING: ", postFilename, imageID, topString, botString)
        # Store the results as a post in the database
        cursor.callproc('uploadImage', (postFilename, 'MACRO'))
        cursor.callproc('makePost', (session['username'], postFilename, imageID, topString, botString))
        conn.commit()

        return redirect("/")

@app.route("/following")
def following():
    if 'username' in session:
        cursor.execute("SELECT followed_userID FROM Follows WHERE userID='" + session['username'] + "'")
        data = cursor.fetchall()
        following = []

        for row in data:
            following.append(row[0])

        return render_template('following.html', followingList = following)
    else:
        return redirect("/")

@app.route("/follow/<userID>")
def follow(userID):
    if 'username' in session:
        cursor.execute("SELECT * FROM Users WHERE userID='" + userID + "'")
        data = cursor.fetchall()
        if (len(data) == 0):
            return "user does not exist"
        else:
            cursor.execute("INSERT INTO Follows VALUES ('" + session['username'] + "', '" + userID + "')")
            conn.commit()
            return redirect("/following")

@app.route("/profile/followers")
def prof_followers():
    if 'username' in session:
        cursor.execute("SELECT * FROM Follows WHERE followed_userID='" + session['username'] + "'")
        data = cursor.fetchall()

        followers = []
        for row in data:
            followers.append(row[0])

        return render_template("profile_user.html", followerList=followers)
    else:
        return redirect("/")

@app.route("/profile/saved")
def prof_saved():
    if 'username' in session:
        cursor.execute("SELECT imageID FROM SavedImages JOIN Images ON SavedImages.saved_imageID=Images.imageID WHERE userID='" + session['username'] + "' AND img_type='MACRO'")
        data = cursor.fetchall()

        savedPosts = []
        for row in data:
            savedPosts.append(row[0])

        return render_template("profile_user.html", savedPostsList=savedPosts)
    else:
        return redirect("/")

@app.route("/profile/library")
def prof_library():
    if 'username' in session:
        cursor.execute("SELECT imageID FROM SavedImages JOIN Images ON SavedImages.saved_imageID=Images.imageID WHERE userID='" + session['username'] + "' AND img_type='TEMPL'")
        data = cursor.fetchall()

        tempLib = []
        for row in data:
            tempLib.append(row[0])

        return render_template("profile_user.html", tempLibList=tempLib)
    else:
        return redirect("/")

@app.route("/profile/<userID>")
def profile(userID):
    if 'username' in session:
        return render_template("profile.html", userID = userID)
    else:
        return redirect("/")

@app.route("/profile/<userID>/avatar")
def getAvatar(userID):
    if 'username' in session:
        cursor.execute("SELECT avatarID FROM Profiles WHERE userID='" + userID + "'")
        data = cursor.fetchall()
        if (len(data) != 0):
            avatar = data[0][0]
        else:
            # If user has not set avatar, use default
            return send_from_directory(app.config["APP_ASSETS"], "avatar.png")

        return send_from_directory(app.config["USER_ASSETS"], avatar)
    else:
        return redirect("/")

@app.route("/profile/<userID>/upload_avatar", methods=['POST'])
def uploadAvatar(userID):
    if 'username' in session:
        if session['username'] == userID:
            print("WE MADE IT THIS FAR")
            if request.method == "POST":
                file = request.files['avatar']
                if file and allowed_file(file.filename):
                    stringToHash = session['username']
                    fileExtension = "." + file.filename.rsplit('.', 1)[1].lower()

                    filename = hashlib.md5(stringToHash.encode('utf-8')).hexdigest() + fileExtension

                    file.save(os.path.join(app.config['USER_ASSETS'], filename))
                    cursor.execute("SELECT * FROM Profiles JOIN Images ON Profiles.avatarID=Images.imageID WHERE Profiles.userID='" + userID + "'")

                    data = cursor.fetchall()
                    print("UPLOADED!! ", data)
                    if (len(data) == 0):
                        cursor.callproc('uploadImage', (filename, 'AVATR'))
                        cursor.callproc('setAvatar', (filename, userID))
                        conn.commit()

            return redirect("/profile/" + userID)
        else:
            return "Hacker, no hacking!"
    else:
        return redirect("/")

@app.route("/godview")
def godview():
    if session['username'] == 'god':
        cursor.execute("SHOW TABLES")
        showTables = cursor.fetchall()

        description = "GodView is a nifty developer's web tool to dump and inspect the state of all the tables in the database. With great power comes great responsibility, young padawan."

        return render_template("godview.html", showTables = showTables, description = description)
    else:
        return "Blasphemy! Begone ye false idol!"

@app.route("/godview/<tableName>")
def godviewTable(tableName):
    if session['username'] == 'god':
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
        return "Blasphemy! Begone ye false idol!"

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if 'username' in session:
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            filelist = request.files.getlist("file")
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

                    cursor.callproc('uploadImage', (filename, 'TEMPL'))
                    cursor.callproc('saveImage', (filename, session['username']))
                    conn.commit()

            return redirect("/new")

        return render_template('upload.html')
    else:
        return redirect("/")

@app.route('/templates/<filename>')
def uploaded_templates(filename):
    return send_from_directory(app.config['MEME_TEMPLATES'],
                               filename)

@app.route('/meme/<filename>')
def uploaded_memes(filename):
    return send_from_directory(app.config['USER_FOLDER'], filename)
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
