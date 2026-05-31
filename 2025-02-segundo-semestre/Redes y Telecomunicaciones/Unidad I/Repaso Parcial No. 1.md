
---

**Internet**, (internetwork) es la red de redes más grande del mundo. Es pública y abierta, cualquiera puede acceder siempre que tenga conexión

**Intranet**, es una red privada interna de una organización, que utiliza las mismas tecnologías de internet (páginas web, correo, servidores), pero está limitada solo a usuarios autorizados 

**Red de área local (LAN - Local Area Network)**, es una red de computadoras limitada a un área pequeña, como una casa, una oficina, un laboratorio o un edificio. Ejemplo, Ethernet y WiFi

**Extranet**, es como una extensión de la intranet, pero que permite el acceso controlado a usuarios externos (clientes, proveedores, socios).  Ejemplo, un banco tiene una extranet para que los clientes consulten sus cuentas

**Red de Área Personal (PAN)**, conecta dispositivos en un área muy limitada, como un hogar o una oficina pequeña. Ejemplo: bluetooth y wifi direct

**Red de Área Metropolitana (MAN)**, conecta dispositivos dentro de una ciudad o un área metropolitana. Utiliza tecnologías como fibra óptica o cable

**Red de Área Amplia (WAN)**, conecta dispositivos en áreas geográficas extensas, incluso a través de continentes. Incluyen internet y utilizan tecnologías como líneas telefónicas, satélites y fibra óptica

**¿Cómo se transmiten los datos?**
Cada dispositivo de entrada (mouse, teclado) traduce la interacción humana al código binario para que la CPU la procese y guarde. Cada dispositivo de salida (impresora, monitores) toma los datos binarios y los traduce nuevamente a la forma humana. En ASCII cada carácter está respresentado por 8 bits
	_Se utilizan tres método comunes para transmitir señales en las redes_
	- Señales eléctricas, la transmisión se realiza representando los datos como pulsos eléctricos que viajan por un cable de cobre
	- Señales ópticas, la transmisión se realiza convirtiendo las señales eléctricas en pulsos de luz
	- Señales inalámbricas, la transmisión se realiza por medio de ondas infrarrojas, de microondas o de radio por el aire. 

**Ancho de banda**, es la capacidad de un medio para transportar datos. Es la cantidad máxima de datos que pueden transmitirse a través de una red o conexión en un tiempo determinado. Se mide normalmente en bits por segundo (bps).
- Miles de bits por segundo - Kbps
- Millones de bits por segundo - Mbps
- Miles de millones de bits por segundo - Gbps

**¿Qué es el cable UTP?**, Unshielded Twisted Pair, par trenzado sin apantallar. Cable compuesto por 4 pares trenzados, usado en la mayoría de redes Ethernet LAN
![[Pasted image 20250820225427.png]]


**Tipos de cables según uso**
- Cable directo (Straight-through), conecta dispositivos distintos (Switch-PC, Router-PC)
- Cable cruzado (Crossover), conecta dispositivos iguales (PC-PC, Switch-Switch)

**Cable certificado**, fabricado bajo estándares de calidad reconocidos, cumple con normas de rendimiento 

**Cableado estructurado**
Sistema estandarizado de cables, conectores y dispositivos que soporta múltiples servicios (voz, datos, videos)
- Evita enredos y desorden 
- Facilita el mantenimiento
- Es escalable

- **Componentes del cableado estructurado**
	- Rack, estructura metálica donde se montan los equipos 
	- Patch Panel, organiza los cables que vienen de los puntos de red
	- Switch, conecta los dispositivos 
	- Cables UTP, STP, Cat5e, Cat6, Car6A
- **Normas y topologías**
	- TIA/EIA 568, estándar de cableado 
	- Topología estrella, cada punto de red se conecta al switch 
	- Distancias máximas, 100 metros 

## Protocolos de comunicación 
Los protocolos son necesarios para que las computadoras se comuniquen correctamente a través de la red. 

