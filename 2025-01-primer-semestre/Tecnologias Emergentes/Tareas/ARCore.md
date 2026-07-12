<hr>

## ¿Qué es ARCore?
**ARCore** es una plataforma de Google que permite a los dispositivos Android crear experiencias de **realidad aumentada** (RA). Usa la cámara del dispositivo, sensores y procesamiento para superponer objetos digitales en el mundo real.

**A Nivel Técnico**
**ARCore** es un **SDK (Software Development Kit)** creado por Google que permite a los desarrolladores integrar **capacidades de Realidad Aumentada (RA)** en sus aplicaciones para Android (y también compatible con Unity y Unreal Engine).

## Tecnologías que utiliza 

### 1. **Pose Estimation (Estimación de Posición y Orientación)**
- Utiliza la cámara RGB + sensores del teléfono (IMU = Unidad de Medición Inercial).
- Estima la **pose** del dispositivo: posición en 3D y orientación (rotación en los 3 ejes: pitch, yaw, roll).
- Esto permite que el objeto virtual permanezca fijo aunque el usuario se mueva.
### 2. **Plane Detection (Detección de Superficies Planas)**
- Usa la imagen de la cámara para identificar **puntos clave (feature points)** y formar planos horizontales (piso, mesas).
- Puede usar algoritmos de detección como **FAST**, **ORB**, o técnicas basadas en la estructura del movimiento (**Structure from Motion**).

Saber dónde colocar el objeto (por ejemplo, un Pokémon parado sobre el suelo).
### 3. **Anchor System (Sistema de Anclaje)**
- Cuando un objeto se coloca en una posición, se crea un **"anchor"**.
- Este ancla permite que el objeto se **mantenga estable** en esa ubicación 3D, aunque el usuario se mueva.

Sin esto, los objetos parecerían flotar o desplazarse sin lógica.
### 4. **Environmental Understanding (Entendimiento del entorno)**
- Va más allá de planos: ARCore puede **detectar geometría 3D compleja**, como curvas o paredes.
- Esto permite que objetos virtuales **interactúen con el entorno real** (e.g., esconderse detrás de una mesa).
### 5. **Light Estimation (Estimación de Luz)**
- ARCore analiza la **luz ambiental** (intensidad, color).
- El motor de renderizado ajusta las **luces y sombras** del objeto virtual para que se integre de forma realista al entorno.

Usa histogramas de luminancia o mapas HDR simples para imitar la iluminación real.

## ¿Qué pasa cuando un Pokémon Aparece en nuestro entorno?
1. **La app usa ARCore para acceder a la cámara y sensores.**
2. **Detecta el plano del suelo y genera un ancla 3D.**
3. **El Pokémon se renderiza usando el motor gráfico (como Unity o Niantic Lightship).**
4. **ARCore actualiza la posición de la cámara mientras nos movemos.**
5. **El Pokémon reacciona al entorno gracias a la pose, luz y superficie detectadas.**

## ¿Qué tecnologías están involucradas?
- **Computer Vision (Visión por Computadora)**
- **Sensor Fusion (fusión de sensores IMU + cámara)**
- **Machine Learning (algunos modelos ayudan a detectar objetos o superficies)**
- **3D Rendering (motores como Unity, Unreal, OpenGL, Vulkan)**

## ¿Cómo interactúa Unity con ARCore en Pokémon GO?
### 1. **ARCore detecta el entorno**
- ARCore usa la cámara y los sensores del celular para:
    - Detectar superficies.
    - Rastrear el movimiento.
    - Estimar la luz ambiental.
### 2. **Unity renderiza el Pokémon**
- Unity recibe esa información (posición, rotación, luz).
- En base a eso, **renderiza el modelo 3D del Pokémon** usando sus herramientas gráficas internas (como shaders, iluminación, animaciones).
- Unity también permite que el Pokémon tenga físicas (por ejemplo, que reaccione si se lanza una pokébola mal).
### 3. **ARCore actualiza en tiempo real**
- Mientras te mueves, ARCore sigue enviando datos a Unity.
- Unity actualiza la posición del Pokémon en tiempo real para que parezca que **está en el mismo lugar del mundo real**, sin moverse.

## Requisitos de Hardware para utilizar ARCore
No todos los celulares pueden usar ARCore. Se necesita:
- **Cámara con buena resolución y enfoque automático.**
- **Sensores precisos**: acelerómetro, giroscopio y magnetómetro.
- **Procesador potente** (por ejemplo, Snapdragon 845 o superior).
- **Android 7.0+** (aunque lo ideal es Android 10+).
- **Google Play Services for AR** instalado (esto actualiza la compatibilidad con ARCore).

ARCore es una plataforma que actúa como puente entre el mundo real y lo virtual. Utiliza visión por computadora, algoritmos de mapeo 3D, y sensores del teléfono para entender el entorno y colocar objetos digitales en él. Gracias a esto, apps como Pokémon GO pueden colocar criaturas virtuales en el mundo físico, permitiendo al usuario interactuar con ellas como si estuvieran realmente ahí.

<hr>

# Top 10 aplicaciones de Realidad Aumentada
### 1. **Pokémon GO**
El clásico de Niantic sigue siendo líder en juegos de RA, permitiendo capturar criaturas en el mundo real y participar en eventos comunitarios. 
### 2. **IKEA Place**
Esta aplicación te permite visualizar muebles en tu hogar mediante RA, facilitando la decoración y planificación del espacio. ​
### 3. **Google Lens 2.0**
Una herramienta versátil que reconoce objetos, traduce textos en tiempo real y ofrece información contextual utilizando la cámara de tu dispositivo. ​
### 4. **Snapchat (Snap AR)**
Más allá de los filtros divertidos, Snapchat ha integrado experiencias de RA avanzadas, incluyendo pruebas virtuales de productos y juegos interactivos.
### 5. **AR Learn**
Plataforma educativa que ofrece experiencias inmersivas en historia, ciencias y matemáticas, transformando el aprendizaje en una aventura interactiva.
### 6. **Quiver**
Convierte dibujos en modelos 3D animados mediante RA, ideal para fomentar la creatividad en niños y facilitar el aprendizaje visual. 
### 7. **AR Measure Kit**
Convierte tu smartphone en una herramienta de medición precisa, permitiéndote medir distancias y dimensiones de objetos en tiempo real. ​
### 8. **Houzz**
Aplicación de diseño de interiores que utiliza RA para visualizar cómo quedarían diferentes productos y estilos en tu hogar. ​
### 9. **Google Maps Live View**
Función que superpone direcciones y puntos de interés en el entorno real a través de la cámara, facilitando la navegación peatonal en ciudades.
### 10. **SkyView**
Ideal para los amantes de la astronomía, esta app te permite identificar estrellas, planetas y constelaciones en el cielo nocturno utilizando RA.