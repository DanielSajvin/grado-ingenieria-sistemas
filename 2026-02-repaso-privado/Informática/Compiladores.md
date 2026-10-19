Un compilador es un programa que traduce un programa escrito en un lenguaje de programación de partida (lenguaje fuente) a un programa equivalente en otro lenguaje (lenguaje destino u objeto), preservando estrictamente el significado semántico original y reportando errores presentes en el código fuente. 
_Un compilador es un programa que convierte código fuente de alto nivel en código destino de bajo nivel, mientras se mantiene la funcionalidad del programa._

## Estructura de un Compilador
### Front-End (Fase de Análisis)
- **Responsabilidad**, comprender el código fuente, verificar su validez estructural/semántica y construir una representación interna. 
- **Dependencia**, depende únicamente del lenguaje fuente y es totalmente independiente de la arquitectura del procesador destino. 
- **Componentes**, analizador léxico, analizador sintáctico, analizador semántico y generador de código intermedio. 

### Back-End (Fase de Síntesis)
- **Responsabilidad**, tomar la representación intermedia generada por el Front-End y traducirla a código ejecutable eficiente para la máquina de destino. 
- **Dependencia**, depende únicamente de la arquitectura de la máquina objetivo (registros, conjunto de instrucciones, memoria de la CPU) y es independiente del lenguaje fuente. 
- **Componentes**, optimizador de código (dependiente de máquina) y generador de código objeto/ensamblador. 

### Modelos de Ejecución y Traducción 
- **Compilador Tradicional**, traduce todo el código fuente a código máquina nativo antes de la ejecución (ejemplo: C, C++, Rust, Go). Produce binarios rápidos y optimizados para la plataforma, pero carece de portabilidad directa del binario. 
	- **_Portabilidad_**, _es la capacidad de un programa de ejecutarse en diferentes plataformas (distintos sistemas operativos, arquitecturas de CPU o entornos), con el mínimo esfuerzo o modificaciones en su código fuente._
- **Intérprete Puro**, lee, analiza y ejecuta la sentencia fuente directamente instrucción por instrucción en tiempo de ejecución, sin generar un binario independiente (ejemplo: versiones clásicas de PHP o Bash). Facilita la depuración e introspección, pero es sensiblemente más lento. No genera un archivo ejecutable independiente ni código máquina por adelantado. Toma el código fuente y lo ejecuta directamente instrucción por instrucción. 
- **Compilador Just-In-Time (JIT) - Justo a Tiempo**, el código fuente se compila previamente a un código de bytes o bytecode intermedio (independiente de la plataforma). En tiempo de ejecución, la máquina virtual (JVM en Java, CLR en .NET, V8 en JavaScript) interpreta el bytecode y compila dinámicamente a código máquina nativo las secciones que se ejecutan con alta frecuencia (hot spots). Es un modelo híbrido diseñado para obtener lo mejor de ambos mundos: la portabilidad de un intérprete y la velocidad de un compilador tradicional. 
- **Transpilador**, traduce el código de un lenguaje de alto nivel a otro lenguaje de nivel similar (ejemplo: TypeScript a JavaScript, Babel, Cilk a C).

### Fases del Proceso de Compilación 
1. Secuencia de caracteres (código fuente)
2. **Análisis Léxico**, scanner: produce Tokens
3. **Análisis Sintáctico**, parser: construye el árbol sintáctico 
4. **Análisis Semántico**, decora árbol, valida tipos y ámbitos 
5. **Generación de Código Intermedio**, genera código de 3 direcciones / cuádruplos 
6. **Optimización de Código**, elimina redundancias, propaga constantes 
7. **Generación de Código Objeto**, mapea a instrucciones y registros de la máquina 
8. Código Máquina / Ensamblador 
- **Tabla de Símbolos**, estructura de datos (típicamente tablas hash encadenadas o jerárquicas) que persiste información sobre cada identificador: nombre, tipo de dato, ámbito (scope - alcance), tamaño en memoria, desplazamiento (offset - compensar) y dirección base. 
- **Manejador de Errores**, captura y reporta anomalías en cada fase sin detener abruptamente el proceso, aplicando estrategias de recuperación (modo pánico, recuperación a nivel de frase o producciones de error).

