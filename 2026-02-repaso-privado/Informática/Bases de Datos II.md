**Integridad Referencial**
Evita relaciones inválidas, como registrar una vente de un producto inexistente, esto solamente si se aplica las restricciones correspondientes. 
La integridad referencial es un conjunto de reglas que garantiza que las relaciones entre las tablas de una base de datos sean válidas y coherentes. _La integridad referencial evita que un registro haga referencia a otro registro que no existe, evita datos huérfanos_.

Ejemplo: 
En un supermercado se tienen dos tablas cliente y venta. Un cliente tiene dos ventas registradas, ahora supongamos que se quiere registrar una nueva venta: con id_cliente 99, nos podemos dar cuenta que el cliente 99 no existe, si lel SGBD permite esto, se estaría registrando una venta de un cliente que no existe, entonces con una llave foránea bien configurada se tiene que rechazar esta inserción, porque no se estaría cumpliendo con la integridad referencial. 

Otro problema es que se quiera eliminar al cliente 1, esto porque ya tiene ventas registradas, aquí se tienen varias opciones: 
- Eliminar en cascada, elimina al usuario y todos los registros que tenga el en otras tablas. 
- Se impide eliminar al cliente mientras tenga ventas relacionadas. 
- Se eliminan los campos de usuario en las demás tablas pasando a NULL. 

![485](../recursos/Pasted%20image%2020261102164956.png)
![488](../recursos/Pasted%20image%2020261102164328.png)

**Sistema Gestor de Base de Datos - SGBD**
Un sistema gestor de base de datos es el software encargado de crear, administrar, consultar, proteger y recuperar las bases de datos.  Algunos ejemplos: MySQL, PostgreSQL, SQL Server, Oracle. 

Es importante comprender que la base de datos y el SGBD no son lo mismo: 
- La base de datos contiene los datos y su estructura.
- El SGBD proporciona los mecanismos para acceder a los datos y administrarlos. 

**¿Qué es SQL y que operaciones permite?**
SQL (Lenguaje de Consulta Estructurado), es el lenguaje estándar utilizado para trabajar con bases de datos relacionales. Principales categorías: 
- **DDL**, lenguaje de definición de datos. Define la estructura de la base de datos. 
	- CREATE
	- ALTER
	- DROP
- **DML**, lenguaje de manipulación de datos.  Manipula los datos dentro de una tabla. 
	- INSERT
	- UPDATE
	- DELETE
- **DQL**, lenguaje de consulta de datos. Consulta lo datos, los busca y los presente, sin modificar los datos. S
	- SELECT

### Vista
Una vista es un objeto de base de datos que representa el resultado de una consulta definida previamente. En una vista normal o consulta normal, se muestra todo el contenido de una consulta. Ahora suponiendo que se tiene la tabla "empleado", con las columnas: id, nombre, departamento y salario; y una secretaria de recepción quiere información de los empleados, pero ella no tendría por qué tener acceso a la información de salarios, entonces se crea la vista "info_empleado" y la vista únicamente mostrará: nombre y departamento. 
![510](../recursos/Pasted%20image%2020261102162537.png)
Entonces la vista al final proporciona una especie de interfaz más sencilla a consultas que tienen información sensible y que obviamente limita la información que se muestra. Importante también, una vista por sí sola no asegura una protección real, se tiene que configurar los permisos, ya que si se tiene acceso a la tabla original de nada servirá la vista. 

### Transacciones 
Una transacción es una unidad lógica de trabajo que agrupa una o varias operaciones sobre una base de datos y que debe completarse bajo ciertas garantías de consistencia y confiabilidad.
En otras palabras: _una transacción es una operación (o proceso) que necesita ejecutarse como un conjunto, porque si una parte falla, no tendría sentido conservar únicamente los cambios realizados hasta el momento donde fallo._

#### Cómo funciona una Transacción
Trabaja con tres instrucciones fundamentales: 
1. **BEGIN / START TRANSACTION**, inicia una transacción explícita.
2. **COMMIT**, confirma los cambios realizados.
3. **ROLLBACK**, reviere los cambios no confirmados. 
```
START TRANSACTION;

INSERT INTO tabla.columna VALUES (0, "nombre");
UPDATE tabla SET columna="valor" WHERE id = 1;
COMMIT; 
```

**Propiedades ACID**

_A- Atomicidad_
Una transacción se trata como una unidad indivisible, sus cambios se confirman como conjunto o se revierten. _Todo o nada_. Si la transacción no se hace completa no se hace nada. 
_C - Consistencia_
Una transacción correcta debe llevar la base de datos de un estado válido a otro estado válido, respetando las restricciones establecidas. Por ejemplo: si se exige que una cuenta no pueda quedar con saldos negativos, la operación o el proceso de la transacción debe comprobar esto y no debe violar esa restricción. 
_I - Aislamiento_
Controla cómo interactúan las transacciones simultáneas para evitar interferencias indebidas. La base de datos debe tomar todas las transacciones como si fueran secuenciales, una después de la otra. 
D - Durabilidad 
Una vez se confirme la transacción, sus cambios deben sobrevivir a fallos del sistema dentro de las garantías ofrecidas por el SGBD y su configuración. Por ejemplo: si el banco confirma una transferencia y luego se reinicia el servidor, la transferencia confirmada no debería desaparecer. 

