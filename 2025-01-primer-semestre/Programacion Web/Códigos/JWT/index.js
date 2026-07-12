// backend/index.js
const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());

app.get('/fecha-nacimiento', (req, res) => {
  res.json({ fecha: '1995-06-15' });
});

app.listen(3001, () => {
  console.log('Servidor backend en http://localhost:3001');
});
