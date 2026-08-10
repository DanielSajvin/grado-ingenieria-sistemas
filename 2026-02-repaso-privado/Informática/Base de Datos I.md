<hr>

## Fundamento: Dato vs Información
**Dato**, es un hecho aislado, es decir, por sí solo no tiene contexto o significado. Puede ser un nombre, o un número al azar. 
**Información**, son datos organizados y procesados dentro de un contexto dónde cada dato ya tiene un significado y puede ayudar a tomar una decisión. 

### Datos Primitivos o Básicos
Representan un valor indivisible.
Numéricos:
- Enteros (int)
- Decimales exactos (decimal)
- De punto flotante (float)
Alfanuméricos: 
- Cadena de caracteres (char)
- Cadena de caracteres de longitud variable (varchar)
Booleanos:
- Verdadero o False (bool o tinyint(1))
Fechas y Horas:
- Date
- Time
- DATETIME
- TIMESTAMP

### Datos Complejos o No Primitivos
Son estructuras más complejas, a veces compuestas de múltiples datos primitivos.
- BLOB (Binary Large Object), se usa para guardar archivos binarios puros directamente en la base de datos. Por ejemplo, archivo instalador de algún programa (.exe)
- ENUM, una lista predefinida de valores permitidos. Por ejemplo: Estado_civil ENUM(Soltero, Casado)
- JSON/XML, documentos complejos en formato JSON

## Base de Datos (DB) vs Sistema Gestor de Bases de Datos (DBMS)
**Base de Datos**, es una colección de datos organizados e interrelacionados entre ellos mismos. Dicho de otra forma, son los archivos que contienen toda la información. 
**Sistema Gestor de Bases de Datos**, es el software o conjunto de programas que me permite definir, manipular, recuperar y administrar los datos de forma segura. Por ejemplo: MySQL, Oracle, SQL Server.

## Arquitectura de 3 Niveles (ANSI/SPARC)
**Nivel Interno (Físico)**, es el nivel más bajo. En este nivel se describe cómo se guardan físicamente los datos en el disco duro, los bloques de memoria, los índices y las rutas de acceso. 
**Nivel Conceptual (Lógico)**, es el nivel intermedio. Describe qué datos se almacenan en la base de datos y qué relaciones existen entre ellos (tablas, llaves primarias, tipos de datos). Aquí es donde trabaja el diseñador de la base de datos. 
**Nivel Externo (Vistas)**, es el nivel más alto. Describe solo la parte de la base de datos que es relevante para un usuario común, y oculta todo lo demás. 

_Independencia física, el hardware no afecta al esquema lógico
Independencia lógica, se pueden añadir nuevas tablas o columnas sin que las vistas o programas (nivel externo) dejen de funcionar, siempre y cuando no se elimine algo que se esté usando_

## Arquitectura para Sistemas de Bases de Datos
**Centralizada**, todo el procesamiento, el sistema gestor de bases de datos y la interfaz gráfica corren en una única gran computadora (mainframe). Los usuarios se conectan a través de terminales "tontas" que solo muestran texto, sin procesar nada. 
**Cliente-Servidor**, el trabajo se divide. El Cliente (el equipo del usuario) se encarga de la interfaz gráfica y de hacer las peticiones de datos. El Servidor (una máquina centralizada) ejecuta el sistema gestor de bases de datos, procesa la consulta y devuelve solo los resultados. 
**Distribuida**, la base de datos no está en un solo servidor. Los datos están fragmentados o replicados a través de múltiples servidores conectados por una red, pero el sistema gestor de bases de datos hace que el usuario piense que está consultado una única base de datos. 

## Propiedades ACID
Propiedades que garantizan que una transacción en una base de datos sea segura. 
**A - Atomicidad**, la transacción se hace completa o no se hace nada. 
**C - Consistencia**, la base datos siempre debe pasar de un estado válido a otro estado válido, respetando todas las reglas (como que un saldo no quede negativo si no es permitido).
**I - Aislamiento**, si hay múltiples usuarios haciendo transacciones al mismo tiempo, el sistema debe tratarlas como si fueran secuenciales para que no choquen entre sí.
**D - Durabilidad**, una vez que la transacción se completó (hizo commit), los datos se guardan permanentemente y ya no se pierden. 

<hr>

