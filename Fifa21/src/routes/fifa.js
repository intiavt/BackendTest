const { Router } = require("express");
const router = Router();
const mysqlConnection = require("../database");

//  Obtain the players of a team
router.post("/teams", (req, res) => {
  const { Name } = req.body;
  console.log(req.body);
  mysqlConnection.query(
    "SELECT * FROM players WHERE club = ?",
    [Name],
    (err, rows, fields) => {
      if (!err) {
        res.json(rows);
      } else {
        console.log("err");
      }
    }
  );
});

// Search for players that contain the string in the player name field and sorts them by alphabetical order
router.get("/players", (req, res) => {
  const searchParameter = req.query;
  console.log(searchParameter.search);
  var order = "";

  if (typeof searchParameter.order == "undefined") {
    order = "ASC";
  } else {
    order = searchParameter.order.toUpperCase();
  }
  mysqlConnection.query(
    `SELECT * FROM players WHERE name LIKE ? ORDER BY name ${order}`,
    [`%${searchParameter.search}%`],
    (err, rows, fields) => {
      if (!err) {
        res.json(rows);
      } else {
        console.log("err");
      }
    }
  );
});

module.exports = router;
