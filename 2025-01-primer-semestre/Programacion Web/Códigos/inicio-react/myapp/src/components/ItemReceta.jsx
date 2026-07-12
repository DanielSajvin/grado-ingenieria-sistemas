import React from "react";
import "./ItemReceta.css"; // importamos los estilos

const ItemReceta = (props) => {
  return (
    <div className="item-receta">
      <img src={props.imagen} alt={props.nombre} className="item-imagen" />
      <div className="item-contenido">
        <h2 className="item-nombre">{props.nombre}</h2>
        <p className="item-descripcion">{props.descripcion}</p>
      </div>
    </div>
  );
};

export default ItemReceta;
