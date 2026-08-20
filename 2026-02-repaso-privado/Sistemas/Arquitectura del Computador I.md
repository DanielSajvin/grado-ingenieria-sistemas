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