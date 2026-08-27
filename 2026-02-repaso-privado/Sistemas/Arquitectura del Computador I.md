**Señales**
En la arquitectura de computadoras, una señal es una magnitud física (típicamente voltaje o corriente) que varían en el tiempo y se utiliza para transmitir información. 
- _Señales Analógicas_, es una onda eléctrica continua que cambia de valor de forma suave y sin saltos en el tiempo. Representa datos físicos del mundo real como la temperatura, la voz o la presión mediante voltajes variables. Sus características son: 
	- Continuas, toman una cantidad infinita de valores posibles en un rango
	- Variables, su fuerza o voltaje sube y baja de manera fluida
	- Frágiles, son fáciles de dañar por el ruido o interferencia eléctrica externa. 
- _Señales Digitales_, son pulsos eléctricos que representan información mediante valores discretos (o bien definidos), usando un sistema binario de dos estados: 0 (apagado o voltaje bajo) y 1 (encendido o voltaje alto). Permiten que el procesador, la memoria y los componentes se comuniquen y ejecuten operaciones lógicas. Básicamente son fotos de la onda de la señal analógica, se establece un rango y se está observando en que parte cae la onda eléctrica de la señal analógica en el momento de la foto (muestra) y ya dependiendo del rango se clasifica y se interpreta como 1 o 0. 
- _Señal de Reloj_, es una señal estrictamente digital que no transporta datos, sino que genera un pulso constante y repetitivo para sincronizar a todos los componentes del sistema. Es un pulso constante que sincroniza todas las operaciones de la CPU y los buses. Cada ciclo de reloj dicta el ritmo al que se ejecutan las micro operaciones. 

![](../recursos/Pasted%20image%2020260820121310.png)

**Estados Lógicos**
Los estados lógicos son la abstracción matemática de las señales digitales. En la arquitectura clásica basada en lógica binaria, tenemos dos estados: 0 (Falso/Bajo) y 1 (Verdadero/Alto). Sin embargo, el hardware no es perfecto. Un 1 no es mágicamente un voltaje exacto, sino un rango de voltaje. 
- _Lógica TTL (Transistor-Transistor Logic)_, tradicionalmente, de 0V a 0.8V se lee como un 0 lógico. De 2.0V a 5.0V se lee como un 1 lógico. 
- _Región Prohibida_, el espacio entre 0.8V y 2.0V es indefinido (se puede descartar cómo interferencia). Si el voltaje cae allí, el procesador no sabe si es 0 o 1 y esto causa errores. 

## Sistemas de Numeración 
A nivel físico, la máquina solo entiende binario (base 2), pero se utilizan también otros sistemas para comprimir la información y hacerla legible. El hardware del procesador y la memoria solo entienden binario (señales de 0V y 5V). No hay forma física de que una computadora almacene un 2 o una letra A. Todo se traduce a interruptores encendidos o apagados. Sin embargo, escribir un montón de 1s y 0s es ilegible. Entonces entran los sistemas octal y hexadecimal, son lenguajes puente entre la máquina (binario) y el humano (decimal). 
- Octal (base 8), agrupa los bits de 3 en 3. 
- Hexadecimal (base 16), agrupa los bits de 4 en 4 (un nibble, la mitad de un byte). Es el estándar en arquitectura porque dos dígitos hexadecimales representan exactamente 1 byte (8 bits). Por eso cualquier dirección de memoria o dirección de red se muestra en hexadecimal: permite ver exactamente qué está pasando en los bytes físicos del equipo con muy pocos caracteres. 

### Codificación
La codificación es el acuerdo o estándar que define cómo interpretar un conjunto de bits. Un 01000001 (65 en decimal) es solo un número binario, pero dependiendo de la codificación, significa cosas distintas: 
- **ASCII / UTF-8**, si es texto, ese 65 representa la letra A mayúscula.
- **Entero sin signo**, representa el número 65 tal cual
- **Complemento a 2**, es el sistema de codificación más importante para representar números negativos en binario. Permite que el hardware use el mismo circuito sumador lógico (ALU) para hacer tanto sumas como restas, invirtiendo los bits y sumando 1. 

#### Lenguaje Máquina vs Lenguaje de Alto Nivel 
En la arquitectura de computadoras, existe una jerarquía de abstracción entre el programador y el procesador. 
- **Lenguajes de Alto Nivel (Python, C++, Java)**, permiten pensar en lógica, estructuras de datos y variables sin preocuparse por cómo se maneja la memoria física o qué registros del procesador se están usando. Están diseñados para la mente humana. 
- **Lenguaje Ensamblador (Bajo Nivel)**, es una representación legible por humanos del código máquina. Una mnemónicos (como MOV, ADD, SUB) para dar instrucciones directas a la CPU. Depende completamente de la arquitectura (el ensamblador de x86 es distinto al de ARM). 
- **Lenguaje Máquina**, es el nivel más bajo. Son putos unos y ceros (binarios). Es lo único que la Unidad de Control del procesador puede decodificar y ejecutar físicamente. 

