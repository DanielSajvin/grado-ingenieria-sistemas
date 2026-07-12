const express = require("express");
const app = express();

app.use(express.json());

// Filtrar Productos
const productos = [
    { nombre: "Laptop", precio: 800, categoria: "Tecnología" },
    { nombre: "Mouse", precio: 20, categoria: "Tecnología" },
    { nombre: "Cafetera", precio: 50, categoria: "Electrodomésticos" },
    { nombre: "Silla", precio: 100, categoria: "Muebles" },
    { nombre: "Teléfono", precio: 500, categoria: "Tecnología" }
  ];

app.get('/productos', (req, res) => {
    let {categoria, precioMax} = req.query;
    let productosFiltrados = productos;

    // filtrar por categoria cuando se especifique
    if (categoria) {
        productosFiltrados = productosFiltrados.filter(
            (p) => p.categoria.toLowerCase() === categoria.toLocaleLowerCase()
        );
    }

    // filtrar por precio Maximo
    if (precioMax) {
        productosFiltrados = productosFiltrados.filter(
            (p) => p.precio <= parseFloat(precioMax)
        );
    }

    res.status(200).json(productosFiltrados);
})


// Creación de usuarios

// const usuarios = []

app.post('/usuarios', (req, res) => {
    const {nombre, edad, correo} = req.body;

    // validaciones 
    if (!nombre || !edad || !correo) {
        res.status(400).json({ error: "Todos los campos (nombre, edad, correo) son obligatorios"});
    } 
    if (typeof nombre !== "string" || typeof correo !== "string") {
        return res.status(400).json({ error: "Nombre y correo deben ser cadenas de texto" });
    }
    if (typeof edad !== "number" || edad <= 0) {
        return res.status(400),express.json({error: 'La edad debe ser un numero.'})
    }

    // crear el usuario 
    const nuevoUsuario = {nombre, edad, correo};
    usuarios.push(nuevoUsuario); 
    res.status(201).json(usuarios); 
});


// actualizar datos de un usuario 
const usuarios = [
    { id: 1, nombre: "Juan Pérez", edad: 25 },
    { id: 2, nombre: "Ana López", edad: 30 },
    { id: 3, nombre: "Carlos Ramírez", edad: 22 }
];

// Endpoint PUT /usuarios/:id (Actualizar usuario)
app.put("/usuarios/:id", (req, res) => {
    const id = parseInt(req.params.id);
    const { nombre, edad } = req.body;
  
    // Buscar el usuario por ID
    const usuario = usuarios.find((u) => u.id === id);
    
    if (!usuario) {
      return res.status(404).json({ error: "Usuario no encontrado" });
    }
  
    // Validaciones opcionales antes de actualizar
    if (nombre && typeof nombre !== "string") {
      return res.status(400).json({ error: "El nombre debe ser una cadena de texto" });
    }
    if (edad && (typeof edad !== "number" || edad <= 0)) {
      return res.status(400).json({ error: "La edad debe ser un número positivo" });
    }
  
    // Actualizar solo los campos proporcionados
    if (nombre) usuario.nombre = nombre;
    if (edad) usuario.edad = edad;
  
    res.json({ mensaje: "Usuario actualizado exitosamente", usuario });
});

// Eliminar usuario)
app.delete("/usuarios/:id", (req, res) => {
    const id = parseInt(req.params.id);
  
    // Buscar el índice del usuario
    const indice = usuarios.findIndex((u) => u.id === id);
  
    if (indice === -1) {
      return res.status(404).json({ error: "Usuario no encontrado" });
    }
  
    // Eliminar usuario del arreglo
    usuarios.splice(indice, 1);
  
    res.json({ message: "Usuario eliminado correctamente" });
  });

app.listen(3000, () => {
    console.log('Servidor corriendo')
})