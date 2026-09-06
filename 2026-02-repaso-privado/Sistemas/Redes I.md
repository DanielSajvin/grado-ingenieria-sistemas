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

<hr>

## Teoría de la Comunicación de Datos
Los datos digitales deben codificarse en señales físicas. 
- **Señalización**, si usamos cables de cobre (eléctricos), los bits se representan mediante variaciones de voltaje (por ejemplo, codificación Manchester o NRZ). Si usamos fibra óptica, se representan mediante pulsos de luz (fotones). Si es conexión inalámbrica, usamos ondas electromagnéticas (radiofrecuencia) modulando amplitud, frecuencia o fas. 
- **Fenómenos que Afectan a la Red**, la señal sufre _Atenuación_(pérdida de fuerza con la distancia), _Ruido_(interferencia electromagnética externa) y _Diafonía o Crosstalk_(interferencia generada por un cable o dispositivo cercano o adyacente). El diseño físico debe mitigar esto. 

## Cableado Estructurado 
Es una infraestructura de red estandarizada que permite integrar servicios de datos, voz y video en un edificio o campus de manera predecible y escalable. No es solo "tirar cables"; es una arquitectura. Se divide en 6 subsistemas principales: 
1. **Facilidades de Entrada**, el punto donde el cableado del proveedor de servicios de internet (ISP) entra al edificio y se conecta con el cableado interno. 
	1. El proveedor de internet (ISP) introduce su cable al edificio y coloca su módem/router principal, estableciendo el límite entre su red y la red privada.
2. **Cuarto de Equipos**, el "cerebro" centralizado. Aquí viven los routers principales, switches core y servidores. 
	1. Aquí se ubica el router de la empresa, los firewalls perimetrales, servidores y el Switch Core. 
3. **Cableado Vertebral**, proporciona interconexión entre los cuartos de telecomunicaciones, el cuarto de equipos y la entrada de servicios. Por lo general, se implementa con Fibra Óptica para soportar altos anchos de banda a largas distancias, uniendo diferentes pisos o edificios. 
	1. Desde el Switch Core en el primer piso, salen cables de fibra óptica verticales hacia los demás niveles del edificio. 
4. **Cuarto de Telecomunicaciones**, distribuidores intermedios ubicados típicamente en cada piso. Aquí el cableado backbone (que viene del cuarto de equipos) se conecta a los switches de acceso, y de ahí sale el cableado hacia los usuarios. 
	1. Hay un cuarto (por ejemplo en el quinto piso) secundario. La fibra del backbone entra a este cuarto y se conecta a un "Switch de Acceso", que es el encargado de dar puertos a los usuarios de ese piso.
5. **Cableado Horizontal**, es el cableado que va desde el panel de parcheo (patch panel) en el cuarto de telecomunicaciones hasta la toma de pared (roseta) del usuario. Por estándar, nunca debe exceder los 90 metros de cable sólido (dejando 10 metros para cables de parcheo flexibles, sumando un máximo teórico de 100 metros). Generalmente se usa cable de par trenzado. 
	1. Desde el Swtich de Acceso, se tiran decenas de cables de cobre Cat6 por el techo hacía cada cubículo. Este tramo jamás debe superar los 90 metro sólidos. 
6. **Área de Trabajo**, el espacio donde interactúa el usuario final. Incluye el cable de parcheo (patch cord) que va desde la toma de pared hasta la PC, teléfono o impresora. 
	1. El cable Cat6 termina en un Jack o roseta empotada en la pared del cubículo. Se utiliza un cable de parcheo (Patch Cord) flexible hasta 10 metros para conectar la roseta a la PC. 

<hr>

Las arquitecturas empresariales se diseñan utilizando un modelo jerárquico de diseño, usualmente de tres capas: _Acceso, Distribución y Núcleo/Core_.

**Backbone**
Es la carretera física principal (generalmente fibra óptica de alta capacidad) que une las diferentes redes locales, edificios o cuartos de telecomunicaciones. Su único propósito es mover grandes volúmenes de datos de un punto a otro. 

**Switch Core**
Es el dispositivo de hardware central en la topología lógica. Conecta los switches de las capas inferiores y conmuta paquetes a la máxima velocidad posible, omitiendo políticas de seguridad o listas de acceso granulares para no ralentizar la red. 

<hr>
### Medios de Transporte Principales

**Par Trenzado (UTP/STP)**
Cobre. Se trenza para cancelar la interferencia electromagnética (diafonía). El STP tiene blindaje metálico para entornos industriales con mucho ruido electromagnético. Tienen las siguientes categorías: 