**Ejemplo de que sucede en cada fase**

Entrada inicial: _Código Fuente_
``` posicion = inicial + velocidad x 60 ```

_Análisis Léxico (Scanner)_
Lee la secuencia de caracteres crudos y descarta espacios en blanco. Produce la secuencia tuplas token: 
```<id, 1> <assign, = > <id, 2> <op_add, + > <id, 3> <op_mult, x > <num_int, 60>```

_Análisis Sintáctico (Parser)_
Agrupa los tokens según las reglas gramaticales jerárquicas del lenguaje (respetando que la multiplicación tiene mayor precedencia que la suma) y genera el Árbol de Sintaxis Abstracta (AST).
```
        =
       / \
     id1   +
          / \
        id2   *
             / \
           id3  60
```

_Análisis Semántico_
Verifica que los operandos sean compatibles con los operadores. Al detectar que ```id3``` es de tipo ```float``` y ```60``` es ```int```, inserta un nodo de coerción o conversión de tipos explícita (```inttofloat```):
```
        =
       / \
     id1   +
          / \
        id2   *
             / \
           id3  inttofloat
                    |
                    60
```

_Generación de Código Intermedio_
Transforma el árbol de sintaxis abstracta decorado en una secuencia lineal donde cada instrucción tiene como máximo un operador y dos operandos (código de tres direcciones - TAC):
```
t1 = inttofloat(60)
t2 = id3 x t1
t3 = id2 + t2
id1 = t3
```

_Optimización de Código_
Aplica técnicas para reducir el tiempo de ejecución y el uso de memoria. En este caso, si la conversión se puede calcular en tiempo de compilación. 

_Generación de Código Objeto_
Asigna registros físicos y emite las instrucciones de máquina o ensamblador correspondientes. 

### Maneras de Escribir una Operación Matemática o Lógica
**Notación Infija**
Forma estándar que usamos los seres humanos para escribir expresiones aritméticas y lógicas, en la cual el operador se coloca entre los dos operandos. 
``` (A+B)xC```

**Notación Prefija**
Es conocida como la notación polaca, es una forma de escribir expresiones matemáticas, lógicas o algebraicas en la que el operador se coloca antes de los operandos. 
```x+ABC```

**Notación Postfija**
Se le conoce también como notación polaca inversa o RPN por sus siglas en inglés. Es un método para escribir expresiones matemáticas y lógicas en el que el operador se coloca después de sus operandos. No se necesitan paréntesis ni reglas complejas de precedencia para saber qué operación va primero. Se lee de izquierda a derecha.
```AB+Cx```

La notación postfija elimina por completo la ambigüedad sintáctica y la necesidad de usar paréntesis o reglas de precedencia para evaluar la expresión. Un compilador o una máquina virtual evalúa expresiones postfijas de forma directa utilizando una Pila: 
1. Si el elemento evaluado es un operando, se ejecuta ```PUSH(operando)```.
2. Si el elemento evaluado es un operador binario, se extraen los dos últimos operandos con ```POP()```, se aplica la operación, y el resultado intermedio se reinserta con ```PUSH(resulado)```.

### Consideraciones para la construcción de lenguajes de programación
- Legibilidad y Expresividad 
- Ortogonalidad, 
- Costo Global, incluye el costo de escribir programas, el tiempo de compilación, el tiempo de ejecución, el despliegue del entorno y el costo de mantenimiento. 
- **Sistemas de Tipos**
	- **Tipado Estático vs Tipado Dinámico**, en el tipado estático (C, C++, Java), los tipos de datos se verifican durante la compilación. En el dinámico (Python, JavaScript), las variables están ligadas a referencias y los tipos se resuelven y validan durante la ejecución. 
	- **Tipado Fuerte vs Tipado Débil**, un lenguaje fuertemente tipado previene operaciones no permitidas entre tipos incompatibles sin una conversión explícita. Un lenguaje débilmente tipado (como C o JavaScript) realiza conversiones o reinterpretaciones arbitrarias de memoria en tiempo de ejecución. 

