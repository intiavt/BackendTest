const { json } = require("express");
const express = require("express");
const app = express();
const morgan = require("morgan");

// -----SETTINGS-----
app.set("port", process.env.PORT || 3000);
app.set("json spaces", 2);

// -----MIDDLEWARES-----
app.use(morgan("dev"));
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

//-----ROUTES-----
app.use("/api/v1", require("./routes/fifa"));

// -----STARTING THE SERVER-----
app.listen(3000, () => {
  console.log(`Server on port ${app.get("port")}`);
});