Para que el hardware entienda un lenguaje de alto nivel, el código debe traducirse. Esto se hace principalmente de dos formas: mediante un Compilador (traduce todo el código a lenguaje máquina de una sola vez antes de ejecutarlo) o mediante un intérprete (traduce y ejecuta línea por línea entiempo real).

#### Historia del Desarrollo del Microprocesador 
1. **Tubos al Vacío (1940 -  1956 / 1a. Generación)**: máquinas gigantes, consumían mucha energía y generaban mucho calor. 
2. **Transistores (2da. Generación)**: el reemplazo físico del tubo de vacío. Más pequeños, rápidos, baratos y eficientes. Es la base de la computación moderna. 
3. **Circuitos Integrados (3ra. Generación)**: miles de transistores empaquetados en un solo chip de silicio. 
4. **Microprocesadores (4ta. Generación a la actualidad)**: toda la Unidad Central de Procesamiento (CPU) contenida en un único circuito integrado. La Ley de Moore ha dictado este desarrollo histórico, estableciendo empíricamente que la cantidad de transistores en un microprocesador se duplica aproximadamente cada dos años, reduciendo sus tamaño y aumentando la potencia. 

## Arquitectura del Computador 
La arquitectura define cómo interactúan el hardware y el software, y se divide clásicamente en el modelo de Von Neumann: una unidad de procesamiento, memoria y periféricos de entrada/salida. 

### Circuitos Combinacionales 
Su salida depende únicamente y exclusivamente de las entradas actuales. Por ejemplo una comporta lógica, AND, si entran dos 1, sale un 1. No tienen memoria; olvidan todo en el momento que la señal cambia. La Unidad Aritmética Lógica (ALU) está hecha de estos circuitos. 
![295](../recursos/Pasted%20image%2020260825162602.png)

### Circuitos Secuenciales
Su salida depende de las entradas actuales y del estado anterior. Tienen retroalimentación. La salida del circuito vuelve a conectarse a la entrada. Esto crea la memoria. Un circuito secuencial requiere una señal de reloj para sincronizar cuándo debe leer las entradas y cuándo debe cambiar su estado. 

### Latches 
Un Latch es el circuito secuencial más básico que existe para almacenar un único bit de información (0 o 1). 
El más famoso es el Latch SR (Set/Reset), construido típicamente cruzando dos compuertas NOR o NAND. 
- _Funcionamiento Técnico:_ tiene dos entradas. La entrada S (Set) la salida a 1. La entrada R (Reset) fuerza la salida a 0. 
- Si ambas entradas (S y R) se ponen en 0, el Latch mantiene el último valor que tenía en su salida. Es decir, la compuerta se queda "enclavada" reteniendo ese bit de información de forma infinita (mientras haya energía eléctrica). 

**De Latches a Flip-Flops y Registros**
El problema de un Latch puro es que es asíncrono (es decir, se ejecuta de forma independiente, sin esperar a que otra tarea previa termine antes de continuar); cambia su valor en el instante en que cambian sus entradas. En un procesador que opera a miles de millones de ciclos por segundo (GHz), esto causaría muchos problemas de sincronización. Para solucionarlo, el Latch se le agrega la señal de reloj. Cuando un Latch se le sincroniza con el reloj, evoluciona y se le llama Flip-Flop. Si pones 32 Flip-Flops en paralelo, acabas de construir un Registro de 32 bits dentro del procesador. 

### CPU (Unidad Central de Procesamiento)
Con los circuitos anteriores construimos el cerebro de la computadora. La CPU coordina y ejecuta las instrucciones, y se divide clásicamente en: 
- **Unidad de Control (CU)**, no procesa datos, sino que lee las instrucciones en lenguaje máquina de la memoria, las decodifica y envía las señales de control al resto de los componentes para que actúen. 
- **Camino de Datos (Datapath)**, contiene la ALU (Unidad Aritmética Lógica, que hace las operaciones matemáticas con circuitos combinacionales) y los Registros (hechos de circuitos secuencias / Flip-Flops que almacenan los datos temporalmente a máxima velocidad). 

### Memoria 
A nivel de arquitectura, la memoria es un arreglo masivo de circuitos que almacenan bits.
- **RAM (Memoria de Acceso Aleatorio)**, es el espacio de trabajo activo del procesador. El procesador es rápido, pero no tiene la capacidad para guardar programas enteros. El almacenamiento (SSD) tiene mucha capacidad, pero es muy lento. La RAM es el puente. Cuando se abre un programa, SO copia los datos del SSD hacia la RAM. El procesador solo ejecuta instrucciones y lee datos que ya están cargados en la RAM. 