## Aclaraciones 
**Patrón**
es la regla formal (descrita con una expresión regular). Ejemplo: "un dígito del 0 al 10 repetido una o más veces". 

**Lexema**
Es la secuencia concreta de caracteres en el código fuente que coincidió con el patrón. Ejemplo: "1024", "total", "+".

**Token**
Es la unidad lógica abstracta (un par compuesto por un nombre de token y un valor de atributo opcional). Es la etiqueta que el analizador léxico le entrega al analizador sintáctico. El analizador sintáctico no quiere saber si la variable se llama "edad" o "contador"; al analizador sintáctico solo le importa saber: "aquí viene un ID".
_Es la categoría abstracta que el analizador sintáctico entiende_
- Ejemplo de token: <NUMERO, 1024>, <OP_SUMA, +>

**Aclaración**
El análisis léxico elimina espacios en blanco y comentarios, esto es solo una tarea secundaria de limpieza. Pero la función principal del análisis léxico es convertir una secuencia plana de caracteres (flujo de bytes sin significado) en una secuencia de unidades con significado léxico (Tokens), reconociendo las palabras del vocabulario del lenguaje. 

#### Idea conceptual de cada fase

**Análisis Léxico**
Lee caracteres crudos del archivo. Produce secuencia de tokens. Y _su tarea principal es reconocer el vocabulario o palabras válidas_. Detecta los siguientes errores: 
- Caracteres inválidos 
- Cadenas no cerradas (un string sin comillas)
- Números mal formados (12.34.43)

**Análisis Sintáctico**
Lee las secuencias de Tokens que vienen del análisis léxico. Produce un árbol sintáctico. Y _su tarea principal es verificar la gramática, orden y jerarquía_. Detecta los siguientes errores: 
- Estructuras gramaticales incorrectas (ejemplo: a + * b)
- Paréntesis, llaves o corchetes desbalanceados 
- Falta de delimitadores (falta de ";" o ":")
- Estructuras incompletas (ejemplo: if () {})

**Análisis Semántico**
Lee el árbol sintáctico generado en el análisis sintáctico. Produce otro árbol sintáctico decorado o validado. _Su tarea principal es verificar la coherencia lógica y tipos de datos_. 
- Incompatibilidad de tipos (ejemplo: int x = "texto")
- Variables o funciones no declaradas 
- Variables redeclaradas en el mismo ámbito
- Llamada a función con número o tipo erróneo de argumentos. 
- Uso de break fuera de un bucle. 

**Generador de Código Intermedio**
Lee el árbol sintáctico decorado o validado. Produce código de 3 direcciones. Su tarea principal es generar código abstracto, independiente del hardware. 
- No detecta errores del programador, si el código llego hasta esta parte el programa fuente es semánticamente válido. Solo detecta fallos internos. 

**Optimizador de Código**
Lee el código intermedio. Produce código intermedio optimizado. Su tarea principal es hacer que el código sea más rápido y ligero. 
- No busca errores; busca ineficiencias: 
	- Código muerto (código que nunca se ejecuta)
	- Expresiones redundantes o constantes evaluables. 

**Generador de Código Objeto**
Lee el código intermedio optimizado. Produce lenguaje ensamblador o lenguaje máquina (.asm, .obj, .exe). Su tarea principal es asignar registros de la CPU y emite instrucciones. 
- Errores de recursos del sistema destino: 
	- Desbordamiento de memoria/registros de hardware
	- Instrucciones no soportada por el procesador meta. 

