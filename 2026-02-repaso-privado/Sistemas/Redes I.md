## Modelos de Referencia 
Un modelo de referencia crea un estándar para que todos los fabricantes hagan sus equipos bajo esos estándares y no sea complicado trabajar con ellos. 

### Modelo OSI (Open Systems Interconnection)
Es un modelo conceptual y teórico de 7 capas:
1. Física
2. Enlace de datos
3. Red
4. Transporte 
5. Sesión
6. Presentación
7. Aplicación
El modelo OSI se usa para diagnosticar problemas dividiendo la red en partes lógicas. La regla siempre es investigar "de abajo hacia arriba", es decir, desde el cable físico hasta el software. 

### Modelo TCP/IP 
Es el modelo práctico el que realmente hace funcionar a internet. Tiene solo 4 capas: 
1. Acceso a la red
2. Internet
3. Transporte 
4. Aplicación
Lo que hace el modelo TCP/IP es resumir las 7 capas del modelo OSI a 4 capas más robustas y que están orientadas a la implementación real. 

## Tipos de Redes (Clasificación por alcance geográfico)
**LAN (Local Area Network - Red de Área Local)**, es una red que conecta computadoras y dispositivos dentro de un área geográfica pequeña y limitada, como una casa, un laboratorio o un edificio de oficinas. El objetivo principal de una LAN es compartir recursos e información a alta velocidad. 

**WLAN (Wireless Local Area)**, es lo mismo que una LAN, pero utilizando tecnologías inalámbricas (Wi-Fi) en lugar de cables.

**WAN (Wide Area Network - Red de Área Amplia)**, abarca áreas geográficas extensas, como ciudades, países o continentes. Su función principal es interconectar múltiples LANs, sepatadas por grandes distancias. Internet es la WAN pública más grande del mundo. 
## Dispositivos Fundamentales
**Hub (Capa 1 - Física)**, es un repetidor "tonto". No tiene memoria ni inteligencia. Si recibe un paquete de datos por el puerto 1 dirigido a la computadora del puerto 3, lo retransmite por todos los puertos. Esto satura el ancho de banda y actualmente se encuentra obsoleto. 

**Switch (Capa 2 - Enlace de Datos)**, es inteligente. Cuenta con una tabla de direcciones física (Direcciones MAC) y memoriza qué equipo está conectado a qué puerto. Si un paquete va para el puerto 3, el Switch únicamente lo envía al puerto 3. Esto aísla el tráfico y permite que las redes locales (LAN) sean rápidas y eficientes. 

**Router (Capa 3 - Red)**, mientras que el Switch conecta dispositivos dentro de una misma red local, el Router conecta redes diferentes entre sí. Por ejemplo, es el encargado de comunicar mi red de área local (LAN) con la red pública externa (Internet). Utiliza direcciones IP lógicas para enrutar los paquetes por el mejor camino posible. _Los routers enrutan datos entre diferentes redes_

**_Enrutar - Enrutamiento_**, _es la acción de encontrar y seleccionar el mejor camino posible para que un paquete de datos viaje de una red de origen a una red destino_

## Topologías de Red
Una topologías es el diseño que tiene la red. 

#### Topología Física 
Se refiere a cómo están conectados los cables y dispositivos visualmente o físicamente. Las más comunes son: 

**Topología en Estrella**:  todos los dispositivos finales (PCs, impresoras, servidores locales) se conectan mediante un cable individual a un nodo central. La gran ventaja es que si el cable de una computadora se rompe, solo ese equipo pierde conexión, el resto de la red sigue intacta. Es el estándar en las LAN modernas. 

**Topología en Bus**: todos los equipos se conectan a un único cable principal. Si ese cable central se corta, toda la red se cae. 

**Topología en Malla**: cada dispositivo está conectado físicamente a todos los demás dispositivos. Es muy costosa por la cantidad de cables, pero ofrecen redundancia total: si un camino falla, los datos pueden tomar muchos otros. Se usa en infraestructura crítica o entre routers de internet. 

![](../recursos/Pasted%20image%2020260812205358.png)
#### Topología Lógica
Se refiere a la forma en que los datos (las señales eléctricas) realmente viajan por el medio, sin importar cómo se vean los cables físicamente. 

## Capa Física
**_PDU de la capa 1, Bits (señales eléctricas, luz u ondas)_**
La función exclusiva de esta capa es la transmisión de bits puros (0s y 1s) a través de un medio Físico. A esta capa no le importa si esos bits son un documento PDF o una contraseña, su único trabajo es convertir datos lógicos en señales físicas (pulsos eléctricos, pulsos de luz u ondas de radio) y enviarlos. 

### Medio de transmisión
#### **Cables de Cobre (Pares trenzados - UTP y STP)**
Transmiten los datos mediante pulsos eléctricos. Tienen 8 hilos de cobre trenzados entre sí. 
_¿Por qué están trenzados?_ porque la corriente eléctrica genera campos electromagnéticos. Si los hilos fueran rectos, la señal de uno interferiría con el otro (fenómeno llamado Crosstalk o diafonía). Entonces trenzar los cables entre sí cancela matemáticamente esa interferencia. 

**UTP (Unshielded Twisted Pair)**, es el cable de red estándar. No tiene blindaje extra. Es barato y flexible, pero vulnerable a interferencias externas. 