## Modelos de Datos y Diseños 
**Entidad**, es cualquier cosa u objeto del mundo real (físico o abstracto) del cual queremos guardar información. Estudiante, Usuario
**Atributos**, características que describen a cada entidad. Para la entidad Usuario, los atributos serían nombre, edad, celular. 
**Dominio**, es el conjunto de valores válidos que puede tomar un atributo. Por ejemplo, si el atributo es Estatura_cm el valor tendría que ser positivo, mayor a cero y menor a 300. 
**Relación**, es la asociación lógica entre dos o más entidades. Un usuario tiene asignado un rol. 

_Atributos derivados, se calculan de otros atributos. Por ejemplo: Edad no sería un atributo o un dato que se le pide al usuario, si no que se le pide la fecha de nacimiento DATE y la edad se calcula restando con la fecha actual_

## Modelado y Diagramas

### Tipos de Llaves (Claves)
No se pueden relacionar tablas si no están identificadas. 
**Llave Primaria (Primary Key - PK)**, es el atributo que identifica de manera única e irrepetible a un registro dentro de una entidad.
**Llave Foránea (Foreign Key - FK)**, es el atributo en una entidad que hace referencia a la Llave Primaria de otra entidad. Es el "gancho" que une a las dos tablas. 
**Llave Candidata (Primary Key - PK)**, son todos los atributos que podrían haber sido la llave primaria, pero que al final no se eligió. Por ejemplo, si aun usuario se le pide un ID, número de celular, correo. Pero para llave primaria me decido por elegir ID, entonces los demás atributos serían las llaves candidatas porque son único e irrepetibles pero no se eligieron. 
**Llave Compuesta (Primary Key - PK)**, cuando necesitas dos o más columnas juntas para crear un identificador. Es una llave primaria que está formada por dos o más columnas juntas. Por ejemplo la tabla intermedia que se crea cuando existe una relación de muchos a muchos, ya que al pasar a tener dos relaciones de uno a muchos en esta tabla intermedia se guardan dos llaves foráneas que juntas hacen la llave compuesta, por que ambas hace un solo registro. 

### Cardinalidad 
Define cuántas instancias de una entidad A pueden asociarse a instancias de una entidad B. 

 **1:1 (Uno a Uno)**, una entidad A se relaciona con solo una entidad B.
 **1:N (Uno a Muchos)**, una entidad A se relaciona con muchas entidades B.
 **N:M (Muchos a Muchos)**, muchas entidades A se relacionan con muchas entidades B. Para hacer esta relación se tiene que crear una tabla intermedia (tabla de rompimiento, entidad asociativa o tabla de intersección), entonces la relación muchos a muchos pasa a ser dos relaciones uno a muchos 1:N. Esta tabla de rompimiento solo almacena "punteros" (llaves foráneas) hacia las tablas
 principales, más los datos que solo existen cuando ambas se interactúan. 

## Dibujado de Diagrama Entidad-Relación (notación Chen)
**Rectángulos normales**, representan una entidad fuerte, es decir, existe por sí sola. 
**Rectángulo doble**, entidad débil, su existencia depende de otra entidad. 
![](../recursos/Pasted%20image%2020260809211250.png)

**Óvalo normal**, atributo estándar. Por ejemplo: Nombre
**Óvalo con el texto subrayado**, indica que ese atributo es la llave primaria.
**Óvalo con línea punteada**, atributo derivado. Es un dato que no se almacena físicamente, sino que se calcula a partir de otro. Por ejemplo: la edad, ya que se pide la fecha de nacimiento no la edad cómo tal. 
**Óvalo doble**, atributo multivaluado. Se usa cuando un atributo puede tener varios valores al mismo tiempo. 
![](../recursos/Pasted%20image%2020260809211417.png)
![](../recursos/Pasted%20image%2020260809211427.png)
![](../recursos/Pasted%20image%2020260809211437.png)
![](../recursos/Pasted%20image%2020260809211448.png)
![](../recursos/Pasted%20image%2020260809211459.png)

**Rombo normal**, relación estándar. Adentro se escribe un verbo.
**Rombo doble**, relación identificadora. Se usa exclusivamente para conectar una entidad fuerte con una entidad débil. 
![](../recursos/Pasted%20image%2020260809211608.png)

![](../recursos/Pasted%20image%2020260809211619.png)

