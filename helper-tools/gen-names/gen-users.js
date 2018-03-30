var faker = require('faker');
var mysql = require('mysql');

var connection = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	password: 'root',
	database: 'Pictualize'
});

connection.connect();

for (var x = 0; x < 50; x++) {
	var un = faker.internet.userName();
	var fn = faker.name.firstName();
	var ln = faker.name.lastName();
	var em = faker.internet.email();
	var av = faker.image.avatar();

	// Insert user data into Users table
	var insertUserSQL = 'INSERT INTO Users VALUES(';
	insertUserSQL += "'" + un + "',";
	insertUserSQL += "'" + fn + "',";
	insertUserSQL += "'" + ln + "',";
	insertUserSQL += "'" + "'";
	insertUserSQL += ")";

	connection.query(insertUserSQL, function (err, result) {
		if (err) throw err;
		console.log("inserted", insertUserSQL);
	});

	// Give the user an Avatar
	var insertAvatarSQL = 'INSERT INTO Profiles VALUES(';
	// insertAvatarSQL += "'" + un + "',";
	// insertAvatarSQL += "'" + av + "'";
	// insertAvatarSQL += ")";

	// console.log(insertAvatarSQL);
	// connection.query(insertAvatarSQL, function (err, result) {
	// 	if (err) throw err;
	// 	console.log("inserted", insertAvatarSQL);
	// });
}

connection.end();
