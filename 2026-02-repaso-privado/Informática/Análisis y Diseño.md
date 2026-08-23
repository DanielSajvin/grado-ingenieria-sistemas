![](../recursos/Pasted%20image%2020260809190316.png)
## Actividades Estructurales 
1. Comunicación, hablar con el cliente, levantar requerimientos, entender el negocio
2. Planeación, definir riesgos, recursos, cronogramas y estimaciones
3. Modelado, diseñar la arquitectura, la base de datos y la interfaz (UML, diagramas)
4. Construcción, escribir el código y las pruebas
5. Despliegue, entregar el software al cliente, instalarlo y dar soporte
### Levantamiento de Requerimientos
El análisis de requerimiento es la fase donde se define qué necesita el cliente, esto se tiene que hacer antes de pensar en cómo se va a programar. Los requerimientos se dividen estrictamente en tres categorías: 
1. **Requerimientos Funcionales (El Qué)**, define lo que el sistema debe hacer. Son los comportamientos, funciones, entradas de datos, procesos lógicos y salidas que el software ejecutará. Si el software no hace esto, pues simplemente no sirve para su propósito principal. Característica: _Siempre se redactan con verbos de acción_. Un ejemplo puede ser: El sistema debe permitir al usuario _registrar_ un nuevo perfil con correo y contraseña. 
2. **Requerimientos No Funcionales / Atributos de Calidad (El Cómo)**, define cómo debe comportarse el sistema. No son funciones, si no restricciones tecnológicas, métricas de calidad y exigencias sobre la arquitectura del software. Si fallan el sistema hace lo que debe hacer, pero lo hace mal (lento, inseguro, inestable). Los requerimientos no funcionales o atributos de calidad se dividen en categorías clave sobre atributos de calidad: 
	1. Rendimiento, tiempos de respuesta.
	2. Escalabilidad, que el software tenga la capacidad de seguir creciendo. 
	3. Seguridad, por ejemplo que las contraseñas estén encriptadas. 
	4. Disponibilidad, que el software se mantenga funcionando y no sufra caídas o si las sufre que no se por mucho tiempo y tampoco tan seguido. 
	5. Usabilidad, que sea intuitivo y nada complejo para usuario nuevos. 
3. **Reglas de Negocio (El Por Qué)**, son políticas, leyes, regulaciones o decisiones operativas propias de la empresa o del país. Existen independientemente de si hay o no hay software. El software simplemente se programa para respetarlas y hacerlas cumplir. Por ejemplos: un cliente menor de 18 años no puede crear una cuenta nueva, un cliente no puede hacer devoluciones después de 30 días. 

### Técnicas de Recolección de Datos (Elicitación)
**Entrevistas**, reuniones uno a uno con los Stakeholders (personas interesadas) para extraes información cualitativa profunda. 
**Cuestionarios / Encuestas**, para obtener información cuantitativa cuando hay cientos de usuarios.
**Observación**, sentarse al lado del usuario mientras hace su trabajo actual para ver los problemas reales, esto porque el usuario puede mentir en los cuestionarios o entrevistas, o simplemente no saben explicar lo que hacen. 

### Especificación de Requerimientos de Negocio
Es el documento formal que nace después de analizar la Arquitectura y las Vistas de Negocio. Este documento no habla de botones, bases de datos ni de lenguajes de programación. Habla estrictamente de qué problemas de negocio se van a resolver. Define el "Alcance" del proyecto para evitar que el cliente pida cosas que no estaban pactadas. 
**Contenido**, documenta quiénes son los patrocinadores (quién paga), los objetivos financieros, las restricciones legales y las reglas de negocio principales.
**Diferencia clave**, el documento especificación de requerimientos de negocio se escribe en lenguaje administrativo/gerencial. De este documento nacerá después el documento con la Especificación de requerimientos del Software, que es el que sí está dirigido a los programadores y contiene todos los diagramas UML, casos de uso y requerimientos técnicos. 

## Modelación de Requerimientos 
En este punto ya se sabe qué quiere el negocio. Ahora toca "traducirlo" al equipo de programación. 

