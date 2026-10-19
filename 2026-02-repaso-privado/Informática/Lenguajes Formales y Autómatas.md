
Los lenguajes formales se construyen de manera ascendente mediante una jerarquía algebraica: Símbolos -> palabras -> lenguaje.

**Símbolo o Carácter o Letra**, entidad abstracta básica e indivisible. Ejemplo: 0, 1, a , b. 
**Alfabeto**, conjunto finito, no vacío de símbolos. Ejemplo: Alfabeto Binario = {0, 1}. Un alfabeto no puede ser infinito ni vacío por definición.
**Palabra o Cadena**, es una secuencia finita y ordenadas de símbolos de un alfabeto, también llamado cadena. 

**Longitud de una Cadena**, número total de posiciones de símbolos que la conforman. 

## Lenguaje (L) - formal
Es un conjunto de cadenas o palabras formadas a partir de un alfabeto específico, de acuerdo con reglas gramaticales o de construcción definidas. Características principales: 
- **Sintaxis, no semántica**, se enfoca únicamente en la estructura y en cómo se combinan los símbolos, sin importar el significado que se le quiera dar a dichas cadenas. 
- **Sin ambigüedad natural**, a diferencia de los lenguajes humanos (que dependen del contexto o la interpretación), _un lenguaje formal_ es completamente preciso y predecible. 
- **Relación con los autómatas**, las gramáticas sirve para generar las palabras del lenguaje, mientras que los autómatas (como los autómatas finitos o las máquinas de Turing) sirven para _reconocer o validar_ si una palabra pertenece a dicho lenguaje. 
Un lenguaje entonces es básicamente un conjunto o subconjuntos de cadenas que se forman de otro conjunto que es el alfabeto, por lo tanto al ser un lenguaje formal un conjunto también se pueden aplicar las operaciones de conjuntos a estos. 

### Jerarquía de Chomsky
Los lenguajes formales se pueden clasificar en 4 niveles, según su complejidad. Y para cada tipo de lenguaje existe un tipo exacto de autómata capaz de reconocerlo. A mayor complejidad del lenguaje, más memoria y capacidad necesita el autómata. 

| Tipo de Lenguaje      | Gramática/Descripción                                     | Autómata que lo reconoce                                            | Ejemplos de Aplicación                                                   |
| --------------------- | --------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Regulares             | Estructuras muy simples, patrones repetitivos             | Autómata Finito (AFD o AFND)                                        | Validar un correo electrónico o un número de teléfono                    |
| Libres de Contexto    | Estructuras anidadas o emparejadas                        | Autómata de Pila (memoria tipo LIFO)                                | Verificar que los paréntesis de un código estén bien abiertos y cerrados |
| Sensibles al Contexto | El significado/regla depende de los símbolos de alrededor | Autómata Linealmente Acotado (memoria limitada al tamaño del texto) | Análisis sintáctico avanzado de lenguajes naturales                      |
| Sin Restricciones     | Cualquier lenguaje que pueda ser computado                | Máquina de Turing (memoria infinita en cinta)                       | Un lenguaje de programación completo (Python, C++, Java)                 |

### Autómata
Es un modelo matemática abstracto que procesa cadenas de símbolos y decide si pertenecen o no a un lenguaje formal. Actúa como una máquina teórica con un conjunto de estados y un conjunto de reglas que le indican cómo cambiar de estado según la información que vaya leyendo. 

_Es una máquina de estados que se encarga de procesar inputs, es decir, tiene una entrada la procesa y genera una salida; la salida que genera es la aceptación o no de la palabra o cadena_

**Autómata Finito Determinista - AFD**
Se compone de los siguientes elementos: 
- **Q**, conjunto de estados del autómata, es decir, las posibles situaciones que se pueden dar cuando el autómata procese la cadena. 
- **Σ**, alfabeto del autómata, todos los símbolos o caracteres con los que el autómata puede trabajar. 
- **δ**, recoge todas las transiciones entre estados del autómata. 
- **q0**, es el estado inicial del autómata. Es la flecha que indica el inicio o por qué estado debe iniciar el autómata. 
- **F**, subconjunto de Q, contiene todos los estados finales. Es decir, todos los estados en dónde si el autómata termina entonces la cadena se acepta, se llama estados finales o estados de aceptación.

Un autómata es finito y determinista cuando _para cada estado, existe una transición por símbolo como máximo_, de modo que no existe la ambigüedad 

**Autómata Finito No Determinista - AFND**
Se compone de los siguientes elementos: 
- **Q**, conjunto de estados del autómata, es decir, las posibles situaciones que se pueden dar cuando el autómata procese la cadena. 
- **Σ**, alfabeto del autómata, todos los símbolos o caracteres con los que el autómata puede trabajar. 
- **δ**, recoge todas las transiciones entre estados del autómata. 
- **q0**, es el estado inicial del autómata. Es la flecha que indica el inicio o por qué estado debe iniciar el autómata. 
- **F**, subconjunto de Q, contiene todos los estados finales. Es decir, todos los estados en dónde si el autómata termina entonces la cadena se acepta, se llama estados finales o estados de aceptación. 

La diferencia ente un AFD y entre un AFND es qué _desde un estado puede haber una transición por cada símbolo como máximo_. Ahora para un AFND _desde un estado puede haber varias transiciones definidas para cada símbolo_. 

![503](../recursos/Pasted%20image%2020261018130017.png)

![507](../recursos/Pasted%20image%2020261018130326.png)

#### Aplicaciones de los Autómatas hoy en Día

**Compiladores e Intérpretes de Programación**
Cada vez que se ejecuta una línea de código en Python, Java, entre otros y se ejecuta, el lenguaje pasa por un proceso de traducción. Los autómatas trabajan aquí en dos etapas críticas: 
- **Análisis Léxico (Autómata Finito)**, separan el código en palabras clave (if, while, var). Si se escribe una palabra reservada mal, entonces el autómata finito rechaza esa palabra o cadena inmediatamente, porque determina que esa cadena no pertenece al lenguaje. 
- **Análisis Sintáctico (Autómata con Pila)**, revisan que la estructura sea correcta. Por ejemplo, verifican que cada llave de apertura tenga llave de cierre correspondiente, sin importar cuántas líneas de código haya en medio. 

**Procesamiento de Texto y Motores de Búsqueda**
Las _Expresiones Regulares_ (RegEx), que se usan en cualquier lenguaje de programación para buscar, reemplazar o validar texto (como verificar que un string tenga formato de correo electrónico o contraseña segura), se transforman internamente en un _Autómata Finito_ para poder ejecutarse a velocidades ultrarrápidas. 

