
![[../recursos/Pasted image 20260809185714.png]]
## Actividades Estructurales 
1. Comunicación, hablar con el cliente, levantar requerimientos, entender el negocio
2. Planeación, definir riesgos, recursos, cronogramas y estimaciones
3. Modelado, diseñar la arquitectura, la base de datos y la interfaz (UML, diagramas)
4. Construcción, escribir el código y las pruebas
5. Despliegue, entregar el software al cliente, instalarlo y dar soporte

## Modelos de Desarrollo 

### Modelo Tradicional 
El principio de este modelo es que una fase no se puede iniciar hasta que la anterior haya terminado. 
**Fases del Modelo Tradicional en Cascada**
1. **Análisis de Requerimientos:** se documenta todo lo que hará el sistema, es decir, se define el alcance del software. 
2. **Diseño:** se define la base de datos, la infraestructura y los componentes.
3. **Implementación:** es la fase en la que se codifica y se construye como tal el software
4. **Pruebas:** unitarias, de integración y de sistema 
5. **Despliegue y Mantenimiento:** es cuando ya pasa a producción.
El punto débil de este modelo de desarrollo es la _Gestión del cambio_, ya que si por ejemplo durante la fase de pruebas el cliente quiere cambiar algo, primero se tiene que modificar toda la documentación previa hasta este punto y después de todo eso ya se empieza a tocar el código, todo esto tomando en cuenta el impacto el costos y tiempo. 

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
![[../recursos/Pasted image 20260809185739.png]]

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
1. **Desarrollo Guiado por Pruebas**, primero se escribe el código de la prueba unitaria (que lógicamente va a fallar) y después se escribe el código para que pase la prueba, 
2. **Programación en parejas**, dos desarrolladores en un solo teclado/monitor, uno escribe el código y el otro revisa en tiempo real si ese código es el mejor o no. Esto evita demasiado los bugs. 
3. **Integración Continua**, el código se integra al repositorio principal varias veces al día y se compila automáticamente. 
4. Solo se programa lo que se necesita hoy. Está prohibido hacer funcionalidades "por si acoso" en el futuro.

### Modelos Evolutivos 
Son el puente entre lo tradicional y lo ágil. 
#### Prototipos
Se construye una versión rápida (muchas veces desechable) para validar con el usuario requerimientos que no están claros, antes de construir el sistema real. Pero no solo se trata de hacer "pantallas", existen dos enfoques principales: 
1. **Prototipo Desechable:** se hace rápidos, con herramientas de mockup (como Figma) o código basura. Solo se usa para entender al usuario. Una vez aprobado este prototipo se desecha y ya se empieza a programar desde cero con una buena arquitectura. 
2. **Prototipo Evolutivo**: se construye sobre una arquitectura real desde el día 1. El primer prototipo es muy básico, pero el código es sólido y se va iterando sobre él hasta convertirse en el producto final. 

#### Espiral
Está diseñado para proyectos inmensos, costosos y con alta incertidumbre o riesgo tecnológico. El proyecto da "vueltas" en espiral pasando por 4 cuadrantes en cada iteración:
1. **Determinar Objetivos**, se determina qué es lo que se quiere lograr en esta vuelta
2. **Análisis y Evaluación de Riesgos**, si en este cuadrante se detecta que el riesgo técnico es insalvable, el proyecto se cancela antes de gastar en programación.
3. **Desarrollo y Pruebas**, se construye esa parte del software.
4. **Planificación**, se revisa con el cliente y se planea la siguiente vuelta. 

#### Desarrollo Basado en componentes 
En lugar de programar, se trata de ensamblar. 
Primero se hace el levantamiento de requerimientos y después se buscan componentes o librería que ya hagan eso. Entonces acá el trabajo no es codificar la lógica interna, sino diseñar las interfaces de comunicación para que estos componentes de terceros hables entre sí de forma segura. 

