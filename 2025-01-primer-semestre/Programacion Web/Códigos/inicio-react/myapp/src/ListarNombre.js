import React, { useState, useEffect } from "react";
import "./ListaNombre.css"; // Importamos los estilos

const NameList = () => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [showButton, setShowButton] = useState(false);

  // useEffect para actualizar la visibilidad del botón
  useEffect(() => {
    if (firstName.trim() !== "" && lastName.trim() !== "") {
      setShowButton(true);
    } else {
      setShowButton(false);
    }
  }, [firstName, lastName]); // Se ejecuta cuando cambian firstName o lastName

  return (
    <div className="name-form-container">
      <h2>Ingrese su Nombre y Apellido</h2>
      <input
        type="text"
        placeholder="Nombre"
        value={firstName}
        onChange={(e) => setFirstName(e.target.value)}
      />
      <input
        type="text"
        placeholder="Apellido"
        value={lastName}
        onChange={(e) => setLastName(e.target.value)}
      />

      {showButton && <button className="next-button">Siguiente</button>}
    </div>
  );
};

export default NameList;
