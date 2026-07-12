const express = require("express");

const app = express.Router();

app.get("/userName", (req, res) => {
  res.send("Username route");
});

app.get("/profile", (req, res) => {
  res.send("profile route");
});

module.exports = app;
