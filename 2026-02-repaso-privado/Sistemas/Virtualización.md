La virtualización es una capa de abstracción lógica que desacopla los recursos físicos de hardware (CPU, memoria, almacenamiento y adaptadores de red) de los sistemas operativos y aplicaciones que los utilizan, permitiendo crear múltiples entornos de ejecución aislados e independientes sobre una misma plataforma física. 

![](../recursos/Pasted%20image%2020261014155214.png)

**Host/Anfitrión**
Es el equipo físico real (el hardware) y el entorno principal que presta sus recursos computacionales para que la virtualización sea posible. 

**Invitado**
Es el sistema operativo o máquina virtual que "vive" dentro del anfitrión y consume esos recursos. También se le puede conocer como _entorno virtualizado_. 

## Hipervisor
Es un software que permite crear, administrar y ejecutar múltiples máquinas virtuales en un único servidor o equipo físico. El hipervisor actúa como un intermediario entre el hardware físico y los sistemas operativos invitados, distribuyendo recursos como la CPU, la memoria RAM, el almacenamiento y la red de forma eficiente y aislada. 

### Tipos de Hipervisores

#### **Hipervisor de Tipo 1 - Bare-Metal**
Se ejecuta directamente sobre el hardware físico del servidor o  computadora anfitrión, sin necesidad de un sistema operativo intermedio. Ofrece el máximo rendimiento, estabilidad y seguridad, por esto es el estándar en entornos empresariales y centros de datos. 
Ejemplos: VMware ESXi, Microsoft Hyper-V. 

Otra manera de verlo es, el hipervisor de tipo 1 bare-metal es en sí el sistema operativo.
- En una computadora normal: `Hardware` -> `BIOS` ->  `Windows/Linux`  ->  `Tus programas`.
- En un servidor Bare-Metal: `Hardware` ->  `BIOS` ->  `Hipervisor` ->  `Máquinas Virtuales`.

Características importantes: 
- Elimina el retraso porque habla directamente con la CPU, la memoria y las tarjetas de red. 
- **Seguridad y Aislamiento**, como no tiene un sistema operativo base tiene una superficie de ataque muy pequeña. Y si se logra comprometer una máquina virtual, primero no afecta a las demás y mucho menos se puede llegar al centro. 
- **Consumo mínimo de Recursos**, el hipervisor en sí mismos es muy ligero. 

Se utiliza en centros de datos, bancos, nube (AWS, Azure) y servidores empresariales. 

#### **Hipervisor de Tipo 2 - Alojado/Hosteado**
Se instala como una aplicación o programa sobre un sistema operativo convencional (como Windows, macOS o Linux). Es más fácil de configurar para pruebas o usuarios particulares, pero tiene un rendimiento menor debido a que depende del sistema operativo anfitrión. 
Ejemplos: VirtualBox, VMware Workstation. 

Este tipo de hipervisor está diseñado para la comodidad, el desarrollo, las pruebas y el uso personal, algunas características importantes son: 
- **Dependencia del Sistema Anfitrión**, si por ejemplo Windows se traba, todas las máquinas virtuales también van a presentar ese fallo. 
- **Mayor consumo de recursos**, el rendimiento se ve penalizado porque la computadora debe mantener encendido el sistema operativo principal más el hipervisor y más la máquina virtual. 

## Tipos de Virtualización
#### Virtualización de Hardware/Servidores 
Resuelve el desperdicio de CPU y memoria en servidores físicos individuales. Lo que hace es tomar los núcleos del procesador físico y los bloques de memoria RAM física y los reparte en procesadores virtuales (vCPU) y memoria virtual para cada máquina virtual. 
- Máquina Virtual 

#### Virtualización de Almacenamiento 
Tradicionalmente, cada servidor tenía sus propios discos duros. Si el servidor A se quedaba sin espacio, se tenía que apagar y meterle más disco, mientras que el servidor B tenía 5 Tb libres. Además, si el servidor A se quemaba, la información se quedaba en sus discos. 
Entonces se decidió desacoplar el almacenamiento de los servidores. Se toman varios discos (se forma una cabina de almacenamiento o red SAN/NAS) y mediante software, se unen todos esos discos físicos en un solo gran disco de almacenamiento. 

