# Pictualize
Team Members:
* Alexander Matson
* Jeter Gutierrez
* Kelly Lu

CS 336 DB Project, made in [Flask](https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972).

## Summary
Dear Professor Connor,

The `sql` folder in this repo contains all the SQL code. It contains the definition of our schemas, stored procedures, and triggers for a complete project as per the specs.

When users create new memes, they must select a meme template from their saved library. Of course, when the account is newly created, they _have_ no saved meme templates. Thus, we created a trigger called `TR_addDefaultTemplates` which executes **AFTER INSERT** on the `Users` table. Here's how it works:

There is a special user called `god`. Through this account, we upload all templates that we wish to be default templates. A SQL View called `DefaultTemplates` uses a natural join to display all Template Image IDs belonging to `god`.

The trigger will execute after a new user is inserted, and it iterates through the `DefaultTemplates` view and saves the same image IDs to `NEW.userID`. Thus, the new user now has all the same templates that `god` has.

There is another special feature related to the `god` account. If you login with the username `god`, you'll expose the **godview** feature. **Godview** is a web tool that displays all the data from any table in the database in an HTML table, for your convenience. You can see all the data in the database, and also verify that using the app will properly change the database (creating a new meme creates a new record in the `Posts` table, for instance).

## To-Do
- [x] ~~Add asset branding~~
- [x] ~~Refactor CSS with Flexbox layouts~~
- [x] ~~GODVIEW: Create a godview page as a helpful development tool. Godview will be an interactive HTML front-end to the database so we can see all the values from all the tables and it can help us visualize the database.~~
- [x] ~~HOMEPAGE: needs to display the most recent posts that every user has posted. Right now it just iterates through and displays the base templates.~~
- [ ] HOMEPAGE: save post item needs to be a button that will store the postID in the database for the logged in user.
- [ ] HOMEPAGE: "fork post" will do two things; it will save the template to the user's library, and open the post editor to rewrite the top/bottom text. Make a Flask route with a variable like `/fork/<postID>/`.
- [ ] PROFILE PAGE: create an HTML file for the profile page. Has avatar picture, with a sidebar. Sidebar has: "Following You", "Saved Posts", "Template Library". Each opens the respective item in content area.
- [ ] FOLLOWING PAGE: display a feed of just the posts created by the people you are following. Sidebar has list of usernames of people you're following.
- [x] ~~NEW POST: Clicking `create` should make a new post by storing it in the database, and bring you to homepage. Use a S.P. to insert the post data. It should also use Python to generate an image with the text embedded and store it under `img_user_gen` in the static folder.~~
- [x] ~~REGISTRATION: Add a trigger to save default templates in a new user's library.~~

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
