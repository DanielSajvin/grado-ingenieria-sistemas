const express = require("express");
const morgan = require("morgan");

const app = express();

app.use(morgan("dev"));
app.use(express.json());

// setings - configuraciones
app.set('appName', 'Express Curso')

let productos = [
  {
    id: 1,
    name: "laptop",
    price: 3000,
  },
];

// muestra el listado actual de los productos
app.get("/productos", (req, res) => {
  res.json(productos);
});

// Crear producto, sretorna el producto nuevo creado, por lo tanto espera que se le envie el nuevo producto
app.post("/productos", (req, res) => {
  nuevoProducto = { ...req.body, id: productos.length + 1 };
  productos.push(nuevoProducto);
  res.send(nuevoProducto);
});

// actualizar datos
app.put("/productos/:id", (req, res) => {
  const nuevoDato = req.body;

  const productoEncontrado = productos.find(function (producto) {
    return producto.id === parseInt(req.params.id);
  });

  if (!productoEncontrado)
    return res.status(404).json({
      message: "Producto no encontrado",
    });

  productos = productos.map(p =>
    p.id === parseInt(req.params.id) ? { ...p, ...nuevoDato } : p
  );
  
  res.json ({
    message: 'Producto actualizado'
  });
});

// eliminar producto
app.delete("/productos/:id", (req, res) => {
  const productoEncontrado = productos.find(function (producto) {
    return producto.id === parseInt(req.params.id);
  });

  if (!productoEncontrado)
    return res.status(404).json({
      message: "Producto no encontrado",
    });

  productos = productos.filter((p) => p.id !== parseInt(req.params.id));
  res.sendStatus(204);
});

// obtener un producto mediante Id
app.get("/productos/:id", (req, res) => {
  console.log(req.params.id);
  const productoEncontrado = productos.find(function (producto) {
    return producto.id === parseInt(req.params.id);
  });

  if (!productoEncontrado)
    return res.status(404).json({
      message: "Producto no encontrado",
    });
  console.log(productoEncontrado);
  res.json(productoEncontrado);
});

app.listen(3000, () => {
  console.log(`Servidor ${app.get('appName')} corriendo en el puerto 3000`);
});