## Modelo Relacional 
Es la traducción técnica del diagrama entidad-relación al diagrama relacional. 
En el modelo relacional cambian los términos y sus significados: 
**Relación**, es el equivalente a lo que conocemos como Tabla. En el ER la relación era el rombo, pero en el relacional "Relación" es la tabla completa.
**Tupla**, es el equivalente a una fila o registro. Por ejemplo todos los dato de un usuario en específico. 
**Atributo**, sigue siendo la columna o la característica de una entidad. 
**Grado**, es el número de columnas o atributos que tiene la tabla. 
**Cardinalidad**, para el contexto del modelo relacional se refiere al número de filas que tiene la tabla. 

### Diseño y Dibujado: Notación Pata de Gallo
UNO, obligatorio
![](../recursos/Pasted%20image%2020260809211800.png)

UNO, opcional
![](../recursos/Pasted%20image%2020260809211814.png)

MUCHOS, opcional
![](../recursos/Pasted%20image%2020260809211840.png)

MUCHOS, obligatorio (uno a muchos)
![](../recursos/Pasted%20image%2020260809211829.png)

### Pasar del Diagrama ER al Diagrama Relacional 
**Entidades Fuertes**, cada rectángulo fuerte se convierte en una tabla normal con su llave primaria.
**Relaciones 1:1**, la llave primaria de cualquiera de las dos tablas puede viajar a la otra como llave foránea. Se elige la que tenga más sentido lógico.
**Relaciones 1:N**, la llave primaria de la tabla del lado UNO siempre viaja y se convierte en la llave foránea en la tabla del lado de MUCHOS .
**Relaciones N:M**, el rombo desaparece y se crea la tabla intermedia llamada tabla de rompimiento. En esta nueva tabla se guardan las llaves primarias de ambas tablas, que termina generando una llave compuesta. 

<hr>

## Normalización 
Es el proceso para organizar los datos, minimizar la redundancia (datos repetidos innecesariamente) y evitar problemas al insertar, actualiza o eliminar registros. 

### Dependencia Funcional 
Es una relación estricta entre dos columnas de una misma tabla. Ocurre cuando el valor de un atributo determina el valor de otro. Y los tipos principales de dependencias funcionales son: 
- **Total**, cuando el atributo depende de toda la llave primaria
- **Parcial**, cuando depende solo de una parte de una llave compuesta
- **Transitiva**, cuando un atributo depende de otro atributo que no es llave primaria. 

### Primera Forma Normal 1FN
El objetivo principal es eliminar los grupos repetitivos. Evitar la redundancia.
Los atributos tienen que ser atómicos (es decir, indivisibles ya que un átomo ya no se puede partir en algo más), entonces en una celda de la base de datos solo debe contener un valor lógico y no una lista de varias cosas. 
Eliminar datos o columnas que se repiten innecesariamente. 
**Solución para para la primera forma normal**, crear una nueva tabla que esté relacionada con su respectiva llave foránea. 
### Segunda Forma Normal 2FN
Primero se tiene que estar en 1FN. Segundo, todos los atributos que no sean llave deben depender completamente de toda la llave primaria, no solo de una parte de ella. Dependencia Total. 

### Tercera Formal Normal 3FN
Primero se tiene que estar en 2FN. Segundo, no deben existir dependencia transitivas. Es decir, los atributos que son llave no deben depender de otro atributo que no sea llave. 

<hr>

## Lenguajes de Bases de Datos
**DDL (Data Definition Language / Lenguaje de Definición de Datos)**, sirven para construir, modificar o destruir las estructuras (las tablas, las bases de datos).
Comandos: _CREATE, ALTER, DROP, TRUNCATE_

**DML (Data Manipulation Language / Lenguaje de Manipulación de Datos)**, sirven para interactuar con la información que está adentro de las tablas.
Comandos: _INSERT, UPDATE, DELETE_

**DQL (Data Query Language / Lenguaje de Consulta de Datos)**, sirve exclusivamente para buscar y leer información sin modificarla. 
Comandos: _SELECT, WHERE, GRUOP BY, ORDER BY, JOIN_, y funciones como _SUM, COUNT_

## Algebra Relacional y Operaciones de Conjunto 

### Operaciones Relacionales Especiales
**Selección**, filtra filas (tuplas). Devuelve registros completos que cumplan una condición específica. 
Equivalente SQL: _WHERE_

