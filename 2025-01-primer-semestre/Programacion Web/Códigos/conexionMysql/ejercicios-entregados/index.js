const express = require("express");
const pool = require("../db");

const app = express();
const port = 3000;

app.use(express.json());

const swaggerJsDoc = require("swagger-jsdoc");
const swaggerUi = require("swagger-ui-express");

const swaggerOptions = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "API Documentation",
      version: "1.0.0",
      description: "API documentation for the project",
    },
    servers: [
      {
        url: "http://localhost:3000",
      },
    ],
  },
  apis: ["./routes/*.js", "./index.js"], // Include index.js for Swagger documentation
};

const swaggerDocs = swaggerJsDoc(swaggerOptions);
app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerDocs));
/**
 * @swagger
 * components:
 *   schemas:
 *     Cliente:
 *       type: object
 *       required:
 *         - nombre
 *         - telefono
 *         - email
 *       properties:
 *         id:
 *           type: integer
 *           description: ID del cliente
 *         nombre:
 *           type: string
 *           description: Nombre del cliente
 *         telefono:
 *           type: string
 *           description: Teléfono del cliente
 *         email:
 *           type: string
 *           description: Email del cliente
 *       example:
 *         id: 1
 *         nombre: Juan Pérez
 *         telefono: "123456789"
 *         email: juan.perez@example.com
 *
 *     Mesa:
 *       type: object
 *       required:
 *         - numero
 *         - capacidad
 *       properties:
 *         id:
 *           type: integer
 *           description: ID de la mesa
 *         numero:
 *           type: integer
 *           description: Número de la mesa
 *         capacidad:
 *           type: integer
 *           description: Capacidad de la mesa
 *       example:
 *         id: 1
 *         numero: 5
 *         capacidad: 4
 *
 *     Reserva:
 *       type: object
 *       required:
 *         - cliente_id
 *         - mesa_id
 *         - fecha
 *         - hora
 *       properties:
 *         id:
 *           type: integer
 *           description: ID de la reserva
 *         cliente_id:
 *           type: integer
 *           description: ID del cliente
 *         mesa_id:
 *           type: integer
 *           description: ID de la mesa
 *         fecha:
 *           type: string
 *           format: date
 *           description: Fecha de la reserva
 *         hora:
 *           type: string
 *           format: time
 *           description: Hora de la reserva
 *         estado:
 *           type: string
 *           description: Estado de la reserva
 *       example:
 *         id: 1
 *         cliente_id: 1
 *         mesa_id: 1
 *         fecha: "2023-10-01"
 *         hora: "19:00"
 *         estado: "confirmada"
 */

/**
 * @swagger
 * /reservas:
 *   post:
 *     summary: Crear una nueva reserva
 *     tags: [Reservas]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             $ref: '#/components/schemas/Reserva'
 *     responses:
 *       201:
 *         description: Reserva creada con éxito
 *       400:
 *         description: La mesa ya está reservada en esa fecha y hora
 *       500:
 *         description: Error en la consulta
 */



/**
 * @swagger
 * /reservas/{id}:
 *   put:
 *     summary: Actualizar el estado de una reserva
 *     tags: [Reservas]
 *     parameters:
 *       - in: path
 *         name: id
 *         schema:
 *           type: integer
 *         required: true
 *         description: ID de la reserva
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               estado:
 *                 type: string
 *                 description: Nuevo estado de la reserva
 *     responses:
 *       200:
 *         description: Estado de la reserva actualizado
 *       404:
 *         description: Reserva no encontrada
 *       500:
 *         description: Error en la consulta
 */

/**
 * @swagger
 * /reservas/{id}:
 *   delete:
 *     summary: Cancelar una reserva
 *     tags: [Reservas]
 *     parameters:
 *       - in: path
 *         name: id
 *         schema:
 *           type: integer
 *         required: true
 *         description: ID de la reserva
 *     responses:
 *       200:
 *         description: Reserva cancelada con éxito
 *       404:
 *         description: Reserva no encontrada
 *       500:
 *         description: Error en la consulta
 */

/**
 * @swagger
 * /reservas/disponibilidad:
 *   get:
 *     summary: Consultar disponibilidad de mesas en una fecha y hora específica
 *     tags: [Reservas]
 *     parameters:
 *       - in: query
 *         name: fecha
 *         schema:
 *           type: string
 *           format: date
 *         required: true
 *         description: Fecha para consultar disponibilidad
 *       - in: query
 *         name: hora
 *         schema:
 *           type: string
 *           format: time
 *         required: true
 *         description: Hora para consultar disponibilidad
 *     responses:
 *       200:
 *         description: Lista de mesas disponibles
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 disponibles:
 *                   type: array
 *                   items:
 *                     $ref: '#/components/schemas/Mesa'
 *       500:
 *         description: Error en la consulta
 */

// endpoint para registrar un nuevo cliente
/**
 * @swagger
 * /clientes:
 *   post:
 *     summary: Registrar un nuevo cliente
 *     tags: [Clientes]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             $ref: '#/components/schemas/Cliente'
 *     responses:
 *       201:
 *         description: Cliente agregado con éxito
 *       500:
 *         description: Error en la consulta
 */
