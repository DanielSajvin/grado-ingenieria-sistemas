## El Kernel
Un sistema operativo abarca tanto aplicaciones dentro de una computadora cómo los recursos que la computadora ofrece a esas aplicaciones. Entonces el Kernel es el que se encarga de administrar los recursos (el hardware de la computadora) y decide qué aplicación, cuándo y por cuánto tiempo tiene acceso a esos recursos. 

_Es la capa de software que actúa como puente absoluto entre las aplicaciones (software) y el procesamiento real de los datos (hardware)_

### Tipos de Kernel Principales
- **Monolítico**, todo el código del administrador (gestión de memoria, procesos, controladores de hardware) está compilado en un solo gran bloque en el espacio del Kernel. Es muy rápido, pero si un controlador de video falla, todo el sistema operativo se congela. Ejemplo: Linux 
- **Microkernel/Híbrido**, el núcleo se mantiene lo más pequeño posible, delegando muchas tareas (como los controladores de red o video) al espacio de usuario como si fueran servicios normales. Si un controlador falla, solo se reinicia ese servicio, no toda la máquina. Ejemplo: Windows NT (es el núcleo de Windows 11).

### Dual-Mode Operation 
Para que el sistema no colapse si una aplicación falla, los procesadores modernos dividen la memoria y la ejecución en dos modos: 
- **Modo Usuario**, aquí se ejecutan los programas normales. Tienen un acceso muy restringido. Si un programa aquí intenta leer la memoria de otro o acceder directamente al disco duro, el hardware lo bloquea. 
- **Modo Kernel**, aquí viven el kernel, tiene control total, absoluto y sin restricciones sobre todo el hardware de la computadora. 



<hr>

## Sistema Operativo 
**Perspectivas Top-Down (Máquina Extendida / Máquina Virtual)**, el SO es una capa de abstracción. El hardware desnudo (discos físicos, sectores, transistores) es complejo y propenso a errores de programación. El SO oculta esta complejidad y le presenta al usuario o programados una "máquina extendida" limpia y fácil de usar. Por ejemplo, en lugar de complicarse moviendo el brazo mecánico de un disco magnético, el SO permite la abstracción de "Archivos y Carpetas".

**Perspectiva Bottom-Up (Gestor de Recursos)**, el SO es el administrador o gestor de los recursos, ya que en un sistema moderno, múltiples programas compiten por la CPU, la RAM y el almacenamiento, entonces el SO es el que ordena el caos, esto lo hace multiplexando los recursos en el tiempo y en el espacio. 

_Multiplexación en el tiempo, la CPU le da ciertos milisegundos a un proceso y después le da tiempo a otro proceso, es decir, los procesos se van turnando los recursos en el tiempo_
_Multiplexación en el espacio, para que varios procesos se ejecuten al mismo tiempo, el SO debe dividir la memoria RAM, le asigna ciertos espacios o bloques a cada proceso, para que no se sobrescriban_
### Historia de los sistemas operativos 
1. **Primera Generación - Tubos al vacío (1945-1955)**, no existían los SO, el programador reservaba la máquina entera, introducía código binario mediante interruptores físicos o tarjetas perforadas y esperaba el resultado. Problema, el 90% del tiempo la máquina estaba inactiva esperando que el humano configurara los cables. 
2. **Segunda Generación - Transistores y Sistemas por Lotes (1955-1965)**, nace el primer acercamiento a un SO (como FMS o IBSYS). Para no desperdiciar el tiempo de la CPU, los trabajos (tarjetas perforadas) se agrupaban en lotes. El SO simplemente leía un trabajo de la cinta magnética, lo ejecutaba hasta terminar e inmediatamente cargaba el siguiente. Problema: si un programa pedía leer datos de una cinta, la CPU se quedaba sin hacer nada (ociosa) hasta que el lento dispositivo mecánico terminara. 
3. **Tercera Generación - Circuitos Integrados y Multiprogramación (1965-1980)**, la memoria se divide en particiones para cargar varios programas a la vez. Si el programa A necesita  esperar al disco duro, el SO le quita la CPU y se la da al programa B. Nace también el tiempo compartido, donde múltiples usuarios se conectan a un mainframe (computadora central, que funciona como un servidor de gran tamaño) mediante terminales, el SO le da a cada uno una fracción de segundos de CPU, creando la ilusión de que cada usuario tiene su propia computadora. En la tercerea generación nada UNIX, que sería como el abuelo de Linux.
4. **Cuarta Generación (1980-Presente)**, las computadoras se vuelven personales. Nacen las interfaces gráficas. El enfoque pasa de "aprovechar al máximo la CPU" a "hacer la vida mas fácil al usuario". Nacen los SO de red y los SO distribuidos. 
5. **Quinta Generación**, SO para computación en la Nube, virtualización mediante hipervisores y contenedores donde el SO se abstrae aún más del hardware físico e internet de las cosas (IoT) con sistemas operativos en tiempo real muy limitados en recursos. 