**Características de los protocolos**
- Formato del mensaje, los formatos del mensaje dependen del tipo de mensaje y del canal que se utilice para entregar el mensaje 
- Tamaño del mensaje, un mensaje largo puede dividirse en parte más pequeñas para ser entregado correctamente 
- Sincronización, determina la velocidad a la que se transmiten los bits a través de la red. 
- Codificación, el host emisor primero convierte en bits los mensajes envidados, cada bit se codifica en un patrón de sonidos, ondas de luz o impulsos electrónicos
- Encapsulamiento, es el proceso de agregar encabezado con información del host de origen y de destino. 
- Patrón del mensaje, algunos mensajes requieren confirmación de recepción para poder enviar el siguiente mensaje. 

**Estándar**, es un conjunto de reglas que determina cómo se realiza algo. 

## Modelo TPC/IP

![[Pasted image 20250819155542.png]]

Es un conjunto de protocolos que permiten que los dispositivos en internet y en redes privadas se comuniquen entre sí. 
- **TCP (Transmision Control Protocol)**, se encarga de garantizar la entrega confiable de los datos. Divide los mensajes en segmentos, los envía y asegura que lleguen completos y en orden
- **IP (Internet Protocol)**, se encarga de direccionar y encaminar los paquetes a través de la red hasta llegar al destino correcto
	- _IP dice a dónde  va el paquete_
	- _TCP asegura que llegue bien y en orden_
#### Capas del modelo TCP/IP
1. Capa de acceso a red
	1. Se ocupa de la entrega física de los datos a través de cables, WiFi, fibra óptica, entre otros. Ejemplo: Ethernet en cable, WiFi en inalámbrico
2. Capa de internet 
	1. Define la dirección de origen y destino y decide la ruta que toman los paquetes 
	2. Protcolos: IP(IPv4, IPv6), ICMP, ARP
3. Capa de transporte 
	1. Gestiona la comunicación entre aplicaciones 
	2. TCP, confiable. Se usa en correo o web porque no puede faltar información
	3. UDP, rápido pero no confiable. Se usa en streamming o juegos online porque se prefiere rapidez a exactitud 
4. Capa de aplicación
	1. Aquí se están los programas que usamos para comunicarnos, navegador web, correo electrónico, videollamadas 

---
Hay dos tipos básicos de modelos para describir las funciones que deben estar presentes para que las comunicaciones de red sean exitosas: _modelos de protocolo_ y _modelos de referencia_

**Modelo de Protocolo**, el modelo TCP/IP es un modelo de protocolos porque describe las funciones que ocurren en cada capa de protocolos. 

**Modelo de referencia**, describe las funciones que se deben completar en una capa en particular, pero no especifica exactamente cómo se debe realizar una función. El objetivo principal es ayudar a comprender mejor las funciones y los procesos necesarios para las comunicaciones de red. 

---

### Modelo de referencia OSI

![[Pasted image 20250819222059.png]]

Open Systems Interconnection, es un modelo teórico creado por la ISO para entender y estandarizar cómo se comunican los sistemas en red. No es un protocolo como TCP/IP, si no un marco de referencia 
#### Capas del modelo OSI
1. Capa física 
	1. Se encarga de la transmisión de bits (0 y 1) a través del medio físico (cable, fibra, ondas). Ejemplo, voltajes, conectores, cables UTP, WiFi, fibra óptica 
2. Capa de enlace de datos
	1. Organiza los bits en tramas y detecta/corrige errores de transmisión. Ejemplos, trajetas de red, switches, protocolos Ethernet, dirección MAC
3. Capa de Red
	1. Determina la ruta que toman los paquetes y gestiona las direcciones lógicas (IP). Ejemplos, routers, protocolo IP
4. Capa de transporte
	1. Asegura le entrega confiable y en orden de los datos (o rápida sin control en el caso de UDP)
5. Capa de sesión 
	1. Administra las sesiones de comunicación entre las aplicaciones (abre, mantiene y cierra la sesión). Ejemplo, al iniciar sesión en una videollamada, esta capa mantiene la conexión establecida 
6. Capa de presentación 
	1. Traduce, comprime y encripta los datos para que la aplicación los entienda