**STP (Shielded Twisted Pair)**, tiene una malla metálica interior que envuelve los cables. Se usa en entornos industriales o donde hay mucha interferencia eléctrica. 

![](../recursos/Pasted%20image%2020260812214255.png)

**Categorías**:
- Cat5e, soporta hasta 1 Gbps.
- Cat6, soporta 1 Gbps (hasta 100 metros) y hasta 10 Gbps (pero solo si la distancia es menor a 55 metros).
- Cat6a, soporta 10 Gbps garantizados hasta los 100 metros. 

**Fibra Óptica**
Transmite los datos mediante fotones (pulsos de luz) a través de hilos de vidrio o plástico puro. 
_Ventaja_, es 100% inmune a la interferencia electromagnética y puede transmitir datos a kilómetros de distancia sin perder señal.
_Tipos_:
- Monomodo, usa un láser para distancias de decenas de kilómetros
- Multimodo, usa luces LED, más barato, para conectar cuartos de servidores dentro de un mismo edificio. 

**Transmisión Inalámbrica (Wi-Fi, Microondas)**
Transmite los datos modulando ondas electromagnéticas en el aire (banda ancha). Es susceptible a interferencia físicas (paredes gruesas, agua) y a interferencias de frecuencia (otras redes, microondas, Bluetooth).

_Atenuación, es la pérdida de potencia de la señal física a medida que viaja por el medio. _

## Capa de Enlace de Datos
**_PDU de la capa 2, trama o frame_**
Esta capa toma los bits crudos que suben por el cable y los agrupa en bloques lógicos y ordenados llamados _Tramas_.

**Direccionamiento Físico (Direcciones MAC)**
A este nivel no existen las direcciones IP. Los dispositivos se comunican usando la Dirección MAC (Media Access Control). Es una dirección física única en el mundo, que viene grabada en la tajeta de red de fábrica. 

**Acceso al medio**
Si dos computadoras envían datos por el cable al mismo milisegundo, las señales eléctricas chocan y se destruyen (colisión). 

**Detección y corrección de errores**: durante el viaje físico, la interferencia puede cambiar un 1 por un 0. Para evitar recibir datos corruptos, la capa de enlace añade un código matemático al final de la trama  (llamado FCS o CRC). El equipo que recibe el mensaje hace el mismo cálculo; si los números no coinciden, sabe que la trama se dañó y la descarta. 

**Protocolos de ventana**
Es un mecanismo de control de flujo. Sirve para que una computadora muy rápida no inunde de datos a una impresora más lenta, enviando la información por "ventanas" o bloques manejables. 

CRC, procedimiento matemático de la capa de enlace de datos que se coloca al final de cada trama para verificar que la información que se envía está completa.

_El cerebro de la capa 2 es el Switch_

## Capa de Red
DUDA REALMENTE QUE ES UNA IP
QUE SON LOS BITS

**_PD1 de la capa 3, paquete_**
#### Protocolos Esenciales de la capa de red

**IP (Internet Protocol)**, se encarga de ponerle la IP de origen y destino al paquete. Existe en sus versiones IPv4 e IPv6.
- **IPv4**, utiliza 32 bits y se representa en cuatro octetos decimales (192.168.1.10). El problema es que solo permite unos 4,300 millones de direcciones y ya se agotaron mundialmente. 
- **IPv6**, utiliza 128 bits y formato hexadecimal. Es el estándar moderno diseñado para solucionar la escasez de direcciones.
**IP pública vs IP privada**
- **IP Pública**, es el identificador único en todo internet. Esta la asigna el proveedor de internet (ISP).
- **IP Privada**, son direcciones reservadas exclusivamente para usarse de puertas para adentro (en una LAN, mi casa por ejemplo). Ninguna IP privada puede navegar por internet directamente.
**NAT (Network Address Translation)**, es el protocolo del router encargado de interceptar los paquetes, borrarles la IP privadas de origen y ponerles una IP pública y enviarlos a internet.

**ICMP (Internet Control Mesaage Protocol)**, es el protocolo de diagnóstico. Sirve para enviar mensajes de control y error. Herramienta más famosa _ping_ y también mensajes de error común _Destino Inalcanzable_.

**ARP (Address Resolution Protocol - Protocolo de Resolución de Direcciones)**, es el puente entre la capa 2 y la capa 3. Traduce direcciones IP lógicas a direcciones MAC físicas. Este protocolo funciona de la siguiente manera: 
1. **Caché local**, la computadora emisora primer revisa su propia memoria (la tabla ARP interna) para ver si ya preguntó por esa IP recientemente. 
2. **ARP Request - Broadcast**, si no la conoce, la computadora arma un mensaje especial y lo envía a la dirección MAC de "Broadcast" (FF:FF:FF:). Esto obliga al Switch a enviar el mensaje a absolutamente todos los dispositivos de la red. El mensaje llega a todos los dispositivos, el mensaje contiene la IP del dispositivo del cuál quiere averiguar la MAC.
3. **ARP Reply - Unicast**, entonces todos los dispositivos reciben el mensaje, pero solo el dueño de la IP (de ese Request) responde. Y responde ya con su MAC.
4. **Almacenamiento**, la computadora original recibe la MAC, la guarda en su caché, y ahora sí puede armar la trama del a Capa 2 para enviar los datos que necesite. 

