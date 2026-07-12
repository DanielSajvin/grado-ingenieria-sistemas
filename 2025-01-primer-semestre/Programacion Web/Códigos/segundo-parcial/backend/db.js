const mysql = require("mysql2");

const conexion = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "root",
  database: "test",
});

conexion.connect((error) => {
  if (error) {
    console.error("Error de conexión a la base de datos:", error);
    return;
  }
  console.log("Conexión a la base de datos establecida.");
});

module.exports = conexion;
// Exportar la conexión para usarla en otros archivos