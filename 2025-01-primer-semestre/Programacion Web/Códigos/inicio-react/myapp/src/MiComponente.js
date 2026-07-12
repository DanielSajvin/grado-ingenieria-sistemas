import React, { useState } from "react";

export default function MiComponente() {
  const [saludo, setSaludo] = useState(""); // recibe un valor inicial, y el de primero va el valor de la variable y el segundo la funcion que va a cambiar el valor de la variable

  const clickHandler = () => {
    setSaludo("Hola, Daniel"); // cambia el valor de la variable saludo
  };

  return (
    <div>
      <h2>{saludo}</h2>
      <button onClick={clickHandler}>Ejemplo de componente en React</button>
    </div>
  );
}