### Enfoque Ágil
**Historias de Usuario**, son descripciones cortas, simples y escritas desde la perspectiva del usuario final. No entran en detalles técnicos hiper-complejos al inicio. La estructura obligatoria de una historia de usuario es: 
```
Como [Rol / Actor], quiero [Acción / Funcionalidad] para [Beneficio / Valor de negocio].
```
Ejemplo: 
"Como Administrador de Servidor, quiero poder reiniciar la instancia desde una interfaz web, para no tener que entrar por consola SSH cada vez que el servicio se caiga".
También se tiene que tener en cuenta los criterios de aceptación, estas son condiciones que deben cumplirse para dar la historia por terminada. Por ejemplo: debe pedir confirmación de dos pasos antes de reiniciar. 

### Enfoque Tradicional 
Pertenece al Lenguaje Unificado de Modelado (UML). Son mucho más detallados, formales y estructurados. Un caso de uso describe paso a paso la interacción entre un "Actor" (humano o sistema) y el software. Elementos clave del diagrama de casos de uso: 
1. Actor, quien inicia la acción
2. Flujo Principal, el paso a paso de lo que ocurre si todo sale perfecto
3. Flujos Alternos, qué hace el sistema si hay un error 
4. Relaciones:
	1. ```<<include>>```  un caso de uso llama obligatoriamente a otro.
	2. ```<<extend>>``` un comportamiento opcional. 

![](../recursos/Pasted%20image%2020260814182810.png)


<hr>

### Ingeniería de Software 
No es lo mismo que programar. Es la aplicación de un enfoque sistemático, disciplinado y cuantificable al desarrollo, operación y mantenimiento de software. 

**¿Qué significa en la práctica?**, un programador solo escribe el código. Un ingeniero de software diseña cómo ese código será probado (testing), cómo se llevará el control de versiones (Git), cómo se gestionarán los errores y cómo hacer para que otro ingeniero pueda leer ese código después de cierto tiempo y pueda entenderlo perfectamente. 

**Enfoque**, calidad, mantenibilidad, estándares y metodologías

### Arquitectura de software
La arquitectura de software se encarga de definir los componentes principales del software, sus propiedades externar y las relaciones (comunicación) entre ellos (entre los componentes).

**¿Qué significa en la práctica?**, el arquitecto no programa un botón, por ejemplo, si no que se encarga de decidir si el sistema usará una base de datos relacional o no relacional, si el backend estará separado del frontend, si se usará un servidor monolítico o microservicios, y qué protocolos de seguridad conectarán los nodos. 

**Enfoque**, escalabilidad, seguridad y la topología del sistema. Las decisiones arquitectónicas son las más costosas de cambiar una vez que el proyecto avanza. 

### Ciclo de Vida de Desarrollo de Software
Es el marco de trabajo (framework) que describe las fases por las que pasa un software desde que es una idea hasta que es retirado o reemplazado. Básicamente entonces el ciclo de vida de desarrollo de software es el "qué pasos hay que dar" para desarrollar un software. 

**Fases Universales**: 
1. Análisis de Requerimientos 
2. Diseño 
3. Implementación
4. Pruebas 
5. Despliegue y Mantenimiento 

**Actividades Estructurales**: 
1. Comunicación 
2. Planeación
3. Modelado 
4. Construcción
5. Despliegue
Roger Pressman cambia los nombres de las fases universales, con el objetivo que se pueda adaptar también a cada modelo de desarrollo. 

## Modelos de Desarrollo 

### Modelo Tradicional o Ciclo de Vida Clásico 
El principio de este modelo es que una fase no se puede iniciar hasta que la anterior haya terminado. 
#### Modelo en Cascada
**Fases del Modelo Tradicional en Cascada**
1. **Análisis de Requerimientos:** se documenta todo lo que hará el sistema, es decir, se define el alcance del software. 
2. **Diseño:** se define la base de datos, la infraestructura y los componentes.
3. **Desarrollo o Implementación:** es la fase en la que se codifica y se construye como tal el software
4. **Pruebas:** unitarias, de integración y de sistema 
5. **Despliegue y Mantenimiento:** es cuando ya pasa a producción.
El punto débil de este modelo de desarrollo es la _Gestión del cambio_, ya que si por ejemplo durante la fase de pruebas el cliente quiere cambiar algo, primero se tiene que modificar toda la documentación previa hasta este punto y después de todo eso ya se empieza a tocar el código, todo esto tomando en cuenta el impacto el costos y tiempo. 

