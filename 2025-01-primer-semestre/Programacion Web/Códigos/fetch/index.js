const express = require("express");

const app = express();

app.use(express.json());

// asyn, es como hacer un hilo solo para este request
app.get("/get-data-api-publica", async (req, res) => {
  try {
    // hacer la petición a la API pública
    const response = await fetch(
      "https://jsonplaceholder.typicode.com/posts/1"
    );

    // Si falla la respuesta, no es ok, se lanza el error
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    // convertir la respuesta a json
    const data = await response.json();

    // se envia la respuesta que serían los datos
    res.json(data);
  } catch (error) {
    console.error("Error: ", error);
    res.status(500).json({ error: "Error al obtener datos" });
  }
});

// enviar un nuevo post a la API pública
app.post("/send-data-api-publica", async (req, res) => {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title: "foo",
        body: "bar",
        userId: 1,
      }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    res.json(data);
  } catch (error) {
    console.error("Error: ", error);
    res.status(500).json({ error: "Error al enviar datos" });
  }
});

app.listen(3000, () => {
  console.log("Servidor corriendo");
});