| Categoría | Velocidad Máxima                   | Frecuencia | Distancia Máxima | Uso Recomendado                                                                    |
| --------- | ---------------------------------- | ---------- | ---------------- | ---------------------------------------------------------------------------------- |
| Cat5e     | 1 Gbps                             | 100 MHz    | 100 metros       | Instalaciones antiguas o redes domésticas básicas                                  |
| Cat6      | 1 Gbps (hasta 10 Gbps a 55 metros) | 250 MHz    | 100 metros       | Estándar comercial base para corporativos estándar                                 |
| Cat6a     | 10 Gbps                            | 500 MHz    | 100 metros       | Enlaces de alta densidad, puntos de acceso WiFi de última generación               |
| Cat7      | 10 Gbps (blindado STP)             | 600 MHz    | 100 metros       | Entornos industriales con mucha interferencia electromagnética                     |
| Cat8      | 25 Gbps / 40 Gbps                  | 2000 MHz   | 30 metros        | Conexiones ultracortas de switch a servidor dentro de un mismo rack en datacenters |
**Fibra Óptica**
La fibra óptica transmite fotones a través de un hilo de vidrio ultrapuro. Funciona mediante el _principio de reflexión interna total_. El hilo consta de un núcleo central por donde viaja la luz y un revestimiento exterior con un índice de refracción diferente, actuando como un espejo continuo. Los pulsos de luz rebotan en las paredes internas sin escapar del cable. Existen dos tipos de fibra óptica: 
1. **Multimodo (MMF)**, núcleo más grueso, la luz rebota en múltiples ángulos (modos). Usa LEDs o láseres de bajo costo. Ideal para distancias cortas (backbone dentro de un mismo edificio). Tiene un alcance entre 300 metros y 2 kilómetros.
2. **Monomodo (SMF)**, núcleo extremadamente delgado, la luz viaja en línea recta (un solo modo) generada por láseres de alta potencia. Ideal para kilómetros de distancia (backbone entre edificios). Tiene un alcance entre 10 kilómetros hasta 100 o 160 kilómetros. 

## Propósito de los Modelos y la Encapsulación
Históricamente, los fabricantes creaban hardware y software de red que solo funcionaba con sus propios equipos. Para solucionar esto, la ISO creó el _Modelo OSI (Interconexión de Sistemas Abiertos)_ como un marco conceptual de 7 capas. Sin embargo, el _Modelo TCP/IP_ (creado por el departamento de la Defensa de EE.UU.) fue el que se implementó en la práctica para dar vida a internet. 

**Encapsulamiento**
La información no viaja como un bloque sólido. A medida que los datos bajan por las capas (desde la aplicación del usuario hasta el cable), cada capa le añade un "encabezado" con información de control. Este proceso de añadir ese encabezado es lo que se conoce como **Encapsulamiento**. La unidad de información en cada capa recibe un nombre técnico específico llamado PDU (Protocol Data Unit): 
- *Capas 7, 6 y 5*: _Datos (Data)_
- *Capa 4: Segmento (TCP) o Datagrama (UDP)*
- *Capa 3: Paquete (Packet)*
- *Capa 2: Trama (Frame)*
- *Capa 1: Bits*

### Análisis de las Capas del Modelo OSI

**Capa 7: Aplicación**
Es la interfaz directa entre los programas de red y el usuario. No es "la aplicación de software" en sí (no es el ejecutable de algún programa o el navegador web), sino los servicios de red que esas aplicaciones utilizan para comunicarse hacia el exterior. 
_Protocolos Principales_: HTTP/HTTPS (navegación), FTP(transferencia de archivos), SMTP/POP3(correo electrónico), DNS (resolución de nombres), SSH(terminal segura) y los protocolos propios de cada programa. 

**Capa 6: Presentación**
Actúa como el "traductor" de la red. Garantiza que la información enviada por la capa de aplicación de un sistema pueda ser leída por la capa de aplicación de otro. Se encarga del formato de los datos, la comprensión y la encriptación. 
_Protocolos/Estándares_, ASCII, EBCDIC, JPEG, MPEG, MIDI y protocolos de encriptación y seguridad como TLS/SSL (que cifran el tráfico HTTPS).

**Capa 5: Sesión**
Establece, administra y finaliza las sesiones de comunicación entre dos hosts. Mantiene separados los datos de diferentes aplicaciones e implementa puntos de control (sincronización). Si una descarga grande falla, la capa de sesión permite retomarla desde el último punto de control en lugar de iniciar desde cero. 
_Protocolos Principales_, NetBIOS, RPC(Remote Procedure Call), PAP. 

