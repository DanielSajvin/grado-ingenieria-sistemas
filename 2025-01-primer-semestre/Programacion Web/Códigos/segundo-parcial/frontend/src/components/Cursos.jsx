import React, { useEffect, useState } from "react";
import "./styles/Cursos.css";

const Cursos = () => {
  const [cursos, setCursos] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem("token");

    fetch("http://localhost:3000/cursos", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => {
        if (res.status === 401) {
          throw new Error("No autorizado");
        }
        return res.json();
      })
      .then((data) => setCursos(data))
      .catch((err) => {
        alert("Debe iniciar sesión");
        console.error(err);
      });
  }, []);

  return (
    <div className="cursos-container">
      <h2>Cursos disponibles</h2>
      <ul>
        {cursos.map((curso) => (
          <li key={curso.id}>{curso.titulo}</li>
        ))}
      </ul>
  
    </div>
  );
};

export default Cursos;
