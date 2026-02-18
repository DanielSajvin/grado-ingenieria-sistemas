<hr>

## Introducción a la Virtualización 
La virtualización surge para cumplir con crecimiento rápido, menor consumo de recursos y para asegurar disponibilidad todo el tiempo, claramente para ya no depender de recursos físicos. 

_Problemas del modelo tradicional_
Un servidor = una función 
Costos altos, alta demanda de energía y refrigeración, espacio físico dedicado, bajo aprovechamiento del hardware, escalabilidad lenta, recuperación ante fallos complicada

### Cambio del concepto de centro de datos (de físico a virtualizado)
*Data Center Tradicional (Físico)*
Enfoque en hardware independiente
- Cada servidor hace una sola tarea, mucho cableado y mantenimiento manual 

*Data Center Consolidado (Pre-virtualización)*
- Se compran equipos más potentes
- Se agrupan funciones en menos servidores 
- La administración sigue siendo física
- La eficiencia mejora, pero aún es limitada 

*Data Center Virtualizado (Actual)*
- Capas virtuales entre hardware y servicios 
- Creación de máquinas virtuales bajo demanda 
- Alta densidad y consolidación 
- Automatización y movilidad de cargas 
- Preparado para nube privada y pública 

### ¿Qué es la Virtualización?

**_Es una tecnología que permite crear versiones virtuales de recursos físicos. Abstraer recursos físicos a lógicos_**

Virtualizar es crear recursos computacionales virtuales (servidores, discos, redes) dentro de un hardware físico real. Una máquina física puede alojar múltiples máquinas virtuales, cada una con su propio sistema operativo y aplicaciones. 

**Virtualización y la Nube**
La virtualización es el cómo (la tecnología), y la nube es el qué (el servicio que se entrega gracias a esa tecnología). 

_La Nube_
Es alquilar recursos a proveedores en la nube (AWS)

---

## Tipos de virtualización
Más usados en centros de datos: 
- Virtualización de servidores
- Virtualización de red 
- Virtualización de almacenamiento 

*Beneficios generales de virtualizar*
- Aprovechamiento del hardware 
- Implementaciones más rápidas 
- Recuperación ante fallos
- Reducción de costos 
- Mayor disponibilidad 
- Automatización y escalabilidad 

### **Virtualización de servidores**
Es la capacidad de ejecutar múltiples servidores virtuales sobre un solo servidor físico. Se logra mediante un hipervisor, que administra los recursos. 

_Hipervisor_, software que crea y gestiona máquinas virtuales
Tipo 1 (bare metal), Tipo 2 (hosted)
_Beneficios de virtualizar servidores_, consolidación de servidores, aislamiento entre máquinas, migraciones en caliente, creación de entornos de prueba 

### **Virtualización de Red**
Permite crear redes virtuales que funcionan sobre redes físicas. Consiste en separar el tráfico lógico de la infraestructura física. 

**1. SDN (Software-Defined Networking / Redes Definidas por Software):**
- **El concepto:** SDN separa el "cerebro" de la red de los "músculos".
- **El criterio:** En un router tradicional, el plano de control (el cerebro que decide por dónde va el tráfico basándose en tablas de enrutamiento) y el plano de datos (el músculo que físicamente empuja el paquete por el cable) están en la misma caja de metal. SDN saca el "cerebro" y lo centraliza en un software controlador. Los switches físicos ahora solo reciben órdenes del controlador sobre qué hacer con los paquetes. Esto permite programar y cambiar el comportamiento de toda la red desde un solo panel de control, al instante.
	- _Todo en un panel de control accesible_
**2. NFV (Network Functions Virtualization / Virtualización de Funciones de Red):**
- **El concepto:** Consiste en tomar servicios de red que antes requerían hardware especializado (como un Firewall de hardware, un Balanceador de Carga o un detector de intrusos - IDS) y convertirlos en máquinas virtuales (software).
- **El criterio:** Si necesitas implementar un firewall de Palo Alto o Cisco, ya no compras la caja metálica y esperas a que llegue por paquetería para enrackarla. Simplemente despliegas una Máquina Virtual con el sistema operativo de ese firewall en cualquier servidor estándar que ya tengas.
	- _Máquina virtual con el sistema operativo del dispositivo que se necesite_

### **Virtualización de almacenamiento**
Agrupa los recursos físicos de múltiples dispositivos de almacenamiento en red para que parezcan un único dispositivo de almacenamiento lógico centralizado. 

_Tecnologías comunes_
#### 1. NAS (Network Attached Storage - Almacenamiento Conectado en Red)
Piensa en el NAS como un servidor de archivos súper optimizado. Es un dispositivo físico (o virtual) que se conecta directamente a tu red local (LAN) estándar, usando los mismos cables Ethernet y switches por donde viaja el tráfico normal de internet o de tus aplicaciones.
#### SAN (Storage Area Network - Red de Área de Almacenamiento)
Si el NAS usa las "calles públicas" (tu LAN), la SAN es una "autopista privada de alta velocidad" construida exclusivamente para que los servidores hablen con los discos duros. Es una red dedicada y separada de tu red local normal.
- **El Concepto Clave (Acceso a nivel de Bloques):** Aquí está la gran diferencia. Una SAN no sabe qué es un "archivo". La SAN entrega "bloques" de disco crudos al servidor. El sistema operativo de tu servidor formatea ese bloque y cree que tiene un disco duro físico conectado directamente a su placa base, aunque el disco real esté en otra habitación.

---

## Hipervisores
Un hipervisor es el software especializado que hace posible la virtualización de sistemas. Actúa como una capa de abstracción entre le hardware físico y las máquinas virtuales. 

_Funciones Principales_
1. Crear y gestionar máquinas virtuales independientes 
2. Administrar y distribuir recursos del hardware físico 
3. Garantizar el aislamiento entre máquinas virtuales 
4. Optimizar el rendimiento del sistema completo 

### Hipervisor de Tipo 1 (Bare Metal)
Se instala directamente sobre el hardware físico, sin necesidad de un sistema operativo previo que actúe como intermediario. 
Este ofrece el máximo rendimiento posible, ya que elimina las capas innecesarias entre el hardware y las máquinas virtuales. 

_**Ventajas**_
- Alto rendimiento
- Mayor estabilidad 
- Mejor aislamiento 
- Uso profesional 

### Hipervisor de Tipo 2 (Hosted)
Se instala encima de un sistema operativo convencional que ya está funcionando en la computadora. A diferencia del Tipo 1, no tiene acceso directo al hardware. 
_Funciona como una aplicación más dentro del sistema operativo anfitrión_

_**Ventajas**_
- Facilidad de instalación
- Uso en PCs personales 
- Rendimiento moderado 
- Ideal para educación 

### Arquitectura básica de virtualización 
Un entorno virtualizado se estructura en capas, esto porque ofrece flexibilidad, escalabilidad y facilita el mantenimiento del entorno completo, las capas son las siguientes: 
1. Capa física, hardware real (procesador, RAM, disco duro)
2. Capa de virtualización, el hipervisor que distribuye los recursos físicos entre cada máquina virtual creada 
3. Capa Virtual, cada máquina virtual funcionando de forma independiente como si fuera una computadora o servidor físico 
4. Capa lógica, los sistemas operativos invitados, es decir, cada sistema operativo de cada máquina virtual creada 