#### Virtualización de Redes
En una red física, si se quería aislar el departamento A del departamento B por seguridad, se tenía que comprar swtiches físicos separados, tirar cables de red y reconfigurar puertos físicamente. Entonces la solución fue crear la red mediante software dentro de los propios servidores. Componentes principales: 
- **Switch Virtual**, un programa dentro del hipervisor que se comporta exactamente igual que un switch de red. Las máquinas virtuales "conectan" sus cables de red virtuales a este switch virtual para hablar entre sí a velocidades de memoria RAM. 
- **VLANs**, permiten que por un solo cable físico viajen datos datos de varios departamentos de una empresa totalmente separados por una etiqueta lógica de modo que no puedan verse entre sí a menos que un router lo permita. 
- **SDN (Redes Definidas por Software)**, permite configurar routers, firewalls y balanceadores mediante comandos y código, sin tener que ir a conectar cables físicamente al rack. 

#### Virtualización a Nivel de Sistema Operativo (Contenedores/Docker)
Una máquina virtual virtualiza el hardware completo. Cada máquina virtual tiene su propio sistema operativo, su propio kernel, sus propios controladores y sus propios archivos base.  

Un **contenedor** NO virtualiza el hardware ni instala un sistema operativo nuevo. Comparte el mismo kernel del sistema operativo del host. Lo único que aísla son los archivos del programa, sus librerías y sus procesos. 

### ¿En qué factores se debe basar uno para elegir tener un servidor físico o un servidor virtualizado?
Los factores para saber si decidir entre un servidor virtualizado o un servidor físico son: 

**Nivel de Utilización**
_Servidor Virtualizado_
Se elige cuando la carga de trabajo no va a consumir el 100% de la capacidad de un servidor físico moderno. Porque entonces se estaría desaprovechado el servidor físico. 

Lo que pasa es que por seguridad y estabilidad se recomienda que por cada aplicación servicio que se tenga se tiene que comprar un servidor físico, porque si entra un virus o esa app o servicio presenta un fallo o es vulnerado solo afectará a eso únicamente, entonces por eso se recomienda un servidor físico por cada app; lo que genera tener un servidor físico por app es que se termina desperdiciando y termina siendo un gasto absurdo, porque solo usaría como máximo un 20% del potencial de ese servidor físico moderno. Entonces si se tienen varias apps no muy grandes es mejor un servidor virtualizado. 
Ejemplos de apps y servicios que serían mejor tenerlos virtualizados: 
- Aplicaciones internas de la empresa (intranet)
- Páginas web, ya sean corporativas, informativas o tipo blogs. 
- Sistemas de control de asistencias, horas de llegada de los empleados, días que van o no van. 

_Servidor Físico_
Se elige solo si la aplicación es demasiado grande que por sí sola va a consumir todos los núcleos de CPU del servidor físico las 24 horas del día. Si una sola aplicación va a exprimir todo el potencial del hardware físico, entonces es mejor elegir un servidor físico. 
Entonces se debe elegir un servidor físico para aplicaciones que generan un uso masivo y constante de hardware, esto porque procesan volúmenes demasiado grandes de datos en tiempo real, atienden miles o millones de usuarios simultáneamente, y esto porque lo que se busca es evitar la pérdida de rendimiento que causa el tener un hipervisor. Ejemplos de aplicaciones se recomiendan tener en un servidor físico: 
- Sistemas bancarios y financieros 
- Sistemas ERP a gran escala (SAP o Oracle)
- Plataformas de streaming en vivo
- Servidores de videojuegos multijugador masivos. 
- Entrenamiento de modelos de inteligencia artificial 

**Rendimiento**
Si se requieren aplicaciones con un nivel muy bajo de latencia o lag se tiene que elegir un **servidor físico**, por ejemplo transacciones financieras o servidores que procesan señales de video y audio en tiempo real. Si un pequeño lag no se nota o no es tan importante entonces se puede elegir un servidor **virtualizado en la nube**.

**Respaldo y Continuidad del Negocio**
Tanto como para generar respaldos como snapshots o backups se pueden dejar programados de forma automática en un **servidor virtual en la nube**, y estos se pueden realizar en caliente, como también el restaurar una máquina virtual dañada se puede hacer casi instantáneo y sin que se note que el el sistema está caído o que hubo una interrupción. Por otro lado un **servidor físico** cualquier daño que exista o cualquier cambio que se quiera hacer en el hardware se tiene que interrumpir por completo la app o servicio y apagar completamente el servidor y se podrá restaurar la app o servicio hasta que se haga el mantenimiento o se arregle el problema. 

