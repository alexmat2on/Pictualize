CREATE TABLE Images (
	imageID INT PRIMARY KEY, /* not sure if this should be an int id or a varchar contiang path to image... */
	img_size INT,
	img_type VARCHAR(5),	/* options would be 'MACRO', 'IMAGE', 'GIF', or 'AVATR' */
	text_top VARCHAR(15),	/* top text should be limited to 15 chars */
	text_bot VARCHAR(15)	/* bot text should be limited to 15 chars */
);

CREATE TABLE ImageTags (
	imageID INT,
	tag VARCHAR(10),
 	FOREIGN KEY (imageID) REFERENCES Images(imageId)
);

CREATE TABLE Users (
	userID VARCHAR(25) PRIMARY KEY, /* usernames max 25 chars */
	first_name VARCHAR(25),
	last_name VARCHAR(25),
	email VARCHAR(20)	/* email should also be unique */
);

CREATE TABLE Profiles (
	userID VARCHAR(25), 
	avatarID VARCHAR(255),
	FOREIGN KEY (userID) REFERENCES Users(userID)
);

CREATE TABLE Follows (
	userID VARCHAR(25),
	followed_userID VARCHAR(25),
	FOREIGN KEY (userID) REFERENCES Users(userID),
	FOREIGN KEY (followed_userID) REFERENCES Users(userID)
);

CREATE TABLE SavedImages (
	userID VARCHAR(25), 
	FOREIGN KEY (userID )REFERENCES Users(userID),
	saved_imageID INT, 
	FOREIGN KEY (saved_imageID) REFERENCES Images(imageID)
);


CREATE TABLE Posts (
	postID INT PRIMARY KEY,
	userID VARCHAR(25), 
	FOREIGN KEY (userID) REFERENCES Users(userID),
	post_imageID INT,
	FOREIGN KEY (post_imageID)REFERENCES Images(imageID),
	post_ts DATETIME not null
);

CREATE TABLE Replies (
	postID INT, 
	FOREIGN KEY (postID) REFERENCES Posts(postID),
	posterID VARCHAR(25), 
	FOREIGN KEY (posterID) REFERENCES Users(userID),
	reply_imageID INT, 
	FOREIGN KEY (reply_imageID) REFERENCES Images(imageID),
	reply_ts DATETIME
);
