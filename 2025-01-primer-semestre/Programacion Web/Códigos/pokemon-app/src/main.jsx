import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "normalize.css"; // <-- Asegúrate de importar esto primero
import "./index.css"; // <-- Luego tu CSS personalizado si hay

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