![](../recursos/Pasted%20image%2020260814152507.png)
#### Modelo en V
Es una evolución estricta del modelo en cascada. Su principal característica es que demuestra cómo las fases de prueba se relacionan directamente con las fases de análisis y diseño. 
**Brazo Izquierdo**:
1. Análisis de requerimientos
2. Diseño
3. Diseño Arquitectónico 
4. Diseño de Módulos
**Vértice**
	La fase codificación o programación
**Brazo Derecho (Pruebas)**
1.. Pruebas Unitarias
2.. Pruebas de Integración
3.. Pruebas de Sistema
4.. Pruebas de Aceptación 

![](../recursos/Pasted%20image%2020260809190252.png)

### Modelos Ágiles 
No se trata de fases secuenciales, se trata de iteraciones cortas. Ya que en este modelo se asume que los requerimientos pueden ir cambiando. 
#### Metodología SCRUM
Se trata de realizar iteraciones cortas llamadas _Sprints_ que duran de 1 a 4 semanas. 
Según la guía oficial de Scrum un Sprint debe durar un mes o menos, de 1 a 4 semanas.
El estándar, las empresas optan por hacer Sprints de 2 semanas. 
**Roles**:
- **Product Owner (PO)**: su trabajo es entender el negocio, hablar con el cliente y escribir el _Product Backlog_ (la lista de todo lo que el sistema debe tener). Decide que tiene más valor para el negocio. No programa.
- **Scrum Master**: no es el jefe del equipo, es más bien un líder servicial. Su trabajo es asegurar que todos respeten las reglas de SCRUM y eliminar impedimentos técnicos o administrativos.
- **Dev Team**: son los ingenieros, analistas, diseñadores y testers. Ellos deciden cómo construir técnicamente lo que pide el _Product Owner_. Se auto-organizan
**Artefactos**:
- **Product Backlog**: estas son las historias de usuario, es decir, todo lo que el usuario desea que el sistema haga y cómo funcione. 
- **Sprint Backlog**: lo que el equipo se compromete a entregar en el Sprint actual. 
- **Incremento**: es el software que ya funciona, está probado y listo para usarse al final de Sprint. 
**Ceremonias**:
- **Planning**, se hace una sola vez al inicio del Sprint. El equipo se reúne con el _Product Owner,_ el PO dice por ejemplo que módulos quiere ya terminados al finalizar el Sprint y el equipo analiza técnicamente y crea el _Sprint Backlog_.
- **Daily**, se hace todos los días y dura un máximo de 15 minutos. Todo el equipo de desarrollo debe responder a tres preguntas: 
	- ¿Qué hice ayer?
	- Qué haré hoy?
	- ¿Tengo algún bloque que me impida avanzar?
- **Review (Revisión)**, se hace al final del Sprint. El equipo le muestra al cliente el software funcionando. 
- **Retrospective**, se hace después de la _Review_. Solo participa el equipo técnico y el _Scrum Master._ Analizan qué hicieron bien, qué hicieron mal y cómo mejorar para el siguiente Sprint. 

#### Programación Extrema (XP - Extreme Programming)
Se caracteriza por ser programación en parejas. La programación extrema indica cómo programar con excelencia técnica, entonces sus prácticas clave son: 
1. **Desarrollo Guiado por Pruebas**, primero se escribe el código de la prueba unitaria (que lógicamente va a fallar) y después se escribe el código para que pase la prueba.
2. **Programación en parejas**, dos desarrolladores en un solo teclado/monitor, uno escribe el código y el otro revisa en tiempo real si ese código es el mejor o no. Esto evita demasiado los bugs. 
3. **Integración Continua**, el código se integra al repositorio principal varias veces al día y se compila automáticamente. 
4. Solo se programa lo que se necesita hoy. Está prohibido hacer funcionalidades "por si acoso" en el futuro.

