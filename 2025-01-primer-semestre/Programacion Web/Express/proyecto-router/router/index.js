const express = require("express");
const path = require("path");

const app = express();

app.use(express.json);

const userRoutes = require('./user.js')

app.all("/about", (requ, res) => {
  res.send("about page");
});

app.get("/dashboard", (requ, res) => {
  res.send("dashboard page");
});

app.listen(3000, () => {
  console.log(`Servidor ${app.get("appName")} corriendo en el puerto 3000`);
});
