var faker = require('faker');
var mysql = require('mysql');

var connection = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	password: 'root',
	database: 'Pictualize'
});

connection.connect();

var un = faker.internet.userName();
var fn = faker.name.firstName();
var ln = faker.name.lastName();
var em = faker.internet.email();

console.log(fn);
console.log(ln);
console.log(un);
console.log(em);

var insertUserSQL = 'INSERT INTO Users VALUES(' +
											"'" + un + ',' + fn + ',' + ln + ','+ em + ')';
connection.query(insertUserSQL, function (err, result) {
	if (err) throw err;
	console.log("inserted", un, fn, ln, em);
})

connection.query('SELECT * FROM Users', function (error, results, fields) {
  if (error) throw error;
  console.log('The solution is: ', results, fields);
});

connection.end();
