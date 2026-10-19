## Conceptos Base

**Activo**
Cualquier recurso de valor para la organización que debe ser protegido. En el contexto moderno, los datos y la información constituyen el activo crítico (bases de datos, contraseñas, propiedad intelectual, registros o información de clientes), junto con la infraestructura física y lógica que los almacena, procesa y transmite. 

**Vulnerabilidad**
Es una debilidad, falla o defecto interno presente en el diseño, configuración, implementación o procedimiento de un sistema, que se está propenso a ser explotada. 
Ejemplos: 
- Código web sin validación de entradas, software sin parches de seguridad, contraseñas por defecto en un switch o usencia de políticas de caducidad de accesos (contraseñas). 

_Una vulnerabilidad por sí sola no causa daño; es simplemente una puerta sin llave esperando a ser descubierta._

**Amenaza**
Cualquier evento, circunstancia o actor potencial con la capacidad de aprovechar una vulnerabilidad y provocar daño o pérdida al activo. 
- Se divide en el **agente de la amenaza**, cibercriminales, empleados deshonestos, grupos patrocinados por estados; y el **evento de la amenaza**, ataque de ransomware, desastre natural, interrupción de suministro. 

**Ataque**
La materialización intencional o intento coordinado por parte de una amenaza de explotar una vulnerabilidad para comprometer la seguridad de un activo. 

**Impacto**
La magnitud del daño o pérdida que sufre la organización si el ataque tiene éxito o el riesgo se materializa. Puede ser **técnico** (pérdida de integridad de los datos, denegación del servicio), **económico** (multas, rescates, lucro cesante) o **reputacional** (pérdida de clientes, cobertura mediática negativa). 

**Riesgo**
Es la probabilidad de que una amenaza concreta explote una vulnerabilidad determinada y produzca un impacto adverso medible sobre uno o varios activos. 

**Vector de ataque**
La ruta, técnica o medio específico empleado por un actor de amenaza para acceder a un sistema y explotar una vulnerabilidad. 
Ejemplos: 
- Correo hacía un empleado por medio de phishing, puertos expuestos a internet sin MFA (autenticación multifactor), inyección SQL en un endpoint. 

**Superficie de Ataque**
La totalidad de puntos de entrada físicos, lógicos y humanos que un atacante puede intentar explotar para acceder a un entorno o extraer datos. Reducir la superfie de ataque es una regla dorada: cerrar puertos no utilizados, desinstalar servicios innecesarios y aplicar el principio de menor privilegio (es una regla de seguridad que indica que un usuario, programa o proceso solo debe tener los permisos y accesos estrictamente necesarios para realizar su trabajo y nada más).

**Defensa en profundidad**
Enfoque arquitectónico que descarta la idea de un "único perímetro infraqueable". Consiste en disponer múltiples capas de controles independiente (físicos, de red, perimetrales, de host, de aplicación y a nivel de datos). Si una capa falla o es vulnerada, la siguiente previene la fuga del activo. 

Ejemplo del ciclo de vida de un incidente: 
_Un Actor de Amenaza utiliza un vector de ataque para explotar una vulnerabilidad presente en la superficie de ataque, ejecutando un ataque exitoso que materializa el riesgo, generando un impacto negativo sobre la confidencialidad, integridad o disponibilidad de un Activo crítico._

## Pilares de la Seguridad Informática 
1. **Confidencialidad**
2. **Integridad**
3. **Disponibilidad**

### Confidencialidad 
Garantiza que la información solo sea accesible para las empresas, entidades o sistemas debidamente autorizados. Su objetivo entonces es, asegurar que solo quien tiene credenciales y permisos legítimos pueden leer la información. Se suele proteger con: 
- Cifrado y control de acceso
- Listas de control de acceso y esquemas de mínimos privilegios
- Enmascaramiento de datos (proceso de ocultar información confidencial mediante la sustitución de datos originales por valores ficticios, realistas o con una estructura similar) y ofuscación (revuelve, mezcla, cifra o aplica funciones matemáticas a los datos para ocultar su significado, es más complejo que el enmascaramiento de datos). 

### Integridad 
Asegura que los datos sean exactos, fiables y que no hayan sido alterados, manipulados o destruidos de forma no autorizada durante su almacenamiento o transmisión. Es decir, se prioriza la exactitud, completitud y autenticidad de lo activos e información, evitando modificaciones no autorizadas o no detectadas. En otras palabras _garantiza que el dato que sale de un emisor sea idéntico al que llega al receptor, y que los registros almacenados no hayan sido alterados maliciosamente ni corrompidos por fallas de hardware/software._ Se suelen proteger con: 
- Firmas digitales y códigos de autenticación de mensajes. 
- Control de versiones, bitácoras inmutables y transaccionalidad ACID en bases de datos. 

### Disponibilidad
Garantiza que los usuarios autorizados tengan acceso a la información y a los sistemas informáticos en el momento y lugar en que los necesiten, sin interrupciones. Es decir, se asegura que los sistemas, redes y datos sean accesibles y utilizables por los usuarios autorizados en el momento oportuno en que lo requieran. Entonces se garantiza que los servicios donde residen los datos no experimenten caídas, interrupciones o denegaciones de servicio. Esto se asegura con los siguiente mecanismos: 
- Redundancia de infraestructura (balanceadores de carga)
- Planes de continuidad y respaldos periódicos verificados (BCP/DRP)
- Mitigación de ataque de Denegación se Servicio Distribuida (DDoS)