**Capa 4: Transporte**
Toma los Datos de las capas superiores y los divide en piezas más pequeñas. Esta capa decide cómo se enviará la información: garantizando la entrega exacta y en orden, o enviándola lo más rápidos posible sin importar si se pierde algún fragmento. Además, asigna Puertos Lógicos (como el puerto 80 para web) para saber a qué aplicación exacta debe entregar la información dentro del equipo receptor. 
_PDU_: segmento si se usa TCP o datagrama si se usa UDP.
_Protocolos Principales_: TCP (Transmission Control Protocol) y UPD (User Datagram Protocol).

**Capa 4: Red**
Proporciona direccionamiento lógico (direcciones IP) y determina la mejor ruta para que la información viaje desde una red origen hasta una red destino a través de múltiples routers. Es el GPS de internet. 
_PDU_: paquete (Packet)
_Protocolos Principales_: IPv4, IPv6, ICMP(usado por el comando ping), e IPsec. También operan aquí los protocolos de enrutamiento dinámico (OSPF, EIGRP, BGP).

**Capa 2: Enlace de Datos**
Toma los paquetes IP y los prepara para viajar por el medio físico local. Se encarga del direccionamiento físico mediante las direcciones MAC. Además detecta errores que pudieron ocurrir en el cable (mediante un cálculo matemático llamado FCS) y controla el acceso al medio (quién habla y quién escucha en la red local).
_PDU_: trama (Frame)
_Protocolos/Estándares Principales_: Ethernet, Wi-Fi, ARP(Address Resolution Protocol).

**Capa 1: Física**
Convierte las tramas en señales eléctricas, ópticas o de radio frecuencia (bits: ceros y unos) para ser transmitidas por el medio físico.
_PDU:_ Bits

### Análisis Modelo TCP/IP

| Capa - Modelo TCP/IP | Capas OSI equivalentes           | Función Principal                                                                   |
| -------------------- | -------------------------------- | ----------------------------------------------------------------------------------- |
| Aplicación           | Aplicación, Presentación, Sesión | Representa datos para el usuario y controla la codificación/diálogo                 |
| Transporte           | Transporte                       | Admite la comunicación entre distintos dispositivos, puertos y fiabilidad (TCP/UDP) |
| Internet             | Red                              | Determina la mejor ruta a través de la red (IP, ICMP)                               |
| Acceso a la Red      | Física, Enlace de Datos          | Controla el Hardware y los medios físicos                                           |

## Modelo OSI 

### Capa 1: Capa Física
El objetivo de la capa física es la transmisión y recepción de una secuencia no estructurada de bits sin procesar a través de un medio físico. Toma la información lógica (cero y unos) y la codifica en señales físicas compatibles con el medio (variaciones de voltaje en el cobre, pulsos de luz en la fibra óptica o microondas en el aire).

**PDU (Unidad de Datos del Protocolo)**
Bits

**Protocolos y Estándares**

**Dispositivos y Hardware**
En la capa 1 pura, los dispositivos no toman decisiones de enrutamiento ni filtran tráfico; son simplemente "multiplicadores" o "traductores" de energía. 
- **Hub**, es un repetidor multipuerto. Si recibe una señal eléctrica por el puerto 1, la amplifica y la escupe por todos los demás puertos. Es tonto; no lee direcciones. 
- **Repetidores**, su función es regenerar la señal atenuada por la distancia. Si un cable de cobre llega a sus 100 metros, un repetidor inyecta energía nueva para empujar la señal otros 100 metros. 
- **Transceptores/Módulos SFP (Small Form-factor Pluggable)**, son pequeños módulos metálicos intercambiables que se insertan en los switches corporativos. Actúan como conversores de medios. Toman la señal eléctrica interna del switch y la convierte en pulsos láser (fibra óptica) o viceversa. 

<hr>

**Modos de Transmisión**
Definen cómo fluye la información en un canal físico. Existen tres modos fundamentales: 
1. **Simplex**, la comunicación es unidireccional. Un equipo solo envía y el otro solo recibe. Ejemplo, una estación de radio FM o un teclado enviando datos a la PC. 
2. **Half-Duplex (Semi-Duplex)**, la comunicación es bidireccional, pero no simultánea. O solo se envía información o solo se recibe información, pero no ambas cosas a la vez. 
3. **Full-Duplex (Dúplex Completo)**, la comunicación es bidireccional y simultánea. El cable de red moderno usa pares de hilos separados para enviar y recibir al mismo tiempo.

