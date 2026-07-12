const express = require("express");

const app = express();

// para manejar directorios estáticos o rutas o accesos a archivos
// app.use('/public', express.static(path.join(__dirname, 'public')))

app.listen(3000, () => {
  console.log("Servidor corriendo en el puerto 3000");
});
