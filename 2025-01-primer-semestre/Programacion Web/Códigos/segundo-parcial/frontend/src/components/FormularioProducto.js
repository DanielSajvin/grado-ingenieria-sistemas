import { useState } from "react";
import "./styles/FormularioProducto.css";

function FormularioProducto({ onProductoAgregado }) {
  const [nombre, setNombre] = useState("");
  const [precio, setPrecio] = useState("");

  // Maneja el evento de cambio (manejo de envío)
  const handleSubmit = async (e) => {
    e.preventDefault(); // Evita el comportamiento por defecto del formulario

    const nuevoProducto = { nombre, precio };

    // Enviar el nuevo producto al backend
    const res = await fetch("http://localhost:3000/productos", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(nuevoProducto),
    });

    const data = await res.json();
    onProductoAgregado(data); // Llama a la función para agregar el producto a la lista
    setNombre(""); // Limpia el campo de nombre
    setPrecio(""); // Limpia el campo de precio
  };

  return (
    <form className="formulario" onSubmit={handleSubmit}>
      <h3>Agregar Producto</h3>
      <input
        type="text"
        placeholder="Nombre del producto"
        value={nombre}
        onChange={(e) => setNombre(e.target.value)} // Maneja el cambio en el campo de nombre
        required
      />
      <input
        type="number"
        step="0.01"
        placeholder="Precio del producto"
        value={precio}
        onChange={(e) => setPrecio(e.target.value)} // Maneja el cambio en el campo de precio
        required
      />
      <button type="submit">Agregar Producto</button>
    </form>
  );
}

export default FormularioProducto;
// Este componente maneja el formulario para agregar un nuevo producto
