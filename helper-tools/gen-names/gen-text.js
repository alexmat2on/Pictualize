var faker = require('faker');
var mysql = require('mysql');
var fs = require('fs');

var connection = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	password: 'root',
	database: 'Pictualize'
});

connection.connect();

for (var x = 0; x < 25; x++) {
	var top = faker.lorem.word();
	var image = faker.image.image();

	console.log(image);
  console.log(top);
	fs.open("topMeme.txt")
  fs.writeFile("topMeme.txt", top + "\n", function (err) {
    if (err) throw err;
  })
	// Insert user data into Users table
	// var insertUserSQL = 'INSERT INTO Users VALUES(';
	// insertUserSQL += "'" + un + "',";
	// insertUserSQL += "'" + fn + "',";
	// insertUserSQL += "'" + ln + "',";
	// insertUserSQL += "'" + em + "'";
	// insertUserSQL += ")";
  //
	// connection.query(insertUserSQL, function (err, result) {
	// 	if (err) throw err;
	// 	console.log("inserted", insertUserSQL);
	// });
  //
	// // Give the user an Avatar
	// var insertAvatarSQL = 'INSERT INTO Profiles VALUES(';
	// insertAvatarSQL += "'" + un + "',";
	// insertAvatarSQL += "'" + av + "'";
	// insertAvatarSQL += ")";
  //
	// console.log(insertAvatarSQL);
	// connection.query(insertAvatarSQL, function (err, result) {
	// 	if (err) throw err;
	// 	console.log("inserted", insertAvatarSQL);
	// });
}

connection.end();