<hr>

### Capa 2: Enlace de Datos
Toma los paquetes que vienen de la capa superior (Red) y los encapsula agregándoles un encabezado (Header) y un final (Trailer). Su función es entregar de manera confiable esta información de un nodo a otro directamente conectando dentro de la misma red loca (LAN). 
- **Direccionamiento Físico (MAC)**, utiliza direcciones MAC (Media Access Control), que son códigos hexadecimales únicos de 48 bits grabados de fábrica en cada tarjeta de red (NIC). 
- **Acceso al Medio**, define las reglas de quién puede transmitir y cuándo. En redes Ethernet antiguas compartidas se usaba un algoritmo llamado CSMA/CD (Acceso Múltiple por Detección de Portadora con Detección de Colisiones), que básicamente dictaba: "escucha el cable, si nadie habla envía; si chocas con otro, espera un tiempo aleatorio y reintenta". 
- **Detección de Errores**, en el tráiler de la trama se incluye un campo llamado FCS (Frame Chechk Sequence). Es un cálculo matemático (generalmente CRC). El equipo que envía hace el cálculo y lo anota. El que recibe hace el mismo cálculo con los bits que le llegaron; si el resultado no coincide, significa que el cable corrompió los datos y la trama se descarta inmediatamente. 

**PDU**
Trama

**Protocolos y Estándares**
- **Ethernet**, es un estándar de comunicación que define cómo se envían los datos mediante cables físicos. 
- **Wi-Fi**, el estándar para LAN inalámbrica. Usa CSMA/CA (evita colisiones en lugar de solo detectarlas, porque en el aire no se puede detectar colisiones tan fácilmente como en un cable de cobre).
- **STP (Spanning Tree Protocol)**, es un protocolo que evita bucles y tormentas de broadcast, impide que las tramas de red viajen en círculo de manera infinita entre los switches conectados redundantemente. Permite tener cables o caminos de respaldo físicos que se activan de forma automática si la ruta principal falla. 
- **VLANs**, redes de área local virtuales. Permite dividir un único switch físico en varios switches lógicos aislados.

**Dispositivos y Hardware**
- **Tarjetas de Interfaz de Red (NIC)**, las tarjetas de red integradas en computadoras, laptops o servidores. Son las dueñas de las direcciones MAC. 
- **Switch de Capa 2**, el switch tiene memoria y una CPU. Construye una base de datos interna llamada Tabla CAM o Tabla MAC. Cuando se conecta un equipo, el switch aprende qué dirección MAC está conectada a qué puerto específico. 

**¿Cómo funciona internamente la Capa 2: Capa Enlace de Datos?**
Cuando la capa de red (capa 3) termina de armar su paquete (que ya trae la IP de quién envió la información y la IP de destino), se lo entrega a la tarjeta de red (NIC). La NIC es la que "fabrica" la trama envolviendo ese paquete. Lo hace agregando campos muy específicos: 
- **Encabezado**, la NIC escribe al principio de lo bits la MAC de destino y luego la MAC de origen. Después, añade un campo llamado "EtherType" que dice "el paquete que llevo adentro es de tipo IPv4". 
- **Payload**, aquí va metida la información o paquete intacto que venía de la capa de red (capa 3).
- **Trailer (FCS)**, la NIC pasa todos los bits anteriores por una fórmula matemática y anota el resultado final.
El switch recibe esta trama eléctrica en el puerto. El microprocesador del switch lee únicamente la MAC de destino en el encabezado. Busca esa MAC en su Tabla CAM, descubre que está en tal puerto y envía la trama eléctricamente solo por ahí. El equipo receptor lee el trailer, hace la misma fórmula matemática; si el resultado cuadra, quita el encabezado y el trailer (desencapsula) y sube el paquete limpio a su propia capa de red. 

### Capa 3: Capa de Red
Esta capa se caracteriza por el concepto de "Enrutamiento y algoritmos".

Su función es el direccionamiento lógico global y la selección de la mejor ruta. 
- **¿Cómo encapsula?**, toma el "segmento" que le entrega la capa de transporte (capa 4) y le añade un encabezado IP. Este encabezado contiene, entre otras cosas: la IP Origen, la IP de Destino, y un campo crucial llamado TTL (Time to Live).
- **¿Cómo funciona el TTL?**, TTL es un límite que indica cuánto tiempo o cuántos saltos puede viajar un paquete de datos por una red antes de ser borrado. Su fin principal es evitar que los paquetes den vueltas sin fin cuando hay un error de ruta. 