### Revisión de Hardware
El SO no necesita saber cómo tal la estructura física del hardware, pero si necesita conocer íntimamente los componentes lógicos del hardware para administrarlos. 

**El Procesador (CPU) y los Registros**
La CPU es el cerebro. La CPU funciona bajo un ciclo infinito: Buscar (Fetch), Decodificar (Decode) y Ejecutar (Execute) instrucciones. Para no tener que viajar hasta la memoria RAM por cada pequeño cálculo, la CPU cuenta con Registros. Los Registros son celdas de memoria que se encuentran operando a la misma velocidad que el procesador. Los más críticos para el SO son: 
1. **Program Counter (PC) - Contador de Programa**, este es el registro que contiene la dirección de memoria exacta de la siguiente instrucción que la CPU debe ejecutar. Si el SO quiere cambiar del Proceso A al Proceso B, lo que hace a nivel de hardware es alterar el valor del Program Counter para que apunte a la zona de memoria donde está el código del Proceso B.
2. **Stack Pointer (SP) - Puntero de Pila**, apunta a la cima de la pila de la memoria actual. Es vital porque cuando ocurre una interrupción o se llama a una función, el procesador usa la pila para "guardar dónde estaba" antes de saltar a hacer otra cosa. 
3. **Program Status Word (PSW) - Palabra de Estado del Programa**, es un registro que contiene los bits de control del procesador. Aquí se define si el resultado de la última operación matemática fue cero, si fue negativo y críticamente contiene el bit que indica si la CPU está en Modo Usuario o Modo Kernel. 

**La Jerarquía de Memoria**
el SO debe tener en cuenta que existen diferentes velocidades: 
	1. _Caché_, súper rápida, centro de la CPU
	2. RAM, rápida, pero volátil 
	3. Disco (HDD/SS), lento pero persistente. 

**Interrupciones**
Es el mecanismo más importante del hardware. Por ejemplo si el teclado recibe datos, no espera a que la CPU los atienda, por el contrario el teclado envía una señal eléctrica llamada interrupción. La CPU pausa lo que está haciendo, el SO toma el control (Modo Kernel), atiende la interrupción y luego devuelve el control al programa que se estaba ejecutando. 
1. **Interrupciones de Hardware (Asíncronas)**, se generan por dispositivos físicos en cualquier momento. Por ejemplo, si se trabaja con un teclado externo conectado a una laptop, el hardware del teclado envía una señal eléctrica a un chip llamado _Controlador de Interrupciones Avanzado (APIC)_ que se encuentra en el procesador de la laptop. 
2. **Excepciones o Traps (Síncronas)**, son generadas por la propia CPU al ejecutar una instrucción defectuosa o restringida. Por ejemplo, si un programa intenta dividir por cero, o si intenta acceder a un área de la memoria que no le pertenece, la CPU genera el Trap, detiene el programa y le avisa al SO para que mate al proceso.
3. **Interrupciones de Software (System Calls)**, son provocadas intencionalmente por un programa. Cuando un entorno virtualizado, como un busistema de Linux, necesita acceder al disco duro físico, ejecuta una instrucción especial (como syscall) que genera una interrupción de software, cambiando el bit del PSW a Modo Kernel. 

El flujo entonces de una interrupción es el siguiente: 
1. El hardware envía la señal
2. La CPU termina de ejecutar la instrucción actual (nunca se queda a medias)
3. La CPU toma el valor actual del Program Counter y del PSW y los guarda en la pila. Esto es tomar una "foto" del estado actual para no perder el proceso. 
4. La CPU busca en una tabla especial en memoria (vector de Interrupciones) la dirección del código del SO diseñado para manejar ese evento específico, y lo carga en el Program Counter. 

**Cómo Viajan los Datos**
_Los Buses (PCle)_, son las autopistas de datos. Una tarjeta gráfica dedicada, por ejemplo, no se comunica con la CPU a través de conexiones lentas, utiliza líneas de conexión directa de alta velocidad para mover texturas y cálculos gráficos masivos directamente a la memoria o al procesador. 

