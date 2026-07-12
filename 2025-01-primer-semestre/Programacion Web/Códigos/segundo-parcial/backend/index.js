const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const jwt = require("jsonwebtoken");
require("dotenv").config();
const verificarToken = require("./middleware/verificarToken");
const swaggerJsDoc = require("swagger-jsdoc");
const swaggerUi = require("swagger-ui-express");

const app = express();

app.use(cors());
app.use(bodyParser.json());

const cursos = [
  { id: 1, titulo: "Curso de Node.js" },
  { id: 2, titulo: "Curso de React" },
];

/**
 * @swagger
 * /login:
 *   post:
 *     summary: Inicia sesión y obtiene un token JWT.
 *     tags:
 *       - Autenticación
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               usuario:
 *                 type: string
 *                 example: admin
 *               password:
 *                 type: string
 *                 example: 123
 *     responses:
 *       200:
 *         description: Inicio de sesión exitoso.
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 token:
 *                   type: string
 *       401:
 *         description: Credenciales inválidas.
 */
// Endpoint de login
app.post("/login", (req, res) => {
  const { usuario, password } = req.body;

  if (usuario === "admin" && password === "123") {
    const token = jwt.sign({ usuario }, process.env.JWT_SECRET, {
      expiresIn: "1min",
    });
    res.json({ token });
  } else {
    res.status(401).json({ mensaje: "Credenciales inválidas" });
  }
});

/**
 * @swagger
 * /cursos:
 *   get:
 *     summary: Obtiene la lista de cursos (requiere autenticación).
 *     tags:
 *       - Cursos
 *     security:
 *       - bearerAuth: []
 *     responses:
 *       200:
 *         description: Lista de cursos.
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 type: object
 *                 properties:
 *                   id:
 *                     type: integer
 *                   titulo:
 *                     type: string
 *       401:
 *         description: Token no válido o no proporcionado.
 */
// Endpoint protegido
app.get("/cursos", verificarToken, (req, res) => {
  res.json(cursos);
});

const swaggerOptions = {
  swaggerDefinition: {
    openapi: "3.0.0",
    info: {
      title: "API de Cursos",
      version: "1.0.0",
      description: "API para gestionar cursos y autenticación",
    },
    servers: [
      {
        url: "http://localhost:3000",
      },
    ],
    components: {
      securitySchemes: {
        bearerAuth: {
          type: "http",
          scheme: "bearer",
          bearerFormat: "JWT",
        },
      },
    },
  },
  apis: [__filename],
};

const swaggerDocs = swaggerJsDoc(swaggerOptions);
app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerDocs));

app.listen(3000, () => {
  console.log("Servidor backend corriendo en http://localhost:3000");
});