**PDU**
Paquete 

**Protocolos**
- **IPv4 (Internet Protcol v4)**, direcciones lógicas de 32 bits. 
- **IPv6 (Internet Protocol v6)**, direcciones de 128 bits en formato hexadecimal. Soluciona la escasez de direcciones de IPv4 e incorporan seguridad nativa. 
- **ICMP (Internet Control Message Protocol**, no lleva datos de usuario; lleva mensajes de control de la red. Es un protocolo que los dispositivos utilizan para enviar mensajes de error e información operativa sobre la transmisión de datos. 
- **ARP (Address Resolution Protocol)**, es el puente entre la capa 3 y la capa 2. Es un protocolo de red fundamental que traduce una dirección IP en una dirección MAC dentro de una red local. Funciona de la siguiente manera: 
	- Revisión de caché, el equipo origen consulta su tabla ARP para ver si ya conoce la dirección MAC asociada a esa IP. Si la encuentra envía el dato de inmediato. 
	- Solicitud ARP, si no está en la tabla, el dispositivo emite un mensaje de tipo broadcast (difusión) a toda la red, preguntando quien tiene la IP tal que me envíe su dirección MAC.
	- Respuesta ARP, todos los equipos reciben la pregunta, pero solo el dispositivo que tiene la asignada esa IP responde con un mensaje directo (unicast) indicando yo tengo esa IP y mi dirección MAC es tal. 
	- Almacenamiento en caché, el equipo original guarda esta relación (IP y MAC) en su tabla ARP temporalmente para no tener que repetir el proceso. 

**Dispositivos y Hardware**
- **Routers (Enrutadores)**, mientras el switch tiene una tabla CAM (con MACs), el router tiene un Tabla de Enrutamiento (con redes IP y por qué puerto llegar a ellas). Cuando el router recibe una trama, le quita el encabezado de capa 2, analiza IP de destino del paquete de capa 3, consulta su mapa de rutas, determina el siguiente salto, le vuelve a poner un encabezado nuevo de capa 2, y lo envía. 
- **Switches Multicapa (capa 3)**, físicamente son switches, pero tienen un cerebro lógico capaz de leer IPs y hacer enrutamiento interno a la velocidad del hardware, sin depender de un router externo. 

**¿Cómo Funciona la Capa de Red (capa 3)?**
1. **Dirección de Salida**, la computadora tiene el dato empaquetado con una IP destino y la IP origen. El sistema operativo compara la IP de destino con su propia máscara de subred y dice: "esta no es mi red local, no puedo enviarla de forma directa al destino, debo enviársela a mi router (puerta de enlace) para que él la saque a internet o a otra red".
2. **Puente hacia la capa 2 (capa de enlace de datos)**, la computadora necesita armar la trama (para la capa 2) para que los bits viajen por el cable de red hacia el router. La PC conoce la IP del router, pero necesita saber su dirección MAC. Usa el protocolo ARP para preguntar en la red local la MAC del router y, al obtenerla, encapsula el paquete IP dentro de la Trama Ethernet y la envía. 
3. **Desencapsular y Enrutar (trabajo del router)**, el router recibe la trama eléctrica. Quita y destruye el encabezado de capa 2 porque ese encabezado local ya cumplió su función. Ahora el router tiene el paquete IP puro. 
4. **Tabla de Enrutamiento**, el router lee la IP de destino. Revisa su tabla de enrutamiento (su mapa interno). Encuentra una regla que dice "para ir a esa IP, debes enviar el paquete por la interfaz de fibra óptica que conecta con el proveedor de internet".
5. **Re-encapsulamiento**, el router no puede enviar el paquete IP desnudo por la fibra óptica. Vuelve a bajar a la capa 2. Crea una nueva trama con un nuevo encabezado (ahora la MAC de origen es la del router y la MAC de destino es la del equipo del proveedor de internet). Envía los bits. Este proceso de quitar capa 2, leer capa 3 y poner una nueva capa 2 se repite en cada router del mundo hasta llegar al servidor final destino. 

### Capa 4: Transporte 
Mientras que la capa de red (capa 3) se encarga de llevar el paquete de la computadora A a la computadora B, la capa 4 se asegura de entregarlo a la aplicación correcta dentro de esa computadora. Sus dos objetivos principales son la multiplexación (permitir que múltiples aplicaciones usen la red al mismo tiempo mediante puertos) y la segmentación (dividir archivos grandes en pedazos manejables para la red y rearmarlos en el destino).

La capa de red solo lleva datos de una máquina a otra, pero no sabe a qué aplicación entregarlos. La capa de transporte (capa 4) utiliza puertos (del o al 65,535) para dirigir el tráfico.
Las aplicaciones se quedan "escuchando" en un puerto específico. Cuando un usuario intenta conectarse a esa aplicación, la interacción se da bajo de la siguiente manera bajo el protocolo TCP: 
1. **3-Way Handshake (saludo de 3 vías)**, TCP es un protocolo orientado a la conexión. No envía ni un solo dato hasta no asegurar que el destino está vivo y listo.
	1. **SYN**, el usuario origen envía un segmento vacío con una bandera llamada SYN (sincronización). Significa: "hola quiero abrir una conexión contigo en el puerto 16, mi número de secuencia inicial será 100".
	2. **SYN-ACK**, el destino recibe el mensaje, acepta la conexión y responde con dos banderas: SYN y ACK (reconocimiento). Significa: "recibí tu SYN 100, lo confirmo (ACK 101). Yo ´también quiero también quiero sincronizarme contigo, mi número de secuencia es 500".
	3. **ACK**, el origen o usuario (el que inició la conexión) recibe la respuesta del destino y envía un último ACK. Significa: "confirmado tu SYN 500 (ACK 501). Estamos Listos"
2. **Transferencia**, aquí ya fluyen los datos. Si el destino envía un segmento u no recibe un ACK de confirmación en cierto tiempo, asume que se perdió en la red y lo retransmite automáticamente. 
3. **Cierre de conexión**, cuando se cierra la aplicación, se envían banderas FIN para cerrar formalmente el canal y liberar la memoria RAM de ambos equipos. 

**PDU**
Si se usa TCP = segmento
Si se usa UDP = datagrama

**¿Cómo Funciona la Capa de Transporte (capa 4)?**
1. **Multiplexación (asignación de puertos)**, la capa de transporte (capa 4) recibe los datos de la aplicación. Para la descarga de un archivo por ejemplo, asigna el puerto origen (el navegador de donde se descarga) y el puerto destino (el servidor web). Los puertos son como puertas dentro del edificio que es la IP.
2. **Segmentación**, el servidor web no puede enviar todo el archivo (que se quiere descargar) de golpe porque saturaría el cable y excede el tamaño máximo que soporta Ethernet (MTU, típicamente 1500 bytes). La capa de transporte (capa 4) del servidor "corta" ese archivo en miles de segmentos.
3. **Secuenciación (solo TCP)**, a cada uno de esos miles de segmentos, la capa de transporte (capa 4) le estampa un número de secuencia (ejemplo segmento 1, segmento 2, segmento 3, ...).
4. **Encapsulamiento hacia abajo**, la capa de transporte (capa 4) le entrega estos segmentos a la capa de red (capa 3) IP, que los convierte en paquetes y los envía por la red. 
5. **Rearmado en el destino**, los segmentos llega a la computadora. Pueden llegar desordenados porque tomaron distintas rutas en internet. La capa de transporte (capa 4) de la computadora lee los números de secuencia, los ordena matemáticamente, verifica que no falte ninguno y, ya ordenados, le entrega el archivo descargado completo y sin errores al navegador. 

**Protocolos**
- **TCP (Transmission Control Protocol)**, orientado a la conexión, garantiza la entrega en orden y sin errores (retransmite lo perdido). Es lento y pesado porque requiere el 3-Way Handshake y confirmaciones constantes. Se usa para páginas web (HTTP/HTTPS), descargas de archivos, correos y bases de datos. 
- **UDP (User Datagram Protocol)**, no orientado a la conexión. No hace 3-Way Handshake, no espera confirmaciones y no retransmite nada. Simplemente escupe los datagramas a la red lo más rápido posible. Es rápido y ligero. Se usa para transmisión de voz, videollamadas, streamming en vivo y movimiento rápido en videojuegos. 

**Hardware**
Los firewalls de inspección de estado operan aquí. Bloquean o permiten el tráfico basándose en los puertos. 

### Capa 5: Sesión
Esta capa actúa como el coordinador de diálogos de la red. Su objetivo principal es establecer, administrar, sincronizar y finalizar las conversaciones lógicas (sesiones) entre dos hosts. Mientras la capa 4 se asegura que los paquetes lleguen completos, en orden y a la aplicación correcta, la capa de sesión(capa 5) controla los tiempos de ese intercambio: quién habla, cuándo habla, por cuánto tiempo y qué sucede si la comunicación se corta de manera inesperada. Define si el diálogo será simplex, half-duplex o full-duplex a nivel de software (independiente del cable físico).

**PDU**
Datos (Data)
A partir de esta capa hacia arriba, la unidad de información deja de tener encabezados de segmentación o enrutamiento y se trata puramente como datos de software. 

**¿Cómo Funciona la Capa de Sesión (capa 5)?**
1. **Establecimiento del diálogo**, si se tienen múltiples aplicaciones abiertas, que estarán enviando y consumiendo información de la red, el sistema operativo solicita abrir canales de comunicación independientes. La capa de sesión (capa 5) recibe la orden y negocia los parámetros iniciales con los servidores de cada aplicación (por ejemplo, iniciaremos una sesión de audio).
2. **Sincronización**, durante la transmisión, la capa de sesión (capa 5) inserta marcadores o puntos de control en el flujo de datos. Si por ejemplo se descarga un archivo grande del servidor y el internet sufre un microcorte, la capa de sesión (capa 5) localiza el último marcador confirmado por ambos lados. 
3. **Recuperación**, al restablecerse la red, en lugar de solicitar el archivo desde el byte cero, la capa de sesión (capa 5) del sistema operativo le dice al servidor: "retomemos el diálogo exactamente desde el marcado que tenemos registrado". 
4. **Finalización**, cuando se cierra la aplicación, la capa de sesión (capa 5), interrumpe el diálogo lógicamente y le avisa al servidor remoto que destruya esa sesión específica para liberar memoria, sin afectar la sesión de otra aplicación. 

**Protocolos**
- **NetBIOS (Network Basic Input/Output System)**, permite que aplicaciones en computadoras distintas se comuniquen dentro de una red de área local. Funciona enviado mensajes de registro; cuando un nuevo dispositivo entra a la red, NetBIOS transmite un aviso porque se le asigna un nombre a ese dispositivo y para que no se repita avisa de inmediato, y así los otros equipos también tienen conocimiento sobre este equipo. 
- **RPC (Remote Procedure Call)**, permite a un programa ejecutar código en una máquina remota como si fuera local. Si estoy en mi PC y envío una consulta SQL a un servidor externo, RPC empaqueta los parámetros de la consulta, establece la sesión, hace que el servidor la procese y devuelve el resultado. 
- **PAP**, protocolo básico de control de acceso. Antes de permitir que la sesión de datos se abra completamente, PAP exige usuario y contraseña (enviados en texto plano) para validad que el host remoto tiene permiso para iniciar el diálogo. 

**Dispositivos y Hardware**
A diferencia de las capas inferiores, no existe como tal un switch de capa 5 o un cable específico. Esta capa es más de software: 
- **Sistemas Operativos**, las API (Interfaces de Programación de Aplicaciones) de Windows por ejemplo son las responsables de ejecutar estos comandos. 
- **Firewalls de Próxima Generación y Proxies**

### Capa 6: Presentación 
Esta capa es el "traductor universal" de la red. Su objetivo es garantizar que la información enviada por la capa de aplicación de un sistema pueda ser leída y comprendida por la capa de aplicación de otro, sin importar si usan arquitecturas o sistemas operativos diferentes. Se encarga de tres áreas fundamentales: 
1. **Codificación/Formateo**: traducir el abecedarios y los números a un estándar común. 
2. **Compresión**, reducir el tamaño de los datos para no saturar el ancho de banda. 
3. **Cifrado/Encriptación**, ocultar la información para que nadie en el medio físico pueda robarla. 

**PDU**
Datos (data)

**¿Cómo Funciona la Capa de Presentación (capa 6)?**
Imaginando que se hace una compra en línea ingresando el número de tarjeta en una página web: 
1. **Recepción de la aplicación**, la página web (la capa de aplicación, capa 7) recibe el número de la tarjeta y se lo entrega a la capa de presentación (capa 6) del navegador web. 
2. **Codificación**, el sistema operativo usa un formato de texto específico (como UTF-8). La capa de presentación (capa 6) toma esos caracteres y se asegura de que estén formateados en un estándar de red comprensible para el servidor remoto (que quizá usa una base de datos antigua). 
3. **Compresión**, si la página web envía imágenes del producto, la capa de presentación (capa 6) del servidor detecta que la imagen en crudo pesa 20 MB. Le aplica un algoritmo matemático (como JPEG o PNG) reduciendo el tamaño antes de enviar la imagen o dato. 
4. **Cifrado**, la capa de presentación (capa 6) del navegador toma el número de la tarjeta (que está en texto plano) y le aplica un método de cifrado. Convierte el texto plano a un bloque de caracteres incomprensibles. 
5. **Pase a sesión**, una vez que la información está traducida, comprimida y encriptada, la capa de presentación (capa 6) se la entrega a la capa de sesión (capa 5) para que negocie la apertura del canal y comience el viaje hacia el router. 

**Protocolos**
- **TLS y SSL**, son protocolos de seguridad que crean un canal cifrado entre un navegador web y un servidor para proteger los datos en internet. 
- **ASCII/EBCDIC/UTF-8**, son protocolos de codificación de caracteres. Asignan un valor binario específico a cada letra del abecedario. EBCDIC era usado por los grandes servidores (mainframes) de IBM, mientras que las PCs usaban ASCII. La capa de presentación (capa 6) interceptaba el texto de la PC y le cambiaba el mapa de bits para que el servidor IGM no imprimiera símbolos sin sentido. 
- **Formatos Multimedia (MPEG, GIF, JPEG, PNG)**, aunque se vean como extensiones de archivo, a nivel de red, dictan cómo el flujo de bits debe ser interpretado estructuralmente en la pantalla para formar píxeles de color o audio comprimido. 

### Capa 7: Capa de Aplicación 
Esta capa es la interfaz directa entre el usuario y la red. Su objetivo no es ser la aplicación de software en sí, sino proporcionar los servicios de red que esas aplicaciones necesitan para comunicarse con el exterior. En el modelo OSI, esta capa se divide lógicamente en dos subcapas:
1. **CASE**, elementos de servicio de aplicación común, que manejan funciones generales 
2. **SASE**, elementos de servicio de aplicación específica, que manejan protocolos particulares como correos o bases de datos. 

**PDU**
Datos (data)

**¿Cómo Funciona la Capa de Aplicación (capa 7)?**
Suponiendo que se quiere entrar al sitio web de la universidad. 
1. **Solicitud de resolución**, el navegador no sabe qué hacer con las letras del dominio, necesita una IP. La capa de aplicación (capa 7) invoca su primer protocolo interno (DNS) y envía una consulta a la red preguntando: "¿Cuál es la IP con este nombre?".
2. **Preparación del servicio final**, una vez que el DNS resuelve la IP correcta, la capa de aplicación (capa 7) sabe a dónde ir. Ahora invoca al protocolo HTTPS para estructurar una petición formal pidiendo la página principal del sitio web. 
3. **Descenso en la arquitectura**, esta solicitud HTTPS perfectamente estructurada como Datos se la entrega a la capa de presentación (capa 6), que la encriptará, luego bajará a la capa de sesión (capa 5) para abrir el diálogo, a la capa de transporte (capa 4) para asignarle el puerto 443, a la capa de red (capa 3) para ponerle la IP descubierta, a la capa enlace de datos (capa 2) para la MAC y finalmente al cable en la capa física (capa 1).
4. **Recepción**, cuando el servidor responde, la información sube de regreso hasta la capa de aplicación (capa 7), que toma el código HTML limpio y se lo entrega al navegador para que dibuje la página en la pantalla. 

**Protocolos**
- **DHCP (Dynamic Host Configuration Protocol)**, asigna direcciones IP automáticamente. El proceso es el siguiente: 
	- _Descubrir_, un dispositivo se enciende y no tiene IP. Grita a toda la red local no tengo IP, existe algún servidor DHCP aquí. 
	- _Oferta_, el servidor DHCP (generalmente el router) escucha y responde: yo soy el servidor DHCP  te ofrezco la IP 192.168.1.10.
	- _Petición_, el dispositivo responde: acepto esa IP, préstamela. 
	- _Reconocimiento_, el servidor confirma y registra a ese dispositivo con esa dirección IP.
- **DNS (Domain Name System)**, traduce nombres legibles por humanos a direcciones IP. Sin la capa de aplicación (capa 7) haciendo esta consulta silenciosa, tendríamos que memorizar secuencias numéricas para cada página web. 
- **HTTP/HTTPS**, protocolo de la World Wide Web. Funciona bajo un modelo de "Petición-Respuesta" (Request-Response). Un cliente pide un recurso y un servidor lo entrega junto con un código de estado. 
- **SMTP, FTP, P2P: SMTP**, se encarga de rutear y empujar los correos electrónicos hacia los servidores de destino. FTP permite la transferencia y gestión estructurada de archivos. P2P (Peer-to-Peer) permite a los clientes compartir recursos directamente entre ellos sin un servidor central. 