### Modelos Evolutivos 
Son el puente entre lo tradicional y lo ágil. La premisa de los modelos evolutivos es que _en el software, los requisitos nunca están claros al principio y van a cambiar_. Entonces en lugar de forzar al cliente a adivinar el futuro o de obligarlo a recibir piezas terminadas cada cierto tiempo, el modelo evolutivo funciona en base a la experiencia real del cliente. 
#### Prototipos
Se construye una versión rápida (muchas veces desechable) para validar con el usuario requerimientos que no están claros, antes de construir el sistema real. Pero no solo se trata de hacer "pantallas", existen dos enfoques principales: 
1. **Prototipo Desechable:** se hace rápidos, con herramientas de mockup (como Figma) o código basura. Solo se usa para entender al usuario. Una vez aprobado este prototipo se desecha y ya se empieza a programar desde cero con una buena arquitectura. 
2. **Prototipo Evolutivo**: se construye sobre una arquitectura real desde el día 1. El primer prototipo es muy básico, pero el código es sólido y se va iterando sobre él hasta convertirse en el producto final. 

#### Espiral
Está diseñado para proyectos inmensos, costosos y con alta incertidumbre o riesgo tecnológico. El proyecto da "vueltas" en espiral pasando por 4 cuadrantes en cada iteración:
1. **Determinar Objetivos**,  se determina qué es lo que se quiere lograr en esta vuelta
2. **Análisis y Evaluación de Riesgos**, si en este cuadrante se detecta que el riesgo técnico es insalvable, el proyecto se cancela antes de gastar en programación.
3. **Desarrollo y Pruebas**, se construye esa parte del software.
4. **Planificación**, se revisa con el cliente y se planea la siguiente vuelta. 

![](../recursos/Pasted%20image%2020260814160032.png)

#### Desarrollo Basado en componentes 
En lugar de programar, se trata de ensamblar. 
Primero se hace el levantamiento de requerimientos y después se buscan componentes o librería que ya hagan eso. Entonces acá el trabajo no es codificar la lógica interna, sino diseñar las interfaces de comunicación para que estos componentes de terceros hables entre sí de forma segura. 

### Modelos Orientados a Arquitectura 
Son inmensos y abstractos, usados a nivel corporativo (gobiernos, multinacionales). Estos modelos en lugar de enfocarse primero en los requerimientos detallados o en escribir código rápido, este modelo dicta que lo primero y más importante es definir los cimientos, las reglas lógicas y las conexiones del software. 

#### Zachman Framework
No es un proceso paso a paso. Es una matriz (una tabla de 6x6) que cruza las preguntas fundamentales (Qué, Cómo, Dónde, Quién, Cuándo, Por qué) con las diferentes vistas de negocio (El planificado, el dueño, el diseñador, el constructor). Garantiza que no quede un solo aspecto de la empresa sin documentar. 
![](../recursos/Pasted%20image%2020260818105540.png)

#### Model Driven (MDA)
Dirigida a por modelos. Aquí los diagramas UML son tan exactos y perfectos, que utiliza herramientas de software para generar el código fuente automáticamente a partir de los diagramas. 

### Modelos de Referencia 
Son estándares masivos de la industria. Un modelo de referencia indica qué piezas debe tener el sistema y cómo deben relacionarse entre sí para que todo el mundo hable el mismo idioma. 

#### RUP (Rational Unified Process)
Es de IBM. Es iterativo pero muy estructurado. Está guiado por Casos de Uso. Tiene 4 fases: Inicio, Elaboración, Construcción y Transición. En cada fase hay iteraciones. 

#### CMM / CMMI (Capability Maturity Model)
No es un modelo para crear software. Es una certificación para evaluar qué tan madura y profesional es una empresa de software. Tiene 5 niveles: 
1. Inicial / Caótico 
2. Gestionado
3. Definido 
4. Gestionado Cuantitativamente 
5. En Optimización 