7. Capa de aplicación 
	1. Es la más cercana al usuario; aquí viven las aplicaciones y servicios de red



---

**VPN (Virtual Private Network)**, Red Privada Virtual, es un túnel seguro que se crea desde internet para conectar un dispositivo o una red con otra de forma privada y protegida

**IEEE (Institute of Electrical and Electronics Engineers)**, Organización profesional más grande del mundo dedicada al avance de la tecnología en beneficio de la humanidad
- Establece estándares técnicos que usamos todos los días 

**Host**, también llamado equipo terminal, es cualquier dispositivo que origina y/o consume datos en la red. El host es como el usuario de la red. Ejemplos: computadoras, laptops, smartphones, servidores web, bases de datos. Host puede referirse a dispositivos finales 

---


### Dirección IP
IP (Internet Protocol Address) es una dirección lógica y única dentro de una red que identifica a cada dispositivo para poder comunicarse. 
#### Formatos de IP
- IPv4
	- Usa 32 bits, lo que permite 4,294,967,296 direcciones únicas 
	- Se escribe en formato decimal con 4 números
	- Cada número (octeto, 8 bits) va de 0 a 255
	- Cada bloque es un octeto 8 * 4 = 32
- IPv6
	- Usa 128 bits, una cantidad prácticamente infinitas de direcciones 
	- Se escribe en hexadecimal separado por dos puntos 
	- Cada 4 bits está representado por un solo dígito hexadecimal 

#### IP Pública
- Es la dirección con que mi red se identifica en internet 
- La asigna el proveedor de internet, es decir, el ISP
- Única en todo el mundo 
#### IP Privada 
- Se usa dentro de redes locales (LAN)
- No son únicas globalmente 

**_Cómo se conectan las IP privadas a internet_**, esto es gracias a NAT (Network Address Translation), el router traduce las IP privadas a la IP pública para salir a internet 

**_¿Qué es una trama?_**
Es la unidad de datos en la capa de enlace de datos. Está formada por:
- Cabecera (header), contiene información de control (direcciones MAC de origen y destino)
- Datos (payload), la información real que viaja 
- Cola (trailer), usada para verificar que la trama no tenga errores 
Cuando se envía un archivo por la red, este se divide en paquetes, y luego cada paquete se "envuelve" en tramas para poder ser enviado físicamente por un cable o por WiFi

**_Dirección MAC_**
Media Access Control, es la dirección física y única que tiene cada tarjeta de red (NIC)
Se usa en rede locales (LAN), para que los switches identifiquen qué dispositivo está en qué puerto
Tiene un formato de 48 bits, normalmente escrito en hexadecimal 




|     |     |     |     |     |
| --- | --- | --- | --- | --- |
  
||1993|1994|1995|1er. Trimestre 1996|
|Ventas|$ 2,921,000.00|$ 3,477,000.00|$ 4,519,000.00|$              1,062,000.00|
|Utilidad Neta|$       60,000.00|$       68,000.00|$       77,000.00|$                      5,000.00|
|Patrimonio Neto|$     504,000.00|$     372,000.00|$     449,000.00|$                  454,000.00|
|Total Activo|$     919,000.00|$ 1,157,000.00|$ 1,637,000.00|$              1,627,000.00|
|Utilidad Bruta (margen bruto)|$     719,000.00|$     843,000.00|$ 1,095,000.00|$                  263,000.00|

|   |   |   |   |   |
|---|---|---|---|---|
  
||1993|1994|1995|1er. Trimestre 1996|
|Ventas|$ 2,921,000.00|$ 3,477,000.00|$ 4,519,000.00|$              1,062,000.00|
|Utilidad Neta|$       60,000.00|$       68,000.00|$       77,000.00|$                      5,000.00|
|Patrimonio Neto|$     504,000.00|$     372,000.00|$     449,000.00|$                  454,000.00|
|Total Activo|$     919,000.00|$ 1,157,000.00|$ 1,637,000.00|$              1,627,000.00|
|Utilidad Bruta (margen bruto)|$     719,000.00|$     843,000.00|$ 1,095,000.00|$                  263,000.00|