app.post("/clientes", (req, res) => {
  const { nombre, telefono, email } = req.body;

  // consulta prametrizada para insertar un nuevo usuarios
  const sqlQuery =
    "INSERT INTO clientes (nombre, telefono, email) VALUES (?,?,?)";

  // usar el pool de conexiones para ejecutar la consulta
  pool.query(sqlQuery, [nombre, telefono, email], (err, results) => {
    if (err) {
      console.log("Error al ejecutar la consulta: ", err);
      return res.status(500).send("Error de  consulta");
    }
    res.status(201).json({
      message: "Cliente agregado con exito",
      usuarioId: results.insertId,
    });
  });
});

// endpoint para registrar una nueva mesa
/**
 * @swagger
 * /mesas:
 *   post:
 *     summary: Registrar una nueva mesa
 *     tags: [Mesas]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             $ref: '#/components/schemas/Mesa'
 *     responses:
 *       201:
 *         description: Mesa agregada con éxito
 *       500:
 *         description: Error en la consulta
 */
app.post("/mesas", (req, res) => {
  const { numero, capacidad } = req.body;

  // consulta prametrizada para insertar un nuevo usuarios
  const sqlQuery = "INSERT INTO mesas (numero, capacidad) VALUES (?,?)";

  // usar el pool de conexiones para ejecutar la consulta
  pool.query(sqlQuery, [numero, capacidad], (err, results) => {
    if (err) {
      console.log("Error al ejecutar la consulta: ", err);
      return res.status(500).send("Error de  consulta");
    }
    res.status(201).json({
      message: "Mesa agregada con exito",
      usuarioId: results.insertId,
    });
  });
});

//enpoint para crear una reserva
/**
 * @swagger
 * /reservas:
 *   get:
 *     summary: Obtener todas las reservas con datos del cliente y la mesa
 *     tags: [Reservas]
 *     responses:
 *       200:
 *         description: Lista de reservas
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 $ref: '#/components/schemas/Reserva'
 *       500:
 *         description: Error en la consulta
 */
app.post("/reservas", (req, res) => {
  const { cliente_id, mesa_id, fecha, hora } = req.body;

  // Verificar si la mesa está disponible
  const checkQuery =
    "SELECT * FROM reservas WHERE mesa_id = ? AND fecha = ? AND hora = ?";
  pool.query(checkQuery, [mesa_id, fecha, hora], (err, results) => {
    if (err) {
      console.error("Error al verificar disponibilidad: ", err);
      return res.status(500).send("Error en la consulta");
    }
    if (results.length > 0) {
      return res
        .status(400)
        .json({ message: "La mesa ya está reservada en esa fecha y hora" });
    }

    // Insertar la nueva reserva
    const insertQuery =
      "INSERT INTO reservas (cliente_id, mesa_id, fecha, hora) VALUES (?, ?, ?, ?)";
    pool.query(
      insertQuery,
      [cliente_id, mesa_id, fecha, hora],
      (err, results) => {
        if (err) {
          console.error("Error al crear la reserva: ", err);
          return res.status(500).send("Error en la consulta");
        }
        res.status(201).json({
          message: "Reserva creada con éxito",
          reservaId: results.insertId,
        });
      }
    );
  });
});

// endopoint para obtener todas las reservas con datos del cliente y la mesa
app.get("/reservas", (req, res) => {
  const sqlQuery = `
    SELECT reservas.id, clientes.nombre AS cliente, clientes.telefono, clientes.email,
           mesas.numero AS mesa, mesas.capacidad, reservas.fecha, reservas.hora, reservas.estado
    FROM reservas
    JOIN clientes ON reservas.cliente_id = clientes.id
    JOIN mesas ON reservas.mesa_id = mesas.id`;

  pool.query(sqlQuery, (err, results) => {
    if (err) {
      console.error("Error al obtener las reservas: ", err);
      return res.status(500).send("Error en la consulta");
    }
    res.json(results);
  });
});

// endpoint para actualizar el estado de una reserva
app.put("/reservas/:id", (req, res) => {
  const { id } = req.params;
  const { estado } = req.body;

  const updateQuery = "UPDATE reservas SET estado = ? WHERE id = ?";
  pool.query(updateQuery, [estado, id], (err, results) => {
    if (err) {
      console.error("Error al actualizar la reserva: ", err);
      return res.status(500).send("Error en la consulta");
    }
    if (results.affectedRows === 0) {
      return res.status(404).json({ message: "Reserva no encontrada" });
    }
    res.json({ message: "Estado de la reserva actualizado" });
  });
});

// endpoint para cancelar una reserva
app.delete("/reservas/:id", (req, res) => {
  const { id } = req.params;

  const deleteQuery = "DELETE FROM reservas WHERE id = ?";
  pool.query(deleteQuery, [id], (err, results) => {
    if (err) {
      console.error("Error al cancelar la reserva: ", err);
      return res.status(500).send("Error en la consulta");
    }
    if (results.affectedRows === 0) {
      return res.status(404).json({ message: "Reserva no encontrada" });
    }
    res.json({ message: "Reserva cancelada con éxito" });
  });
});

// enpoint para consultar disponibilidad de mesas en una fecha y hora específica
app.get("/reservas/disponibilidad", (req, res) => {
  const { fecha, hora } = req.query;

  const disponibilidadQuery = `
    SELECT * FROM mesas WHERE id NOT IN (
      SELECT mesa_id FROM reservas WHERE fecha = ? AND hora = ?
    )`;

  pool.query(disponibilidadQuery, [fecha, hora], (err, results) => {
    if (err) {
      console.error("Error al consultar disponibilidad: ", err);
      return res.status(500).send("Error en la consulta");
    }
    res.json({ disponibles: results });
  });
});

app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});