## Arquitectura del Negocio
No se trata de arquitectura de software. Se enfoca más en ver a "qué se dedica la empresa". Define la estrategia, la estructura organizacional, los procesos clave y cómo la empresa genera valor.
Es importante conocer esto porque si se desarrolla un software que técnicamente esté bien, pero que no esté alineado con la arquitectura del negocio (por ejemplo automatizar un proceso que la empresa planeaba eliminar), el software prácticamente no sirve y es un fracaso. También se ve si el proyecto es viable o no económicamente hablando. 
En la industria, para no inventar esto desde cero, los ingenieros y arquitectos utilizan marcos de trabajo masivos (como TOGAF - The Open Group Architecture Framework). Según estos estándares, la arquitectura del negocio se compone de artefactos muy específicos: 
1. _Mapas de capacidad del negocio_, una capacidad es lo que el negocio hace, no cómo lo hace. Por ejemplo, Gestión de cobros. 
2. _Cadenas de Valor_, representa el flujo de actividades, de principio a fin, que crean un resultado de valor para un cliente (interno o externo). Ayuda al ingeniero a entender en qué parte exacta del flujo el software va a inyectar eficiencia. 
3. _Mapa Organizacional y Actores_, identifica la estructura jerárquica, las unidades de negocio y los roles de las personas. 
4. _Alineación Estratégica_, es la matriz que justifica la existencia del software. Cada línea de código o infraestructura que el ingeniero proponga debe poder rastrearse hace arriba hasta llega a un objetivo estratégico. 

### Vistas de Negocio
Una vez ya se entendió la arquitectura del negocio, ahora es cuando se tiene que recolectar información. Una empresa es demasiado compleja entenderla de un solo vistazo. Las "Vistas" son diferentes perspectivas de la misma organización, dependiendo de quién la mire. En el levantamiento de requerimientos, se debe extraer información de múltiples vistas, ya que el error común es levantar requerimientos hablando solo con una persona (generalmente el gerente) e ignorar a los demás. Existen tres vistas principales para recolectar o levantar requerimientos: 
1. **Vista Estratégica (Visión de los directores / CEO)**, les importan los costos, el retorno de inversión, los objetivos a largo plazo, las métricas globales y el crecimiento de la empresa. 
2. **Vista Operativa (Visión de los Gerentes / Supervisores)**, les importan los flujos de trabajo diarios, la eficiencia de los empleados y los procesos tácticos y propia gestión del personal. 
3. **Vista Técnica u Operacional (Visión de los Usuarios finales / Infraestructura)**, les importa cómo se hace el trabajo físico o digital paso a paso, la usabilidad de las herramientas y las restricciones físicas. 

### Especificación de Requerimientos (o Procesos) de Negocio 
Es el resultado formal de analizar las Vistas de Negocio. Es el acta de nacimiento del Proyecto. 
Este documento no contiene especificaciones de software (no hay diagramas UML, no hay historias de usuario, no hay mención de bases de datos), su propósito es de blindar el proyecto administrativa y financieramente. Un documento Especificación de Requerimientos de Negocio debe contener estrictamente: 
1. Impulsores de negocio, justificar por qué la empresa está gastando dinero en este proyecto ahora. 
2. Objetivos de negocio, metas medibles, cuantificables y con fecha límite. Estas metas se deben redactar con el formato SMART. 
3. Alcance y Fuera de Alcance, los límites de lo que el software va afectar, para evitar que nos pidan hacer algo que no estaba pactado en el futuro. 
4. Restricciones de negocio, limitaciones de tiempo, presupuesto o regulaciones legales que no se pueden cambiar. 
Esto documento define el Por qué y para qué del negocio. 

## Flujos de Trabajo y Técnicas de Recolección de Datos

### Técnicas de Recolección
1. **Entrevistas**, ideales para gerentes o directores. Se hacen uno a uno. Sirven para extraer los objetivos estratégicos y presupuestosos. 
2. **Observación**, consiste básicamente en sentarse al lado del trabajador por ejemplo y verlo trabajar, sin interrumpirlo ni nada, solo observando. Se usa porque el trabajar muchas veces no sabe explicar su propio trabajo u omite pasos. 
3. **Cuestionarios/Encuestas**, se usan cuando se tienen usuarios distribuidos geográficamente o son demasiados. 
4. **Análisis de documentos,** revisar manuales antiguos, leyes o formularios físicos que la empresa ya usa. 

