CREATE TABLE Images (
	imageID INT PRIMARY KEY, /* not sure if this should be an int id or a varchar contiang path to image... */ 
	img_size INT,		
	img_type VARCHAR(5),	/* options would be 'MACRO', 'IMAGE', 'GIF', or 'AVATR' */
	text_top VARCHAR(15),	/* top text should be limited to 15 chars */
	text_bot VARCHAR(15)	/* bot text should be limited to 15 chars */
);

CREATE TABLE ImageTags (
	imageID INT,
	tag VARCHAR(10)
);

CREATE TABLE Users (
	userID VARCHAR(25) PRIMARY KEY, /* usernames max 25 chars */
	first_name VARCHAR(25),
	last_name VARCHAR(25),
	dob DATE, 
	email VARCHAR(20)	/* email should also be unique */
);

CREATE TABLE Profiles (
	userID VARCHAR(25),
	avatarID VARCHAR(255)
);

CREATE TABLE Follows (
	userID VARCHAR(25),
	followed_userID VARCHAR(25)
);

CREATE TABLE SavedImages (
	userID VARCHAR(25),
	saved_imageID INT
);

CREATE TABLE Posts (
	postID INT PRIMARY KEY,
	userID VARCHAR(25),
	post_imageID INT, 
	post_ts DATETIME
);

CREATE TABLE Replies (
	postID INT,
	posterID VARCHAR(25),
	reply_imageID INT, 
	reply_ts DATETIME
);
