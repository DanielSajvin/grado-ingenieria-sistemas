import React, { useState, useEffect } from "react";
import "./Contador.css"; // Importamos los estilos externos

const Counter = () => {
  const [count, setCount] = useState(0);
  const [message, setMessage] = useState("El número no es divisible entre 6");

  // useEffect para actualizar el mensaje cuando cambia el contador
  useEffect(() => {
    if (count !== 0 && count % 6 === 0) {
      setMessage("El número es divisible entre 6");
    } else {
      setMessage("El número no es divisible entre 6");
    }
  }, [count]); // Se ejecuta cada vez que 'count' cambia

  return (
    <div className="counter-container">
      <h2>Contador: {count}</h2>
      <p
        className={`divisibility-text ${
          count % 6 === 0 && count !== 0 ? "divisible" : "not-divisible"
        }`}
      >
        {message}
      </p>
      <div>
        <button
          onClick={() => setCount(count + 1)}
          style={{ backgroundColor: "green", color: "white", margin: "5px" }}
        >
          Sumar
        </button>
        <button
          onClick={() => setCount(count - 1)}
          style={{ backgroundColor: "red", color: "white", margin: "5px" }}
        >
          Restar
        </button>
        <button onClick={() => setCount(0)} className="reset-button">
          Resetear
        </button>
      </div>
    </div>
  );
};

export default Counter;
