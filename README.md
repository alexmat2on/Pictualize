# Pictualize
Team Members:
* Alexander Matson
* Jeter Gutierrez
* Kelly Lu

CS 336 DB Project, made in [Flask](https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972).

## To-Do
- [x] Began simple web app with Flask (in `FlaskApp/`) that establishes a DB connection
- [x] Write SQL statements to generate all 8 schemas (in `sql/`)
- [x] Write a helper script in Python to auto-generate memes for future testing (in `helper-tools/`)
- [ ] Create appropriate table constraints for tables
- [ ] Connect sign-up form to MySQL backend
- [ ] Write helper script to auto-generate fake users with fake posts
- [ ] Create homescreen UI displaying other user's posts
- [ ] Allow user to save other user's templates/images to personal library
- [ ] Allow user to create new posts from image template and post

## Run
* Install flask with `pip install flask`
* Install flask-mysql with `pip install flask-mysql`
* Go into the FlaskApp directory and execute `python app.py`.

The app connects to a local MySQL instance, which must contain a database called `Pictualize`,
and will run by default on `localhost:5000`
