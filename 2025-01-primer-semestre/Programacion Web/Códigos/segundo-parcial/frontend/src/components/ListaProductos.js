import { useEffect, useState } from "react";
import FormularioProducto from "./FormularioProducto";
import "./styles/ListaProducto.css";

function ListaProductos() {
  const [productos, setProductos] = useState([]);

  const cargarProductos = () => {
    fetch("http://localhost:3000/productos")
      .then((res) => res.json())
      .then((data) => setProductos(data))
      .catch((error) => console.error("Error al cargar productos:", error));
  };

  useEffect(() => {
    cargarProductos(); // Carga los productos al montar el componente
  }, []);

  return (
    <div className="contenedor-productos">
        <h2>Lista de Productos</h2>
        <FormularioProducto onProductoAgregado={cargarProductos} /> {/* Pasa la función para cargar productos al formulario */}
        <table className="tabla-productos">
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>Precio</th>
                </tr>
            </thead>

            <tbody>
                {productos.map((producto) => (
                    <tr key={producto.id}>
                        <td>{producto.nombre}</td>
                        <td>Q{producto.precio.toFixed(2)}</td>
                    </tr>
                ))}
            </tbody>
                
        </table>
    </div>
  )
}

export default ListaProductos;
// Este componente maneja la lista de productos y el formulario para agregar nuevos productos
