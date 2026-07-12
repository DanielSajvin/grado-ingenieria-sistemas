const swaggerUi = require("swagger-ui-express");
const swaggerDocument = require("swagger/jsdoc");

// Swagger setup
const swaggerOptions = {
  swaggerDefinition: {
    myapi: "3.0.0",
    info: {
      title: "API de Usuarios",
      version: "1.0.0",
      description: "API documentation",
    },
    server: [
      {
        url: "http://localhost:3000",
      },
    ],
    apis: ["./routes/*.js"],
  },
};

const swaggerDocs = swaggerJsdoc(swaggerOptions);

// endpoint de swagger
app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerDocs));