### Flujos de Trabajo
Antes de proponer software, se tiene que diagramar el _AS-IS (Tal cual)_, que se refiere a cómo funciona el proceso hoy en día, incluyendo errores y atrasos. Después de tener claro cómo funciona actualmente ya se pasa a diagramar el _TO-BE (Ser)_, que es cómo funcionará el flujo de trabajo después de que el software esté implementado. Esto con el objetivo de no automatizar algo que es ineficiente por ejemplo, pero también para comprender realmente todo el flujo de trabajo. 

### Actividades de la determinación de requerimientos

#### Espacio del Problema
Es el mundo del cliente. Aquí solo se habla de necesidades, dolores de cabeza de la empresa y objetivos

#### Espacio de la Solución
Es el mundo del ingeniero. Aquí se habla de tecnologías, arquitecturas y código. 

_Nunca se tiene que saltar al espacio de la solución sin haber definido completamente el espacio del problema_

#### Definición del Dominio 
El ingeniero debe adoptar el vocabulario de la empresa. Si el negocio llama a sus clientes Atletas, en la base de datos la tabla debe llamarse atletas, no usuarios ni clientes. Esto para evitar errores de traducción entre programadores y clientes.

#### Administración del Cambio
Se tiene que asumir que los requerimientos van a cambiar a mitad del proyecto. Entonces se tiene que determinar o establecer un protocolo para afrontar estos cambios en los requerimientos. ¿Quién autoriza un cambio?, ¿Cómo se documenta?, ¿Cómo se evalúa el impacto en tiempo y costo?, y esto se logra mediante matrices de trazabilidad, donde se cruza cada requerimiento con el módulo de código que lo implementa para saber qué se rompe si cambia algo. 

### Artefactos
Son los documentos formales que se generan posterior o durante la fase de requerimientos.

**Documento de Visión**
Es el puente entre Especificación de Requerimientos del negocio y el código. Alinea a todo el equipo para que entiendan qué están construyendo y para quién. Contiene el problema planteado, las características principales del producto y el perfil de los interesados (stakeholders). El objetivo es evitar que el equipo programe funciones que a nivel técnico estén perfectas, pero no resuelven el problema principal. 

**Especificación de Casos de Uso**
La especificación es el documento de texto que acompaña al dibujo. Este documento ayudar a comprender mejor el dibujo, por lo tanto debe contener lo siguiente: 
- _Precondiciones_, ¿Qué tiene que ser verdad ANTES de que el caso de uso empiece? Por ejemplo, el usuario debe tener una sesión activa y rol de Administrador
- _Flujo Básico (Happy Path)_, los pasos 1, 2, 3 donde todo sale perfecto. 
- _Flujos Alternos_, qué pasa si el usuario ingresa mal la contraseña, si el sistema pierde conexión, entre otros. 
- _Postcondiciones_, ¿En qué estado queda el sistema o la base de datos DESPUÉS de que el caso de uso termina exitosamente? Por ejemplo, el estado de la factura cambia a "Pagada" y se envía un correo. 

**Especificaciones Suplementarias**
Este documento almacena todos los Requerimientos No Funcionales (rendimiento, seguridad, usabilidad) y reglas de negocio globales que afectan a la arquitectura completa y no a un solo caso de uso en particular. 

**User Persona**, es un personaje ficticio, un arquetipo, que representa a un segmento de los usuarios reales. Se le pone nombre, edad, nivel de habilidad tecnológica, frustraciones diarias y metas. Ejemplo, en lugar de decir "el software es para los contadores", el equipo diseña para "Doña Marta, 55 años, lleva 20 años usando Excel, se frustra si hay muchos botones en pantalla, su meta es salir a tiempo"; automáticamente el equipo sabe entonces que debe tener una interfaz minimalista. 