_Acceso Directo a Memoria (DMA)_, es un chip que funciona de la siguiente manera: si se quiere copiar un archivo de 5GB y si la CPU tuviera que leer y escribir cada byte de ese archivo mediante interrupciones, el sistema entero se congelaría. El controlador de disco tiene un chip DMA, entonces el SO le dice al chip que copie esos 5GB del disco a determinada dirección de la RAM y cuando termine esto que avise con una única interrupción, de esta manera la CPU queda libre y la transferencia se hace en segundo plano. 

### Clasificación de los SO
**Sistemas por Lotes**, procesan grandes cantidades de datos sin intervención del usuario. Por ejemplo, sistemas bancarios. 

**Sistemas Interactivos / de Tiempo Compartido**, los más comunes (Windows, Linux ). Su prioridad es el tiempo de respuesta para que el usuario sienta que el sistema es fluido y exclusivo para él.

**Sistemas de tiempo Real (RTOS)** no importa tanto hacer muchas cosas a la vez, sino cumplir con plazos de tiempo estrictos (deadlines). Si el SO frena un milisegundo de más, van a ocurrir demasiados problemas. Por ejemplo: el sistema de frenos ABS de un carro o el equipo de monitoreo de un respirador artificial. 

## Procesos y Árboles de Procesos 
**Proceso**
Un proceso no es un programa. Un programa es código muerto en el disco duro. Un proceso es un programa en ejecución. El proceso entonces consiste en su código, sus datos, su program counter, sus registros y su pila.
Un proceso es una entidad activa; es la instancia de un programa en ejecución. Mientras que un programa es una entidad pasiva, un archivo con código máquina en el disco.

**Process Control Block - Bloque de Control de Procesos (PCB)**, para el SO, un proceso no es más que una estructura de datos en lenguaje C llamado Bloque de Control de Procesos PCB. Cuando la CPU cambia de un proceso a otro, el SO guarda toda la información en el Bloque de Control de Procesos del proceso saliente y carga el PCB del proceso entrante. El PCB contiene lo siguiente: 
- Estado del Proceso (Listo, En Ejecución, Bloqueado)
- Valores de los registros de la CPU y el Program Counter
- Información de gestión de memoria (punteros a sus tablas de páginas)
- Información de contabilidad (cuánto tiempo de CPU ha usado)
- Lista de archivos abiertos por ese proceso

**Árboles de Procesos (Jerarquía)**, en sistemas UNIX/Linux, existe un único proceso raíz creado al arrancar la computadora (tradicionalmente init o systemd, con PID 1). Todos los demás procesos se crean a partir de este mediante la llamada al sistema _fork()_. Esto crea una estructura de árbol estricta. Si un proceso padre muere, el SO interviene: o mata a todos los proceso hijos en cascada, o el proceso raíz _init()_ "adopta" a los procesos huérfanos. 

**Aislamiento**, a nivel arquitectónico, el SO debe garantizar que un proceso no interfiera con otro. Si el Proceso A tiene un error fatal, solo el proceso A debe colapsar.

**El Costo de Rendimiento**, el asilamiento tiene un precio muy alto. Cambiar del Proceso A al Proceso B se llama _Cambio de Contexto_. Esto requiere que el SO detenga la CPU, guarde los registros en el PCB de A, busque el PCB de B, actualice las tablas de memoria y limpie la caché del procesador (TLB). Esto consume milisegundo de la CPU haciendo trabajos administrativos en vez de estar ejecutando código útil, es por esto que, se tiene que evaluar si conviene crear un proceso nuevo completo y aislado (pero lento de gestionar) o usar hilos, comparten memoria, menos aislados, pero más rápidos. 

**Jerarquía**, en sistemas como Linux, los procesos tienen jerarquía (padre e hijo). Si el proceso padre muere, los hijos quedan "huérfanos" (en este caso el SO decide si adoptarlos o matarlos). En Windows, todos los procesos son iguales, aunque el SO guarda un handle (identificador) del proceso que lo creó. 

### Espacios de Direcciones 
Un espacio de direcciones es el conjunto de direcciones lógicas que un proceso puede utilizar para direccionar la memoria. Es la abstracción que protege y aísla la memoria física (RAM).
_La Unidad de Manejo de Memoria (MMU)_, es un chip de hardware integrado en la CPU. Cuando el código dice "guarda esta variable en la dirección lógica 1000", esa dirección es falta (virtual). La MMU intercepta esa petición en nanosegundos y la traduce a la dirección física real en la RAM (por ejemplo, la dirección 85000).

