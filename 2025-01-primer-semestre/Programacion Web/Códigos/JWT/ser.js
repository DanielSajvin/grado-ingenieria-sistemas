const express = require('express');
const cors = require('cors');
const jwt = require('jsonwebtoken');
const cookieParser = require('cookie-parser');

const app = express();
app.use(express.json());
app.use(cookieParser());

// Permitir CORS con credenciales
app.use(cors({
  origin: 'http://localhost:3000',
  credentials: true
}));

const SECRET_KEY = 'clave_secreta';

// Ruta de login
app.post('/login', (req, res) => {
  const { usuario, contrasena } = req.body;

  // Validación simple
  if (usuario === 'admin' && contrasena === '1234') {
    const token = jwt.sign({ usuario }, SECRET_KEY, { expiresIn: '1h' });

    // Enviar cookie HTTP-only
    res.cookie('token', token, {
      httpOnly: true,
      sameSite: 'Lax',
      secure: false // true si usas HTTPS
    });

    res.json({ mensaje: 'Login exitoso' });
  } else {
    res.status(401).json({ mensaje: 'Credenciales inválidas' });
  }
});

// Ruta protegida
app.get('/perfil', (req, res) => {
  const token = req.cookies.token;

  if (!token) return res.status(401).json({ mensaje: 'No autorizado' });

  try {
    const decoded = jwt.verify(token, SECRET_KEY);
    console.log('Token recibido del cliente:', token);
    res.json({ usuario: decoded.usuario });
  } catch (error) {
    res.status(401).json({ mensaje: 'Token inválido' });
  }
});

app.listen(3001, () => {
  console.log('Servidor en http://localhost:3001');
});
