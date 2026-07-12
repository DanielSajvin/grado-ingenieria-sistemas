const mysql = require("mysql2");

const pool = mysql.createPool({
  host: "localhost",
  user: "root",
  password: "root",
  database: "restaurante_db",
  waitForConnections: true, // espera por una conexion si todas estan en uso
  connectionLimit: 10, // numero maximo de conexiones simultaneas
  quequeLimit: 10, // numero de consultas en espera (0 significa sin limite)
});

module.exports = pool;
