Create Database Pictualize;
use Pictualize;

CREATE TABLE ImageTypes (
	img_type VARCHAR(5) PRIMARY KEY
);

INSERT INTO ImageTypes VALUES ('MACRO'), ('TEMPL'), ('GIF'), ('AVATR');

CREATE TABLE Images (
	imageID VARCHAR(40) PRIMARY KEY, /* not sure if this should be an int id or a varchar contiang path to image... */
	img_type VARCHAR(5),	/* options would be 'MACRO', 'TEMPL', 'GIF', or 'AVATR' */
	FOREIGN KEY (img_type) REFERENCES ImageTypes(img_type)
);

CREATE TABLE ImageTags (
	imageID VARCHAR(40),
	tag VARCHAR(10),
 	FOREIGN KEY (imageID) REFERENCES Images(imageID)
);

CREATE TABLE Users (
	userID VARCHAR(25) PRIMARY KEY, /* usernames max 25 chars */
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	email VARCHAR(255)	/* email should also be unique */
);

CREATE TABLE Profiles (
	userID VARCHAR(25),
	avatarID VARCHAR(40),
	FOREIGN KEY (userID) REFERENCES Users(userID),
	FOREIGN KEY (avatarID) REFERENCES Images(imageID)
);

CREATE TABLE Follows (
	userID VARCHAR(25),
	followed_userID VARCHAR(25),
	FOREIGN KEY (userID) REFERENCES Users(userID),
	FOREIGN KEY (followed_userID) REFERENCES Users(userID)
);

CREATE TABLE SavedImages (
	userID VARCHAR(25),
	saved_imageID VARCHAR(40),
	FOREIGN KEY (userID )REFERENCES Users(userID),
	FOREIGN KEY (saved_imageID) REFERENCES Images(imageID)
);


CREATE TABLE Posts (
	postID INT PRIMARY KEY AUTO_INCREMENT,
	userID VARCHAR(25),
	post_image VARCHAR(40),
	template_image VARCHAR(40),
	post_ts DATETIME NOT NULL,
	text_top VARCHAR(20),	/* top text should be limited to 20 chars */
	text_bot VARCHAR(20),	/* bot text should be limited to 20 chars */
	FOREIGN KEY (userID) REFERENCES Users(userID),
	FOREIGN KEY (post_image) REFERENCES Images(imageID),
	FOREIGN KEY (template_image) REFERENCES Images(imageID)
);

CREATE TABLE Replies (
	replyID INT PRIMARY KEY AUTO_INCREMENT,
	parent_post INT,
	reply_post INT,
	FOREIGN KEY (parent_post) REFERENCES Posts(postID),
	FOREIGN KEY (reply_post) REFERENCES Posts(postID)
);
