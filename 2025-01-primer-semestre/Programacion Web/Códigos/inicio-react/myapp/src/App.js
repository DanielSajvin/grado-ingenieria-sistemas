import React, { useEffect, useState } from "react";
import ListadoRecetas from "./components/ListadoRecetas";

function App() {
  const [recetas, setRecetas] = useState([]);
  const [cargando, setCargando] = useState(true);

  useEffect(() => {
    fetch("https://dummyjson.com/recipes")
      .then((res) => res.json())
      .then((data) => {
        // data.recipes es un array de recetas
        // Formateamos las recetas para que tengan la estructura deseada
        const recetasFormateadas = data.recipes.map((receta) => ({
          nombre: receta.name,
          descripcion: receta.ingredients.join(", "), // Convertimos los ingredientes a string
          imagen: receta.image,
        }));
        setRecetas(recetasFormateadas);
        setCargando(false);
      })
      .catch((error) => {
        console.error("Error al obtener recetas:", error);
        setCargando(false);
      });
  }, []);

  return (
    <div>
      {cargando ? (
        <p style={{ textAlign: "center" }}>Cargando recetas...</p>
      ) : (
        <ListadoRecetas recetas={recetas} />
      )}
    </div>
  );
}

export default App;
