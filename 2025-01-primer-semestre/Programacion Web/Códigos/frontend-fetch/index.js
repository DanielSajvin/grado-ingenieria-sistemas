document
  .getElementById("userForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // evita que la pagina se recargue

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    // crear objeto con los datos
    const userData = {
      name: name,
      email: email,
    };

    // enviar datos mediante fetch con post
    fetch("https://jsonplaceholder.typicode.com/posts", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userData),
    })
      .then((response) => response.json())
      .then((data) => {
        document.getElementById("mesagge").textContent =
          "Usuario registrado con exito" + JSON.stringify(data);
        console.log("Respuesta del servidor: ", data);
      })
      .catch((error) => console.log("Error al enviar datos: ", error));
  });

document.addEventListener("DOMContentLoaded", function () {
  const userTableBody = document.getElementById("userTableBody");

  // Función para agregar un usuario a la tabla
  function addUserToTable(id, name, email) {
    const row = document.createElement("tr");
    row.innerHTML = `<td>${id}</td><td>${name}</td><td>${email}</td>`;
    userTableBody.appendChild(row);
  }

  // Obtener usuarios de la API y mostrarlos en la tabla
  fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((users) => {
      users.forEach((user) => addUserToTable(user.id, user.name, user.email));
    })
    .catch((error) => console.error("Error al obtener usuarios:", error));

  // Manejo del formulario para agregar un nuevo usuario
  document
    .getElementById("userForm")
    .addEventListener("submit", function (event) {
      event.preventDefault();

      const name = document.getElementById("name").value;
      const email = document.getElementById("email").value;

      const userData = { name, email };

      fetch("https://jsonplaceholder.typicode.com/posts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(userData),
      })
        .then((response) => response.json())
        .then((data) => {
          // Simula un ID único
          const newId = Date.now();

          // Agregar el usuario a la tabla sin recargar la página
          addUserToTable(newId, name, email);

          // Mensaje de éxito
          document.getElementById("mesagge").textContent =
            "Usuario registrado con éxito";

          // Limpiar inputs
          document.getElementById("userForm").reset();
        })
        .catch((error) => {
          console.error("Error al enviar datos:", error);
          document.getElementById("mesagge").textContent =
            "Error al registrar usuario.";
        });
    });
});
