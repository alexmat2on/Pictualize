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
- [x] Create appropriate table constraints for tables
- [x] Connect sign-up form to MySQL backend
- [x] Write helper script to auto-generate fake users with fake posts
- [ ] Create homescreen UI displaying other user's posts
- [ ] Allow user to save other user's templates/images to personal library
- [ ] Allow user to create new posts from image template and post

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
