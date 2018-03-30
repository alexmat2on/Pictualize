var faker = require('faker');
var mysql = require('mysql');

var connection = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	password: 'root',
	database: 'Pictualize'
});

connection.connect();

  connection.query("Select * FROM Users", function (err, result) {
    if (err) throw err;
    console.log("selected!", result);

    var numRecords = result.length;
    var values = [];
    for (var i = 0; i < numRecords - 1; i++) {
      var followers = [];
      followers.push(result[i].userID);
      followers.push(result[i+1].userID);
      console.log(followers);
      console.log('---');
      values.push(followers);
    }

    console.log(values);
    var sql = "INSERT INTO Follows(userID, followed_userID) VALUES ?";
    connection.query(sql, [values], function (err) {
      if (err) throw err;
    });
    console.log(result.length);
  })

connection.end();
