import React, { useState } from 'react';

function App() {
  const [usuario, setUsuario] = useState('');
  const [contrasena, setContrasena] = useState('');
  const [perfil, setPerfil] = useState(null);

  const login = async () => {
    const res = await fetch('http://localhost:3001/login', {
      method: 'POST',
      credentials: 'include', // Importante para cookies
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ usuario, contrasena })
    });

    const data = await res.json();
    console.log(data);
  };

  const obtenerPerfil = async () => {
    const res = await fetch('http://localhost:3001/perfil', {
      method: 'GET',
      credentials: 'include' // Importante para enviar cookies
    });

    const data = await res.json();
    console.log('Respuesta perfil:', data);
    setPerfil(data);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Login con Cookie HTTP-only</h2>
      <input
        type="text"
        placeholder="Usuario"
        value={usuario}
        onChange={(e) => setUsuario(e.target.value)}
      />
      <br />
      <input
        type="password"
        placeholder="Contraseña"
        value={contrasena}
        onChange={(e) => setContrasena(e.target.value)}
      />
      <br />
      <button onClick={login}>Login</button>
      <button onClick={obtenerPerfil}>Obtener Perfil</button>

      {perfil && (
        <div>
          <h3>Usuario autenticado: {perfil.usuario}</h3>
        </div>
      )}
    </div>
  );
}

export default App;