Entonces si un proceso malicioso intenta pedirle a la CPU que lea una dirección de memoria que no le pertenece, la MMU detecta que 3está fuera de su "Espacio de direcciones" e inmediatamente lanza una interrupción síncrona (Trap). El SO toma el control y mata al proceso emitiendo un error de violación de segmento. 

#### Archivos y Direcciones 
El archivo es la unidad lógica abstracta creada por el SO para ocultar las propiedades mecánicas y eléctricas de los dispositivos de almacenamiento. 

**Inodos (Índices de Nodo)**, en sistemas UNIX/Linux, el disco no busca archivos por nombre. Cada archivo está presentado por una estructura de datos llamada Inodo,  que contiene los metadatos (quién es el dueño, permisos de lectura/escritura, tamaño y en qué bloques físico del disco están los datos reales). El "Directorio" Es simplemente un archivo especial que contiene una tabla vinculando nombres legibles por humanos con su número de inodo.

El SO utiliza la misma interfaz de programación (abrir, leer, escribir, cerrar) para todo. Si por ejemplo se quieren enviar datos por la red a otra computadora, se escribe en archivo abstracto llamado socket (funciona como un canal virtual de entrada y salida gestionado por el núcleo o Kernel).

## Llamadas al Sistema
Si el modo usuario está restringido, ¿Cómo hace un programa para guardar un archivo?
Lo hace a través de una _System Call_. El programa pausa su ejecución, le "pide permiso" al Kernel (cambiando temporalmente a modo Kernel), el Kernel ejecuta la acción de forma segura en el hardware y luego devuelve el control al programa en Modo Usuario.

#### Cómo funciona por ejemplo WSL dentro de Windows 
WSL es básicamente una distro de Linux por ejemplo dentro de Windows. 
En arquitecturas modernas por ejemplo Windows 11, ejecuta un Kernel de Linux real y completo a través de una tecnología de virtualización nativa llamada _Hyper-V (hipervisor)_ 

**¿Cómo se comunican?**, cuando se ejecuta un comando en Ubuntu, el Kernel de Linux real procesa la solicitud. Pero como Windows es el anfitrión, el hipervisor se "sienta" debajo de ambos Kernels. El Kernel de Linux solicita el acceso al disco, y el hipervisor arbitra esa solicitud con el sistema físico o anfitrión.

**Gestión de la GPU**, si un entorno gráfico en Windows y un proceso de desarrollo en Ubuntu necesitan la tarjeta de video al mismo tiempo, la arquitectura utiliza una tecnología llamada GPU Para Virtualización (GPU-PV). El Kernel de Windows y sus controladores retienen la autoridad física, mientras que el Kernel de Linux se comunica con una "GPU Virtual" proyectada por Windows. Windows pone en cola y procesa ambas peticiones secuencialmente a nivel de hardware, evitando la condición de carrera. 

## Estructura 

### Arquitectura Monolítica 
Básicamente es un SO que decide meter absolutamente todo (la gestión de memoria, la planificación de procesos, los controladores de la tarjeta de video, el sistema de archivos del disco dura y los protocolos de red) dentro de un único archivo binario gigante, compilado todo junto. 
Ese archivo gigante se carga en la memoria RAM y se ejecuta enteramente en el Modo Kernel. 

**¿Cómo se comunican las partes?**, como todo está dentro del mismo programa, si el gestor de archivos necesita hablar con el controlador del disco duro, simplemente hace una llamada a una función normal de lenguaje C. Es una comunicación directa, inmediata y sin intermediarios. 
La ventaja es que al estar todo en el mismo espacio de memoria privilegiado, es muy rápido. No hay cambios de contesto ni saltos entre el Modo Usuario y el Modo Kernel dentro de las operaciones internas del sistema. Linux utiliza una arquitectura monolítica, porque está enfocado para el rendimiento máximo en servidores. 

La desventaja es que como todo está en el mismo espacio de memoria en Modo Kernel, si hay un solo error en un componente menor, todo el SO colapsa al instante. No puede aislar el fallo. Es el famoso Kernel Panic en Linux o la Pantalla Azul en Windows. 

