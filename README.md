# Pictualize
Team Members:
* Alexander Matson
* Jeter Gutierrez
* Kelly Lu

CS 336 DB Project, made in [Flask](https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972).

## To-Do
- [x] Add asset branding
- [x] Refactor CSS with Flexbox layouts
- [ ] GODVIEW: Create a godview page as a helpful development tool. Godview will be an interactive HTML front-end to the database so we can see all the values from all the tables and it can help us visualize the database.
- [ ] NEW POST PAGE: needs a non-hardcoded carousel (right now it is hardcoded). We'll need to add "left" and "right" buttons to cycle through base templates. Base templates will need to be fetched from the templates that the user has saved. I think we'll need a new table in the database to keep track of a user's saved templates/base images.
- [ ] HOMEPAGE: needs to display the most recent posts that every user has posted. Right now it just iterates through and displays the base templates.
- [ ] HOMEPAGE: save post item needs to be a button that will store the postID in the database for the logged in user.
- [ ] HOMEPAGE: "make new post with template" will do two things; it will save the template to the user's library, and open the post editor to rewrite the top/bottom text.
- [ ] HOMEPAGE: rename the "make new post with blah blah..." option to "fork post" for brevity.
- [ ] PROFILE PAGE: create an HTML file for the profile page which will contain the current user's followers, followees, and library of templates. and other user info, idk.
- [ ] FOLLOWING PAGE: display a feed of just the posts created by the people you are following.  

## Run
* Install flask with `pip install flask`
* Install flask-mysql with `pip install flask-mysql`
* Go into the FlaskApp directory and execute `python app.py`.

## MySQL Tunnel Connection
* Run `ssh -L 9999:134.74.146.21:3306 -N USERNAME@134.74.126.104`, where USERNAME == the
 first four letters of your last name and the last four digits of your EMPLID all lowercase.

* This command creates an SSH tunnel that connects your local computer to the CCNY computer lab.

* Leave it running in a terminal, without exiting out.

* In another terminal, you can now connect to the school database by using the command
  `mysql -h 127.0.0.1 --port 9999 --user JCSP18XXYYYY -p` to get access to the MySQL command line.

* Replace `XXYYYY` with your appropriate information.  

The app connects to a local MySQL instance, which must contain a database called `Pictualize`,
and will run by default on `localhost:5000`
