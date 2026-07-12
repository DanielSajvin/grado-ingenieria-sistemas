import React, { useState } from "react";
import "./styles/Login.css";

const Login = ({ onLogin }) => {
  const [usuario, setUsuario] = useState("");
  const [password, setPassword] = useState("");

  const manejarLogin = async (e) => {
    e.preventDefault();

    const res = await fetch("http://localhost:3000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ usuario, password }),
    });

    if (res.ok) {
      const data = await res.json();
      localStorage.setItem("token", data.token);
      onLogin(); // Redirigir o actualizar el estado
    } else {
      alert("Credenciales incorrectas");
    }
  };

  return (
    <div className="login-container">
      <h2>Iniciar sesión</h2>
      <form onSubmit={manejarLogin}>
        <input
          type="text"
          placeholder="Usuario"
          value={usuario}
          onChange={(e) => setUsuario(e.target.value)}
        />
        <input
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Ingresar</button>
      </form>
    </div>
  );
};

export default Login;
