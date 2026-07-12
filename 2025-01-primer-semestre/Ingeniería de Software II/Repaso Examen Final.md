<hr>
## ¿Qué son las métricas de producto?

Las **métricas de producto** son medidas que se aplican directamente al **software que se está construyendo**. Evalúan características como el tamaño, complejidad, estructura, calidad y rendimiento del producto final.

Se utilizan para:
- Evaluar la calidad del software.
- Estimar costos y esfuerzos.
- Detectar posibles problemas estructurales.
- Mejorar mantenibilidad, reutilización y confiabilidad.

### **Complejidad ciclomática**
- **Definición**: es una métrica que mide el número de caminos linealmente independientes a través del código fuente de un programa. Cuanto más alto es el número, más compleja es la lógica.

Cantidad de opciones de ejecución que tiene una función. 

Para el cálculo se empieza en 1, y después se van sumando todos los caminos posibles. 

**¿Por qué es importante?**
- Indica cuántas pruebas mínimas se necesitan para cubrir todos los caminos lógicos.
- Valores altos (>10) indican código difícil de mantener y propenso a errores.

### **Acoplamiento y Cohesión**

#### **Acoplamiento (Coupling)**
- **Definición**: Mide el grado de **dependencia** entre módulos. Cuanto más dependiente es un módulo de otro, mayor es el acoplamiento.
Cada módulo debe funcionar en gran medida de forma independiente.

#### **Cohesión (Cohesion)**
- **Definición**: Mide el grado en que los **elementos dentro de un mismo módulo** están relacionados entre sí.
- **Ideal**: **Alta cohesión**. Todas las funciones del módulo deben estar fuertemente relacionadas y enfocadas en una sola tarea.
### **Fan-In y Fan-Out** 
Estas métricas miden las **relaciones entre módulos**:

| Métrica     | ¿Qué mide?                                                                                                                                                               | Valor ideal | Implicaciones                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ---------------------------------------------------------------- |
| **Fan-In**  | Número de módulos que **llaman o usan** a un módulo dado<br><br>Cuántos módulos llaman a un mismo módulo. Por ejemplo, el módulo B, C, D llaman al módulo A.             | Alto        | Módulo muy reutilizable, pero puede volverse un punto crítico    |
| **Fan-Out** | Número de módulos a los que un módulo **llama o depende**<br><br>Un mismo módulo cuánto depende de otros o cuántos llama a otros. Por ejemplo, que el A llame a B, C, D. | Bajo        | Si es alto, el módulo está demasiado acoplado y puede ser frágil |
- Una función `validarEmail()` que es llamada desde 5 módulos → **Fan-In = 5**
- Una función `generarFactura()` que utiliza 4 servicios → **Fan-Out = 4**

#### Cuadro comparativo: ITIL vs COBIT

| Característica   | **ITIL**                            | **COBIT**                                    |
| ---------------- | ----------------------------------- | -------------------------------------------- |
| Enfoque          | Gestión de servicios de TI          | Gobierno y control de TI                     |
| Creador          | Gobierno del Reino Unido (AXELOS)   | ISACA (organización internacional)           |
| Finalidad        | Mejorar la entrega de servicios     | Asegurar control, cumplimiento y alineación  |
| Nivel            | Táctico / operativo                 | Estratégico / gerencial                      |
| Alcance          | Interno en TI                       | Empresarial (TI alineada con negocio)        |
| Procesos típicos | Incidentes, problemas, cambios, SLA | Evaluación, dirección, monitoreo             |
| Uso común en     | Mesa de ayuda, centros de soporte   | Auditorías, gestión de riesgos, cumplimiento |
## ¿Qué es Gobierno?

**Gobierno de TI** (IT Governance) es la **responsabilidad de los altos directivos** (como el CEO, CIO, Junta Directiva) para **asegurar que TI esté alineado con los objetivos del negocio**, **agregue valor**, y se **gestionen adecuadamente los riesgos**.

### 📌 Características del Gobierno:

- Toma decisiones **estratégicas**.
- Se enfoca en el **qué se debe lograr** (objetivos).
- Alinea TI con el negocio.
- Evalúa resultados.
- Define políticas y dirección general.

## ¿Qué es Control?

**Control de TI** se refiere a los **mecanismos, procesos y políticas** que aseguran que las actividades de TI se realicen correctamente y conforme a lo planeado.

### 📌 Características del Control:

- Se ejecuta a nivel **operativo** o **táctico**.
- Se enfoca en **cómo se logra** lo planeado.
- Implementa procedimientos específicos.
- Mitiga riesgos.
- Supervisa tareas y operaciones diarias.

## Relación entre ambos:
- El **Gobierno define** el rumbo → El **Control lo ejecuta y asegura que se cumpla**.
- El Gobierno **establece expectativas** → El Control **las traduce en acciones y monitoreo**.

| Aspecto             | **Gobierno**                                  | **Control**                                           |
| ------------------- | --------------------------------------------- | ----------------------------------------------------- |
| Nivel               | Estratégico                                   | Táctico / Operativo                                   |
| ¿Quién lo ejerce?   | Alta dirección, comité de TI, junta directiva | Gerentes, técnicos, auditores                         |
| Enfoque             | Qué se quiere lograr                          | Cómo se logra y se verifica                           |
| Objetivo principal  | Alinear TI con el negocio                     | Garantizar que los procesos se cumplan correctamente  |
| Alcance             | Visión a largo plazo, valor del negocio       | Cumplimiento de políticas, procesos y procedimientos  |
| Actividades típicas | Establecer metas, políticas, gobernanza       | Controles de acceso, seguridad, monitoreo de procesos |
| Rol en COBIT        | Evalúa, dirige y monitorea                    | Planea, ejecuta y monitorea                           |

#### ¿Qué es COBIT?
**COBIT** es un marco de gobierno y gestión de TI que ayuda a las organizaciones a alinear la tecnología con los objetivos del negocio, garantizando control, cumplimiento, calidad y gestión de riesgos en los procesos de TI.

#### ¿Qué es ITIL?
**ITIL** (Information Technology Infrastructure Library) es un marco de mejores prácticas para la **gestión de servicios de TI**, que ayuda a las organizaciones a **ofrecer servicios de calidad**, alineados con las necesidades del negocio, mediante procesos como gestión de incidencias, cambios, y niveles de servicio.