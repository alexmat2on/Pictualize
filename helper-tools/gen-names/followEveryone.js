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
    for (var i = 0; i < numRecords; i++) {
      var followers = [];
      for (var j = i+1; j < numRecords; j++ ) {
        console.log(j, "oop");
        followers.push(result[i].userID);
        followers.push(result[j].userID);
      }
      values.push(followers);
      console.log("---------------")
    }

    var sql = "INSERT INTO Follows VALUES ?";
    console.log(result.length);
  })

connection.end();
