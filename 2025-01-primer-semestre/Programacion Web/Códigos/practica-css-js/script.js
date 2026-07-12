function agregarAlCarrito(idProducto, nombreProducto, descripcionProducto, imagenProducto) {
    const carrito = document.getElementById("carrito");

    // crea elemento li
    let nuevoItem = document.createElement('li');

    // crea div para almancenar toda la infor del producto 
    let contenedor = document.createElement('div');
    contenedor.classList.add('elemento-carrito');

    let imagen = document.createElement('img')
    imagen.src = imagenProducto;
    imagen.alt = nombreProducto;
    imagen.classList.add('imagen-producto')


    // h1 para el titulo
    let titulo = document.createElement('h1');
    titulo.textContent = nombreProducto;

    // p para la descripcion
    let descripcion = document.createElement('p');
    descripcion.textContent = descripcionProducto;

    // crea boton para eliminar el producto 
    let botonEliminar = document.createElement('button');
    botonEliminar.textContent = 'Borrar';

    // elimina el elemento li en el que se encuentre 
    botonEliminar.onclick = function () {
        carrito.removeChild(nuevoItem);
    }

    // agrega el h1, p y el boton al div
    contenedor.appendChild(imagen);
    contenedor.appendChild(titulo);
    contenedor.appendChild(descripcion);
    contenedor.appendChild(botonEliminar);

    // agregar el div con todos sus elementos al elemento li, es decir, a la lista
    nuevoItem.appendChild(contenedor);

    // agrega el li con todo ya listo a la lista para ser vista 
    carrito.appendChild(nuevoItem);
}