- **DRAM Dynamic RAM (Memoria Dinámica de Acceso Aleatorio)**, construida con un transistor y un pequeño capacitor por cada bit. El capacitor se descarga (pierde la memoria), por lo que necesita un controlador que "refresque" eléctricamente miles de veces por segundo. Es más lenta que la SRAM, pero mucho más barata y densa. Se usa para la Memoria RAM principal. La DRAM es la tecnología con la que se construyen los módulos de RAM; su función es ser esa gran mesa de trabajo donde están cargados el SO, variables y el código de los programas abiertos, 
- **SRAM Static RAM (Memoria Estática de Acceso Aleatorio)**, construida con Flip-Flops (es decir, transistores). Es extremadamente rápida pero muy costosa y ocupa mucho espacio físico en el chip. Se usa para las Memorias Caché y los Registros. Es la tecnología con que se construye la Memoria Caché que está dentro del procesador. 

Todo esto interactúa con el procesador de la siguiente manera: 
1. La CPU necesita un dato. Primero lo busca en su Caché L1. Si está ahí, lo procesa instantáneamente. 
2. Si no está, busca en la Caché L2 o L3 (SRAM más lenta pero con más capacidad).
3. Si el dato no está en ninguna Caché, entonces la CPU se ve obligada a salir por e bus hacia la RAM. 
4. El controlador de memoria toma un bloque completo de datos de la RAM y lo copia a la caché, asumiendo que si la CPU pidió una variable, probablemente pedirá las variables vecinas en los siguientes milisegundos. 

### Entrada / Salida 
Son las interfaces que permiten a la CPU comunicarse con el mundo exterior (discos duros, tarjetas de red, periféricos). Dado que la CPU es millones de veces más rápida que un disco duro o una red local, no se comunican directamente a nivel de hardware. Se utilizan controladores de E/S y mecanismos como el DMA (Acceso Directo a Memoria) y las interrupciones para evitar que la CPU se quede congelada esperando a que un dato llegue. 

**DMA Direct Memory Access (Acceso Directo a Memoria)**, el DMA es un chip controlador independiente (un sub-procesador especializado) ubicado en la motherboard. Y su interacción con la CPU y la RAM es la siguiente: 
- _Delegación_, cuando el programa necesita cargar un archivo de 2GB del SSD a la RAM, la CPU no lo copia. La CPU manda una única instrucción al chip DMA.
- _Procesamiento libre_, la CPU se desconecta de la trasferencia y vuelve a hacer otras cosas.
- _Transferencia_, el chip DMA toma el control de los buses y transfiere directamente los datos del Disco hacia la RAM sin pasar por la CPU.
- _Interrupción_, cuando el DMA termina de copiar todos los datos o archivos, le envía una señal eléctrica especial a la CPU llamada Interrupción. 

## Arquitectura del Procesador

<hr>

## Repaso 

Para entender cualquier sistema computacional, desde un pequeño PIC hasta un procesador multinúcleo, se tiene que entender que todo se reduce a mover y transformar datos. 

La arquitectura básica dicta que se necesitan tres cosas: CPU para procesar, Memoria para almacenar instrucciones y datos y unidades de Entrada/Salida. Pero el secreto de la arquitectura no está en la piezas, sino en cómo se comunican. A esa vía de comunicación le llamamos Buses. Existen tres tipos de buses físicos: 
1. **Bus de Dato**, transporta la información real. 
2. **Bus de Direcciones**, indica dónde está esa información en la memoria. 
3. **Bus de Control**, envía las señales de lectura, escritura, reloj e interrupciones. 

### Arquitectura de Von Neumann
En este diseño las instrucciones del programa y los datos comparten la misma memoria física y los mismos buses. 
![361](../recursos/Pasted%20image%2020260827120754.png) 
El problema de esta arquitectura (Cuello de Botella) es que como el bus es compartido, el procesador (que es más rápido) pasa la mayor parte del tiempo de ciclo de reloj inactivo, esperando a que la memoria (que es más lenta) le entregue las instrucciones o los datos. Se forma un "embotellamiento". 

### Arquitectura Harvard 
Para solucionar el cuello de botella, Harvard separa físicamente la memoria de datos y la memoria de instrucciones, dotando a cada una de sus proprios buses independientes. Y funciona de la siguiente manera: el CPU puede estar leyendo la siguiente instrucción del programa en el bus de instrucciones, exactamente al mismo tiempo que está leyendo o guardando una variable en el bus de datos. La ventaja es que es mucho más rápido y eficiente por cada ciclo de reloj, pero el diseño del motherboard y del chip de silicio se vuelve complejo y costos porque necesita el doble de pistas de cobre (buses) y pines en el procesador. 

![571](../recursos/Pasted%20image%2020260827121527.png)

