const jwt = require("jsonwebtoken");
require("dotenv").config();

function verificarToken(req, res, next) {
  const token = req.headers["authorization"];

  if (!token) {
    return res.status(401).json({ mensaje: "Token no proporcionado" });
  }

  jwt.verify(token.split(" ")[1], process.env.JWT_SECRET, (err, decoded) => {
    if (err) {
      return res.status(401).json({ mensaje: "Token inválido" });
    }
    req.usuario = decoded;
    next();
  });
}

module.exports = verificarToken;
