const express = require("express");
const pool = require("../db");

const app = express();
const port = 3000;

app.use(express.json());

// ruta para buscar usuario por id y nombre
app.get("/usuarios", (req, res) => {
  const { id, nombre } = req.query;

  const sqlQuery = "SELECT * FROM usuarios WHERE id = ? AND nombre = ?";

  // usar el pool de conexiones para ejecutar la consulta
  pool.query(sqlQuery, [id, nombre], (err, results) => {
    if (err) {  
      console.log("Error al ejecutar la consulta: ", err);
      return res.status(500).send("Error de consulta");
    }
    res.json(results); // enviar los resulados como respuesta JSON
  });
});


// ruta para agregar un nuevo usuario
app.post("/usuarios", (req, res) => {
  const { nombre, email, edad } = req.body;

  // consulta parametrizada para insertar un nuevo usuario
  const sqlQuery =
    "INSERT INTO usuarios (nombre, email, edad) VALUES (?, ?, ?)";

  // usar el pool de conexiones para ejecutar la consulta
  pool.query(sqlQuery, [nombre, email, edad], (err, results) => {
    if (err) {
      console.log("Error al ejecutar la consulta: ", err);
      return res.status(500).send("Error de consulta");
    }
    res.status(201).json({
      message: "Usuario agregado con exito",
      usuarioId: results.insertId,
    });
  });
});

// ruta para actualizar el email del usuario
app.put("/usuarios/:id", (req, res) => {
  const { id } = req.params;
  const { email } = req.body;

  if (!email) {
    return res.status(400).json({ error: "El campo 'email' es obligatorio" });
  }

  const sqlQuery = "UPDATE usuarios SET email = ? WHERE id = ?";

  pool.query(sqlQuery, [email, id], (err, results) => {
    if (err) {
      console.log("Error al ejecutar la consulta: ", err);
      return res.status(500).send("Error de consulta");
    }

    if (results.affectedRows === 0) {
      return res.status(404).json({ error: "Usuario no encontrado" });
    }

    res.json({ message: "Email actualizado con éxito" });
  });
});

//ruta para eliminar usuario
app.delete("/usuarios/:id", (req, res) => {
  const { id } = req.params;

  const sqlQuery = "DELETE FROM usuarios WHERE id = ?";

  pool.query(sqlQuery, [id], (err, results) => {
    if (err) {
      console.log("Error al ejecutar la consulta: ", err);
      return res.status(500).send("Error de consulta");
    }

    if (results.affectedRows === 0) {
      return res.status(404).json({ error: "Usuario no encontrado" });
    }

    res.json({ message: "Usuario eliminado con éxito" });
  });
});

app.listen(port, () => {
    console.log(`Servidor corriendo en http://localhost:${port}`);
  });