**Historias de Usuario**, la historia de usuario es corta y fomenta la conversación entre el programador y el cliente. El caso de uso es largo y busca ser un manual técnico inamovible. La estructura de una historia de usuario es la siguiente: 
```
Como [Rol / Actor], quiero [Acción / Funcionalidad] para [Beneficio / Valor de negocio].
```

<hr> 

### Diagrama Casos de Uso
Es una representación gráfica en _UML (Unfied Modelling Languaje - Lenguaje de Modelado Unificado)_ que muestra el comportamiento esperado de un sistema. Define el qué debe hacer el sistema desde la perspectiva del usuario o actor externo, sin entrar en detalles técnicos de su implementación interna. El diagrama se compone de 5 elementos estrictos: 

**El Actor**
Representa un rol, no a una persona específica. Siempre interactúa con el sistema desde afuera. 
- _Actor Principal_, quien inicia el caso de uso para lograr un objetivo. Se dibuja a la izquierda. 
- _Actor Secundario_, un sistema externo, base de datos de terceros o persona que el sistema necesita para completas el caso de uso (Ejemplo, una pasarela de pagos de Visa). 

**El Caso de Uso (El óvalo)**
Representa una funcionalidad concreta que aporta valor al actor.
Siempre se escribe con un verbo en infinitivo más un sustantivo. Por ejemplo, Registrar Usuario, Generar Reporte, Calcular Impuesto. 

**El Límite del Sistema (El Rectángulo)**
Es una caja grande que agrupa todos los casos de uso. El nombre del software se pone en la parte superior. Los actores siempre van fuera de la caja; los casos de uso siempre van adentro. Esto demuestra visualmente qué es responsabilidad del código y qué viene de afuera. 

**Relación de Asociación (Línea Continua)**
Es una línea simple (sin flecha, o con flecha simple) que conecta al Actor con el Caso de Uso. Significa: este actor ejecuta o participa en esta funcionalidad. 

**Relaciones Avanzadas**
```<<include>>``` (Inclusión), es una dependencia obligatoria. Ocurre cuando un caso de uso base necesita llamar a otro caso de uso para poder terminar su trabajo. 
- _Cómo se dibuja_, una flecha punteada que SALE del caso de uso base y APUNTA al caso includio, con la etiqueta ```<<include>>```.

```<<extend>>``` (Extensión), es un comportamiento opcional. Ocurre cuando un caso base puede, bajo ciertas condiciones, ejecutar pasos adicionales. 
- _Cómo se dibuja_, una flecha punteada que SALE del caso de uso opcional y APUNTA al caso de uso base, con la etiqueta ```<<extend>>```. Aquí la flecha va "al revés".

```Generalización``` (Herencia), se usa cuando un caso de uso o actor hereda características de otro, pero agrega algo específico. 
- _Cómo se dibuja_, una línea continua con una flecha en forma de triángulo vacío apuntando al padre. 

### Diagrama de Flujo 
El diagrama de flujo no maneja concurrencia (procesos paralelos) ni calles. Es puramente lineal, pensado para un solo hijo de ejecución de la computadora. Su simbología es la siguiente: 

**Terminal (Óvalo o Elipse)**, marca exclusivamente el Inicio y el Fin del algoritmo. 
![258](../recursos/Pasted%20image%2020260822143925.png)

**Entrada / Salida (Paralelogramo)**, se usa cuando el sistema recibe datos o cuando imprime algo en pantalla. 
![350](../recursos/Pasted%20image%2020260822175851.png)

**Proceso (Rectángulo)**, se usa para cualquier operación matemática, asignación de variables o llamado a funciones. 
![308](../recursos/Pasted%20image%2020260822180629.png)

**Decisión (Rombo)**, evalúa una condición lógica. Siempre obligatoriamente, deben salir dos flechas de el: una etiquetada con "Si" y otra con "No".
![346](../recursos/Pasted%20image%2020260822181759.png)

**Flujo (Flechas)**, conectan los símbolos. En un diagrama de flujo, el flujo siempre debe ir de arriba hacia abajo y de izquierda a derecha. 
![333](../recursos/Pasted%20image%2020260822182503.png)

