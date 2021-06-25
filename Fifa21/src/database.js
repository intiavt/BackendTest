const mysql = require("mysql");

// creates the connection to mysql
const mysqlConnection = mysql.createConnection({
  connectionLimit: 500,
  host: "localhost",
  user: "root",
  password: "", //el password de ingreso a mysql
  database: "backendtest",
  port: 3306,
});

// connects to mysql
mysqlConnection.connect(function (err) {
  if (err) {
    throw err; //
  } else {
    console.log("Connected");
  }
});

module.exports = mysqlConnection;