#### ¿Cómo se Recuperan las Transacciones Después de un Fallo?
Imaginando que una transacción ya se confirmó, pero inmediatamente se interrumpe la energía eléctrica. Para que el SGBD sepa que transacciones conservar y cuáles descartar (se conservan solo las que se confirmaron, COMMIT, las que se quedaron a medias se descartan), se utiliza el siguiente mecanismo: 
**Registro de Transacciones - Transaction Log**
Es una estructura donde el sistema registra información sobre los cambios y operaciones que permiten recuperar la base de datos después de determinados fallos. 
_Recuperar Transacciones o es lo mismo que restaurar un backup_.

## Seguridad en Base de Datos 

**¿Qué significa proteger una base de datos?**
La tríada de seguridad: 
1. **Confidencialidad**, solo personas autorizadas acceden a la información. 
	1. Que un empleado sin permiso consulte salarios de todo el personal.
2. **Integridad**, los datos conservan su exactitud y no sufren alteraciones indebidas. 
	1. Que alguien modifique el precio de un producto sin autorización.
3. **Disponibilidad**, los sistemas y datos son accesibles cuando se necesiten. 
	1. Que una falla impida realizar ventas durante varias horas. 

La seguridad debe equilibrar estos tres principios. 
Pero en un hospital por ejemplo, se prefiere la disponibilidad y la integridad, en un sistema bancario se prefiere más la confidencialidad y la integridad.

**Métodos de Autenticación**
Cómo se comprueba que realmente es quien dice ser. 
- **Algo que sé**, PIN o contraseña 
- **Algo que tengo**, llave de seguridad o aplicación de autenticación (celular)
- **Algo que soy**, huella digital o reconocimiento facial

**Control de Acceso Basado en Roles**
Consiste en asignar permisos a roles y después asociar usuarios a esos roles. Se complementa con el principio de mínimo privilegio. Cada usuario, aplicación o servicio debe tener únicamente los permisos indispensables para cumplir sus funciones. 

#### Protección de los Datos en Tránsito, En Reposo y en Uso
- **En tránsito**, para web usar únicamente HTTPS, certificado TLS. También se pueden enviar datos o consultas usando consultas parametrizadas. 
- **En reposo**, cifrado de disco, cifrado de campos y backups cifrados
- **En uso**, aislamiento de procesos, control de memoria, entornos de ejecución protegidos. 

Importante también implementar _Hardening_, que es el endurecimiento del sistema. Consiste en reducir la superficie de ataque eliminando configuraciones, funciones y accesos innecesarios y aplicando una configuración segura. 

**Diferencia entre Auditoría y Monitoreo**
La auditoría registra eventos relevantes para poder revisarlos y atribuir acciones. 
El monitoreo observa el comportamiento de los sistemas y permite identificar anomalías o fallos que requieren atención. 

**Defensa en Profundidad**
Consiste en implementar varias capas de seguridad independientes y complementarias, para que la falla de una medida no signifique necesariamente que todo el sistema quede comprometido. 

**Ejemplo**
![592](../recursos/Pasted%20image%2020261102183442.png)

### Recuperación y Respaldos 

**Respaldo - Backup**
Creación de una copia recuperable de los datos y de la información necesaria para restaurarla. 

**Restauración**
Proceso de recuperar los datos desde ese respaldo-backup y colocarlos nuevamente en un entorno de base de datos. 

**Recuperación**
Proceso más amplio que permite devolver la base de datos a un estado consistente y utilizable. Puede incluir aplicar registros de transacciones, resolver transacciones incompletas y habilitar nuevamente el servicio. 

#### Tipos de Backup - Respaldos

**Backup Completo**
Un backup completo contiene la información necesaria para restaurar la totalidad de la base de datos o del conjunto de datos incluido en el respaldo. 

_¿Cuándo Conviene?_
Cuando se tiene una base de datos pequeña o mediana, cuando se desea una base periódica de recuperación o cuando se necesita un respaldo completo antes de determinados trabajos de mantenimiento. 

**Backup Diferencial**
Contiene los cambios realizados desde el último respaldo completo utilizado como base. 
Guarda todos los datos que han cambiado desde la última copia de seguridad completa. 
- Es más rápida y sencilla, porque solo necesita la copia completa inicial más la última copia diferencial. 

_¿Cómo se restaura?_
Si ocurre un fallo después de haberse creado el diferencial se necesitará: 
1. El backup completo
2. El último diferencial válido 

**Backup Incremental**
Guarda únicamente los datos que han cambiado desde la última copia de seguridad realizada (ya sea otro incremental o la copia completa). 
- La restauración es más lenta y compleja, ya que para recuperar la información se necesita la copia completa inicial más todas las copias incrementales en orden. 