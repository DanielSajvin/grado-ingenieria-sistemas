const express = require("express");
const morgan = require("morgan");
const path = require("path");
require("ejs");

// req, request
// res, response

// VERBOS HTTP
// GET el cliente está queriendo obtener algo del servidor
// POST va a enviar datos, el cliente está tratando de crear o guardar algo en el servidor, es decir, que también le puede enviar información
// PUT el cliente está tratando de actualizar algo en el servidor, pero va a actualizar todo
// DELETE el cliente está tratando de eliminar algo
// PATCH el cliente quiere actualizar algo, pero únicamente una parte de los datos

// crear el servidor - ejecutar express
const app = express();

// archivos que voy a requerir
const homeRoutes = require("./src/routes/home");
const userRoutes = require("./src/routes/user");

// REST API CRUD -> REST(Representational State Transfer)
// Cliente -> Rest API (el servidor) -> base de datos

// settings
app.set("case sensitive routing", true);
app.set("appName", "Express Course");
app.set("view engine", "ejs");
//app.set("views", path.join(__dirname, views));
app.set("views", "./src/views");

// middleware
app.use(express.json());
app.use(morgan("dev"));

app.use(homeRoutes);
app.use(userRoutes);

app.listen(3000, () => {
  console.log("Servidor corriendo en el puerto 3000");
});

/* // Middleware interceptor
app.get("/profile", (req, res) => {
  res.send("profile page");
});

app.all("/about", (req, res) => {
  res.send("abaout page");
});

app.get("/dashboard", (req, res) => {
  res.send("Dashboard page");
}); */

/* // Introducción a Middlewares II

app.use((req, res, next) => {
  console.log(`Ruta: ${req.url} Método: ${req.method}`);
  next();
});

app.get('/profile', (req, res) => {
  res.send('profile page');
})

app.use(function (req, res, next) {
  if (req.query.login === "daniel") {
    next();
  } else {
    res.send("No autorizado");
  }
});

app.get("/dashboard", (req, res) => {
  res.send("Dashboard page");
});
 */

/* // Introducción a Middlewares

// Middleware, porque se encuentra en medio del navegador y de la ruta
// función que se ejecuta antes de llegar a la ruta (logger)
app.use(function (req, res, next) {
  console.log(`Ruta ${req.url} Método: Método ${req.method}`);
  next();
});

// ruta
app.get("/profile", (req, res) => {
  res.send("profile page");
});

app.all("/prof", (req, res) => {
  res.send("prof page");
});
*/

/* // Routing - Enrutamiento 
app.get('/', (req, res) => {
    res.send('Hola mundo')
})

app.get('/about', (req, res) => {
    res.send('About')
})

app.get('/clima', (req, res) => {
    res.send('Clima actual es bueno')
})

// en caso de no encontrar alguna ruta llega a este punto
app.use((req, res) => {
    res.status(404).send('No se encontró tu página')
}) */

// HTTP Métodos en Express (verbos)
/* app.get('/productos', (req, res) => {
    res.send('Lista de productos');
})

app.post('/productos', (req, res) => {
    res.send('Creando productos');
})

app.put('/productos', (req, res) => {
    res.send('Actualizando producto');
})

app.delete('/productos', (req, res) => {
    res.send('Eliminando Producto');
})

app.patch('/productos', (req, res) => {
    res.send('Actualizando una parte del producto');
})
 */

// HTTP Response
/* app.get("/", (req, res) => {
    res.send("Hola mundo");
  });
  
  app.get("/miarchivo", (req, res) => {
    res.sendFile("./static/descarga.png", {
      root: __dirname,
    });
  });
  
  app.get("/user", (req, res) => {
    res.json({
      nombre: "Daniel",
      apellido: "Sajvin",
      edad: 23,
    });
  });
  
  app.get("/miarchivo", (req, res) => {
      res.sendFile("./static/descarga.png", {
        root: __dirname,
      });
  });
  
  app.get('/isAlive', (req, res) => {
      res.sendStatus(204);
}) */

/* // Request Body

// Partes de la Request: endpoint(URL), header(nota que especifica lo que estoy enviando), body(contenido de la petición)

app.use(express.text())

app.post("/user", (req, res) => {
  console.log(req.body);
  res.send("Nuevo usuario creado");
}); */

/* // Request Params

app.get("/hello/:username", (req, res) => {
  console.log(typeof req.params.username);
  res.send(`Hola ${req.params.username}`);
});

app.get("/suma/:x/:y", (req, res) => {
  const {x, y} = req.params;
  //const resultado = parseInt(req.params.x) + parseInt(req.params.y);
  res.send(`Resultado: ${parseInt(x) + parseInt(y)}`);
});

app.get('/usuario/:username/photo', (req, res) => {
  if (req.params.username === 'daniel') {
    return res.sendFile('./static/descarga.png', {
      root: __dirname
    })
  }

  // si no se coloca return la función sigue hasta la última línea, es decir
  // siempre va a llegar a la última línea ya que el return no le ha indicado que debe retornar y finalizar 
  res.send('el usuario no es válido')

}) */

/* // Queries
app.get("/search", (req, res) => {
  console.log(req.query);
  if (req.query.q === "elemento") {
    res.send("hay un elemento");
  } else {
    res.send("no hay elemento");
  }
}); */

/* // All Method, quiere decir que funciona con cualquier método http
app.get('/info', (req, res) => {
  res.send('server info')
})
 */