## Encontrar el Balance 

**Seguridad vs Usabilidad**
A mayor cantidad de capas y controles de acceso, menor agilidad operativa para el usuario final. 

**Confidencialidad vs Disponibilidad**
Cifrar exhaustivamente con algoritmos pesados o implementar bloqueos agresivos ante intentos fallidos incrementa la confidencialidad, pero eleva la latencia y puede derivar en una auto-denegación de servicio (afectando la disponibilidad). 
Si se protege la información bloqueando cuentas al tercer intento fallido o aislando servidores desconectados de internet, un atacante puede genera bloqueos masivos deliberados o los operadores no pueden dar soporte rápido. 
**Solución**, es mejor implementar controles graduales en lugar de bloqueos absolutos. En lugar de congelar una cuenta, se introducen retardos exponenciales o autenticación multifactor. 

**Integridad vs Rendimiento**
Firmar, hashear y verificar criptográficamente cada datos en tiempo real añade latencia computacional, afectando a la velocidad del sistema. 
**Solución**, implementar un procesamiento asíncrono y desacoplado. Se garantiza la disponibilidad respondiendo al usuario con una confirmación transaccional inmediata en memoria, y los procesos pesados de verificación de integridad o auditoría se ejecutan en segundo plano. 

**Confidencialidad vs Usabilidad**
Forzar contraseñas de 20 caracteres que cambian cada 15 días hace que los usuarios busquen atajos: anotarlas en notas adhesivas o recurrir a herramientas no autorizadas. 
**Solución**, seguridad adaptativa y transparente. Implementar inicio de sesión único, autenticación basada en riesgo (pedir segundo factor solo si la IP o ubicación es sospechosa) y gestores de contraseñas corporativos. 

### El contexto del negocio manda
Para elegir que pilar de seguridad priorizar o para determinar cuál "es mas importante" nos podemos basar en lo que la empresa hace o que activo es el que maneja principalmente: 
- **Banca y Finanzas**, se asegura la _Integridad_. El saldo y los registros deben ser exactos; un error de un centavo corrompe todo el libro contable. 
- **Salud**, se prioriza la _Disponibilidad_. El monitor cardíaco o e expediente de alergias en emergencias debe estar accesible al instante; un retado cuesta vidas. 
- **Militar, Inteligencia, Secretos Militares**, se prioriza la _Confidencialidad_. Si la información clasificada se filtra, el daño es irreversible; es preferible destruir el dato que dejarlo expuesto. 
- **Punto de Venta**, se prioriza _Disponibilidad_ y de inmediato Integridad. Si el punto de venta no cobra, la fila se acumula, el cliente se va a la competencia y venta se pierde. También que se pueda cobrar fuera de línea. 
- **Control de Inventario**, se prioriza _Integridad_. Un inventario disponible pero corrupto es inservible, si el sistema indica que hay 50 unidades de un productos y en bodega física hay 0, se comprometen las compras, se generan órdenes fantasma y se descordina la cadena de suministro. 

## Clasificación y Valoración de Activos de Información
_No se puede proteger lo que no se sabe que se tiene, ni se puede gastar más en proteger un activo de lo que el activo realmente vale._

### Inventario de Activos
Antes de clasificar los activos, se tiene que realizar un inventario formal. Un activo de información no es únicamente hardware:
- **Información / Datos**, bases de datos de clientes, código fuente, secretos comerciales, credenciales, respaldos, archivos de configuración. 
- **Software**, aplicaciones web, sistemas ERP, sistemas operativos, motores de BD, utilitarios. 
- **Hardware**, servidores, firewalls, routers, estaciones de trabajo, dispositivos móviles, unidades de almacenamiento. 
- **Personal**, usuarios finales, administradores de sistemas, desarrolladores, soporte técnico. 
- **Servicios / Infraestructura**, enlaces de internet, DNS, centros de datos, servicios cloud (AWS, Azure).

### Esquemas de Clasificación de la información
Se clasifica según el grado de confidencialidad y el impacto que provocaría la divulgación o alteración de la información. En el ámbito empresarial y de estándares internacionales (ISO/IEC 27001), el esquema más utilizado comprende de 4 niveles: 
1. **Público**, información divulgable sin riesgo de impacto negativo (catálogos de precios, comunicados de prensa).
2. **Uso Interno**, información para la operación cotidiana de la organización, que no debe exponerse al exterior pero cuya divulgación causaría un daño menor (organigramas, procedimientos operativos, minutas de reuniones)
3. **Confidencialidad**, datos de valor cuya divulgación o alteración causaría pérdidas financieras, sanciones regulatorias o daño a la reputación (datos personales de empleados o clientes, estados financieros, contratos con proveedores).
4. **Restringido o Crítico**, información de máxima sensibilidad dentro de la organización. Solo un puñado de personas autorizadas tiene acceso. (claves privadas de cifrado, secretos industriales, algoritmos propietarios, contraseñas maestras, credenciales de infraestructura).

