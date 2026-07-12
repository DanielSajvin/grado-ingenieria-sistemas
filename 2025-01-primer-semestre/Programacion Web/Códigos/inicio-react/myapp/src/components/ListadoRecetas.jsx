import React from "react";
import ItemReceta from "./ItemReceta";

const ListadoRecetas = ({ recetas }) => {
  return (
    <div>
      <h1 style={{ textAlign: "center", color: "#4CAF50" }}>
        Lista de Recetas
      </h1>
      {recetas.map((receta, index) => (
        <ItemReceta
          key={index}
          nombre={receta.nombre}
          descripcion={receta.descripcion}
          imagen={receta.imagen}
        />
      ))}
    </div>
  );
};

export default ListadoRecetas;