Es un módulo grande que contiene todo en el mismo espacio de memoria, y la comunicación es de forma directa, cómo si estuviera llamando a un función en en mi mismo código.
### Arquitectura de Micronúcleo (Microkernel)
La filosofía aquí es la reducción extrema. El núcleo (que corre en Modo Kernel) se hace lo más pequeño posible. Solo se conserva lo absolutamente esencial para que el hardware funcione: gestión básica de memoria, planificación básica de hilos y el mecanismo para que los procesos se comuniquen entre sí (IPC - Inter Process Comunication).

**¿Dónde va todo lo demás?**, todo lo demás (el sistema de archivos, el controlador de red, interfaz gráfica) se saca del Kernel y se ejecuta como procesos normales en el espacio de usuario. A estos procesos se les llama Servidores.
Y si un controlador falla, simplemente muere ese proceso en modo usuario. El micronúcleo lo detecta, reinicia ese proceso únicamente en milisegundos, y el resto del sistema ni se entera. Es seguro y estable. 

El mero núcleo o kernel se queda solo con lo más importante, lo demás lo manda afuera de su dominio, es decir, módulos en modo usuario separados; la comunicación es por ejemplo el modulo A quiere algo del módulo B, entonces el módulo A le pasa el mensaje al kernel -> el kernel recibe el mensaje y se lo pasa al módulo B -> el módulo B recibe y responde al kernel <- el kernel toma la respuesta y se la devuelve al módulo A.

### Arquitectura Híbrida 
El SO mantiene la organización limpia de micronúcleo (separado en módulos independientes para tener aislamiento), pero el kernel agranda su frontera de memoria y mete todos esos archivos ahí dentro. 
Básicamente se divide todo como en micronúcleo, pero ahora en vez de separarlo en direcciones de memoria diferente, el kenel reserva mas espacio de memoria para poder meter todos estos módulos dentro de su mismo espacio o rango de memoria, entonces esto resulta en una comunicación directa entre módulos como en la arquitectura monolítica. 
La ventaja de esta arquitectura es en cómo se administra, ya que si quiero cambiar un módulo lo puedo hacer porque está separado en módulos, cosa que en monolítica no se podía porque todo estaba junto entonces tocaba cambiar todo. 
También importante es qué no todo los controladores o todo el módulo en sí están en modo kernel, si no que solo una parte y la mas pesada está en modo usuario. 

#### Software Libre
Es un movimiento filosófico y ético fundado por Richard Stallman en los años 80 con la _Free Software Fundation (FSF)_. La palabra clave es Libertad, no que es gratis. Para que un software sea formalmente Libre, debe garantizar irrevocablemente 4 libertades: 
- Libertad 0: ejecutar el programa como se desee, con cualquier propósito (incluso comercial o militar)
- Libertad 1: estudiar cómo funciona el programa y cambiarlo para que haga lo que el usuario quiera. Esto requiere obligatoriamente tener acceso al código fuente
- Libertad 2: redistribuir copias para ayudar a otros
- Libertad 3: distribuir copias de sus versiones modificadas a terceros, permitiendo que toda la comunidad se beneficie. 

#### Código Abierto (Open Source)
Es un movimiento paralelo fundado a finales de los 90. La diferencia es filosófica, el software libre es un movimiento que defiende que el software privativo es "inmoral". El código abierto está enfocado en la colaboración, es decir, se enfoca más en los beneficios prácticos, técnicos y de colaboración de desarrollo; porque se tiene a miles de personas ayudando mejorar el código o implementando cosas funcionales. 

#### Licencias
Todo programa en Linux está regido por derechos de autor (Copyright). La licencias son contratos legales que dictan cómo puedes usar ese código. Esta es la razón por la que distribuciones como Ubuntu pueden ser descargadas, modificadas y utilizadas sin pagar regalías, mientras que con otros SO hay que pagar costosas licencias. Se dividen en dos grandes familias restrictivas y permisivas: 
1. **Licencias Copyleft o Virales (GPL - General Public License)**, fueron creadas por el movimiento de software libre. El kernel de Linux (y casi todo el proyecto GNU) usa GPLv2. La regla, si tomo un código con licencia GPL, lo modifico o lo agrego dentro de otro programa, ahora ese programa pasa directamente a heredar la licencia GPL. Entonces quedo obligado a liberar y regalar todo mi código fuente al público. 
2. **Licencias Permisivas (MIT, Apache, BSD)**, son las favoritas del mundo corporativo. La regla es, haz lo que quieras. Puedes tomar el código, modificarlo, cerrarlo, compilarlo y venderlo por millones de dólares sin mostrarle el código fuente a nadie. La única condición legal es que dejes una nota pequeña dando crédito al autor original. 

