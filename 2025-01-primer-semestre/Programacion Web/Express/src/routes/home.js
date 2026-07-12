const express = require("express");
const axios = require("axios");

const router = express.Router();

router.get("/", (req, res) => {
  let isActive = true;

  const users = [
    {
      id: 1,
      name: "Daniel",
      lastName: "Sajvin",
    },
    {
      id: 2,
      name: "Jairo",
      lastName: "Sajvin",
    },
    {
      id: 3,
      name: "Pablo",
      lastName: "Perez",
    },
  ];
  const title = "Index Page";
  res.render("index", {
    title: title,
    isActive: isActive,
    users,
  });
});

router.get("/about", (req, res) => {
  const title = "Mi pagina creada desde Express 2";
  res.render("about");
});

router.get("/dashboard", (req, res) => {
  res.render("dashboard");
});

router.get("/posts", async (req, res) => {
  const response = await axios.get(
    "https://jsonplaceholder.typicode.com/posts "
  );
  //console.log(response);
  res.render("posts", {
    posts: response.data,
  });
});

module.exports = router;