### Diagrama de Actividades (o de calle)
El diagrama de actividad nos dice cómo fluye el proceso paso a paso a lo largo del tiempo. Es la evolución orientada a objetos del clásico diagrama de flujo. Demuestra la lógica de negocio y, sobre todo, los procesos paralelos o concurrentes (cosas que ocurren al mismo tiempo en el procesador o en la empresa). Tiene los siguientes elementos estrictos: 

**Nodo inicial**, un círculo negro y relleno. Indica dónde arranca el proceso. (Solo puede haber uno por diagrama). 
![](../recursos/Pasted%20image%2020260822135015.png)

**Actividad / Acción**, un rectángulo con las esquinas redondeadas. Dentro va la acción empezando con un verbo. Por ejemplo, Validar datos, Calcular total. 
![](../recursos/Pasted%20image%2020260822135116.png)

**Flujo de Control (Línea de Transición)**, una línea con una flecha abierta que conecta una ctividad con la siguiente. 
![588](../recursos/Pasted%20image%2020260822140038.png)

**Nodo de Decisión (Rombo)**, un rombo de donde salen dos o más flechas. Sirve para los condicionales (IF/ELSE). Importante: cada flecha que sale del rombo debe tener una "Guarda" (una condición escrita entre corchetes, ejemplo: [Aprobado] o [Rechazado]).
![](../recursos/Pasted%20image%2020260822135723.png)

**Barras de Sincronización (Fork y Join)**, se dibujan como una línea negra gruesa (horizontal o vertical). 
- _Fork (División)_, entran una sola flecha y salen dos o más flechas. Significa que a partir de ahí, las actividades se ejecutan al mismo tiempo (concurrencia/hilos).
- _Join (Unión)_, entran dos o más flechas y sale una sola. El proceso no puede continuar hasta que todas las tareas paralelas hayan terminado.
![466](../recursos/Pasted%20image%2020260822140411.png)

**Nodo Final**, un círculo negro rodeado por otro círculo. Indica que el proceso terminó por completo. 
![](../recursos/Pasted%20image%2020260822140622.png)

**Calles**, se divide la hoja en columnas. Cada columna tiene el nombre de un Actor o Sistema. Sirve para saber quién es el responsable de ejecutar cada rectángulo de actividad. 

## Modelación Visual UML

### Diagrama de Estados
El diagrama de estados modela exclusivamente el ciclo de vida de un solo objeto a lo largo del tiempo, desde que nace hasta que es destruido. A diferencia del diagrama de actividades que modela el paso a paso de un proceso general donde participan muchos actores. Este diagrama es crítico para entidades complejas, como un Factura (borrador -> emitida -> pagada -> anulada) o una conexión de red (cerrada -> escuchando -> establecida -> desconectada). El diagrama de estados tiene los siguientes elementos estrictos: 

**Estado Inicial**, un círculo negro relleno.
![](../recursos/Pasted%20image%2020260822191508.png)

**Estado**, un rectángulo con las esquinas redondeadas. Representa una situación o condición en la que se encuentra el objeto en un momento dado. El nombre del estado debe ser un adjetivo o un participio (ejemplo: Pendiente, Conectado, Bloqueado), NUNCA un verbo de acción (no se dice "Pagando", se dice Pagado).
![361](../recursos/Pasted%20image%2020260822191843.png)

**Transición (Flecha)**, una línea con una flecha abierta que conecta un estado con otro. Indica que el objeto cambió de estado. 
![374](../recursos/Pasted%20image%2020260822191937.png)

**Etiquetas de Transición**, cada flecha debe llevar texto encima que explique por qué cambió de estado. La sintaxis oficial UML es: 
- ``` Evento [Condición] / Acción```
	- Evento, el disparador (por ejemplo, Hacer clic())
	- Condición, es opcional. Una guarda lógica entre corchetes (ejemplo, [saldo < 0])
	- / Acción, es opcional. Qué hace el sistema durante el cambio. (ejemplo, / Enviar correo).

**Estado Final**, un círculo negro rodeado por otro círculo. Indica que el objeto dejó de existir o completó su ciclo de vida útil. 
![367](../recursos/Pasted%20image%2020260822192347.png)