**Proyección**, filtra columnas (atributos). Devuelve solo las partes de la tabla que interesen, descartando el resto. 
Equivalente SQL: _SELECT_

**Reunión**, une dos tablas diferentes utilizando una columna que tengan en común, generalmente la Llave Primaria y la Llave Foránea. 
Equivalente SQL: _INNER JOIN_

### Operaciones de Conjunto 
**Unión**, suma las filas de dos consultas y elimina los repetidos o duplicados.
Equivalente SQL: _UNION_

**Intersección**, devuelve únicamente las filas que existen simultáneamente en ambos conjuntos. 
Equivalente SQL: _INTERSECT_ si se hace sobre las mismas tablas entonces puede ser un _INNER JOIN_

**Diferencia**, devuelve las filas que están en el conjunto A, pero que no están en el conjunto B.
Equivalente SQL: _EXCEPT_ (_MINUS_ en motores como Oracle)

**Producto Cartesiano**, combina todas las filas de la tabla A con todas las filas de la tabla B. Si A tiene 10 filas y B tiene 10 filas, el resultado tendrá 100 filas. 
Equivalente SQL: _CROSS JOIN_

#### Servidor vs Cliente de Base de Datos
**El motor / Servidor (Sistema Gestor de Base de Datos)**, es el servicio invisible que corre en el fondo de la computadora. No tiene interfaz gráfica; es pura lógica y almacenamiento (MySQL Server)
**El Cliente (Gestor)**, es el programa visual que instalas para no tener que usar la consola negra de comandos. (MySQL Workbench)

### Cómo procesa internamente una consulta la computadora
Por ejemplo en la siguiente consulta: 
```
SELECT estudiantes.nombre, asignaciones.nota
FROM estudiantes
INNER JOIN asignaciones
ON estudiantes.carnet = asignaciones.estudiante_carnet;
```
1. FROM / INNER JOIN, el motor primero va al disco, busca ambas tablas y las fusiona matemáticamente. 
2. ON, después de fusionar la tabla estudiantes con la tabla asignaciones, hace un filtrado de esta fusión y deja solo las filas donde el carnet coindice, es decir, dónde la llave primaria coincide con la llave foránea 
3. SELECT, de último ya solo selecciona las columnas que solicité en la consulta 

**INNER JOIN**, es una intersección. Si no hay coincidencia en ambas tablas, el registro desaparece del resultado. 
**LEFT JOIN**, garantiza que toda la información de la tabla izquierda (la que va después del FROM) aparecerá en el reporte final, tenga o no tenga relación con la tabla de la derecha. 

## Procedimiento Almacenado 
Es un bloque de código SQL que se guarda directamente dentro del servidor de base de datos para ser reutilizado. Para que sirven: 
**Seguridad**, evita los ataques de inyección SQL porque la aplicación externa no envía instrucciones directas, solo manda a llamar al procedimiento. 
**Rendimiento**, reduce el tráfico de red. En lugar de que mi aplicación mande 30 líneas de código SQL por internet, solo envía una, que es la de llamar al procedimiento almacenado. Además, el motor de base de datos los pre-compila, haciéndolos más rápidos. 
**Centralización**, si la regla de negocio cambia, modificas el procedimiento en el servidor una sola vez y todas las aplicaciones que lo consumen (web, móvil, escritorio) se actualizan automáticamente.

## Trigger (Disparador)
Es un bloque de código SQL que se ejecuta (se dispara) automáticamente justo antes o justo después de que ocurra un evento de manipulación (INSERT, UPDATE o DELETE) en una tabla específica. Dentro de estos existen comandos que permiten acceder a los datos en tránsito: 
**NEW**, contiene los datos nuevos que se están intentando guardar. Solo existe en los _INSERT_ y _UPDATE_
**OLD**, contiene los datos viejos que estaban en la celda antes de ser modificados o borrados. Solo existe en los _UPDATE_ y _DELETE_

_Las consultas se hacen en bloque, es decir, se hacen varias al mismo tiempo_

## Cursores - Cursor 
Un cursor equivale a un ciclo FOR o WHILE, es decir, toma un SELECT, lo guarda en memoria y permite avanzar registro por registro obteniendo sus datos para procesarlos.


