# Diagnóstico inicial — Redes

**Área:** Sistemas · Preparación del Privado  
**Inicio y primera sesión:** 2026-11-23  
**Estado general:** EN_ESTUDIO (diagnóstico integral incompleto)  
**Caso:** diseño y defensa oral en pizarra de una red para campus universitario ficticio de cuatro edificios.  
**Fuentes:** programas oficiales `Redes 2025.pdf`, `Redes I.pdf`, `Redes II.pdf`; apuntes `Sistemas/Redes I.md` consultados en GitHub; expediente maestro vigente.  
**Criterio:** completar una etapa no equivale a DOMINADO_VERIFICADO. Este último exige explicación sin apuntes, aplicación independiente y seguimiento. No consta verificación completa de dominio para ningún tema en esta sesión; la exposición fue una defensa oral con diagrama aportado por el estudiante, sin declaración expresa de haberla desarrollado sin consultar apuntes.

## Estado de las seis etapas

| Etapa | Estado de ejecución | Estado de conocimientos |
| --- | --- | --- |
| I. Arquitectura física y lógica | COMPLETADA satisfactoriamente el 2026-11-23 | EN_ESTUDIO; resultados favorables y reservas registradas |
| II. Direccionamiento IPv4, VLSM y VLAN | INICIADA: planteada la pregunta 1; estudiante no respondió | NO_DIAGNOSTICADO |
| III. Enrutamiento (inter-VLAN, rutas, OSPF, Internet) | PENDIENTE | NO_DIAGNOSTICADO; se hicieron repreguntas introductorias sobre OSPF en etapa I, no evaluación completa |
| IV. Redundancia (STP, fallas, convergencia) | PENDIENTE | NO_DIAGNOSTICADO formalmente; hubo evidencia puntual sobre VRRP y fallas en etapa I |
| V. Seguridad (ACL, firewall, aislamiento, gestión) | PENDIENTE | NO_DIAGNOSTICADO; solo decisiones arquitectónicas generales |
| VI. Medios y diagnóstico (cobre, fibra, cableado, pruebas) | PENDIENTE | NO_DIAGNOSTICADO formalmente; elección preliminar de medios evaluada parcialmente en etapa I |

## Caso y restricciones declaradas

- Campus ficticio: A Administración (120 dispositivos cableados, centro de datos y entrada ISP, 3 niveles), B Ingeniería (240, 4 niveles), C Biblioteca (100, 2 niveles), D Laboratorios (180, 3 niveles). Total inicial: 640 dispositivos cableados. Crecimiento mínimo: 30 %.
- Distancias orientativas entre edificios adyacentes: A–B 180 m; A–C 120 m; B–D 160 m; C–D 210 m. No son longitudes definitivas de tendido.
- Bloque IPv4 disponible: `10.40.0.0/16`. Segmentos requeridos: administración, docentes, estudiantes, invitados, servidores y gestión.
- Restricciones: no duplicar todos los componentes por presupuesto; proteger servicios internos frente a caída de Internet siempre que la infraestructura interna continúe operando; prever enlace alternativo donde sea técnicamente posible; gestionar acceso y seguridad.

## Etapa I — Arquitectura física y lógica (completada)

### Diseño y decisiones expuestas por el estudiante [RETROALIMENTACIÓN DEL USUARIO]

1. Conectar edificios por fibra óptica multimodo por sus distancias, mencionando un máximo general de 2 km.
2. Ubicar un switch multicapa principal por edificio (con duplicación de los equipos principales); preferirlo frente a router para crecimiento y puertos.
3. Representar inicialmente una red por edificio como simplificación del diseño físico, aclarando que después habrá varias redes o VLAN por edificio; posponer VLSM.
4. Organizar por edificio un diseño jerárquico de core, distribución y acceso: uno de distribución según presupuesto y switches de acceso por piso; cableado UTP vertical y horizontal hacia las terminales.
5. Duplicar los switches principales para uso de VRRP como redundancia de gateway.
6. Proponer dos ISP (Dual WAN), firewall perimetral y salida a Internet desde el edificio A.
7. Dibujar una estrella jerárquica y enlaces redundantes entre switches principales. Aclaración posterior: el esquema superior representa los cuatro edificios; el inferior amplía las conexiones de core de A y B y muestra distribución y acceso, sin dibujar en detalle C y D por tiempo. Manifestó que los pares de switches principales de B y C dispondrían de conexiones alternativas.
8. Reconocer explícitamente el switch único de distribución por edificio como punto único de falla deliberadamente aceptado por presupuesto; propuso duplicar distribución como mejora si se autorizara inversión.

### Preguntas y respuestas del examen [RETROALIMENTACIÓN DEL USUARIO]

- **Falla de switch de distribución del edificio A:** respondió que los switches de acceso dependientes pierden conexión y que VRRP no soluciona una falta de conectividad física. **Evaluación:** correcta para la topología propuesta.
- **Corte de fibra B–C:** explicó que, con un segundo enlace entre equipos principales y rutas alternativas, OSPF detectaría la falla y recalcularía rutas. **Evaluación:** razonable de manera condicional; no se verificaron detalles de capa 2/capa 3, rutas físicas independientes ni tiempo de convergencia. No es garantía de cero interrupción.
- **Mejora por presupuesto adicional:** añadir segundo switch de distribución por edificio y considerar STP. **Evaluación:** coherente, falta concretar enlaces de acceso y prevención de bucles.
- **Switch capa 2 frente a multicapa:** describió MAC/conmutación vs IP/enrutamiento y el multicapa como equipo capaz de ambos. **Evaluación:** fundamento correcto; precisión: el switch L2 puede transportar múltiples VLAN, pero no enruta entre ellas.
- **VRRP, gateway 10.40.10.1 de host 10.40.10.25/24:** identificó la IP virtual compartida lógicamente por SW-A1/SW-A2, elección master/backup, conmutación sin cambiar configuración del host, y ausencia de reparto automático de tráfico de un mismo grupo. **Evaluación:** respuestas correctas con seguimiento. Matiz: la recuperación de la función master depende de prioridades y preemption; VRRP no restaura enlaces o distribución.
- **OSPF frente a VRRP:** distinguió enrutamiento dinámico y métricas de costo (habitualmente relacionadas con ancho de banda) frente a disponibilidad del gateway. **Evaluación:** buena base; corregir la idea de que OSPF encuentra una ruta “hacia la puerta de enlace” del cliente: el cliente usa el gateway local y los equipos L3 enrutan hacia redes destino. No se probó implementación o cálculo de rutas.

### Competencias: evaluación y criterio de seguimiento

| Competencia | Evidencia y resultado | Estado formal |
| --- | --- | --- |
| Diseño jerárquico y ubicación de equipos | Defendió core/distribución/acceso en diagrama; satisfactorio | EN_ESTUDIO |
| Función de switch L2, multicapa y router | Diferenció conmutación/enrutamiento, con matiz sobre VLAN y motivo de selección; satisfactorio | EN_ESTUDIO |
| Topología física y enlaces de campus | Estrella jerárquica; explicó segundo dibujo; falta validar rutas alternativas específicas | EN_ESTUDIO |
| Restricción presupuestaria y riesgo | Justificó de forma explícita la distribución única, identificó el riesgo; satisfactorio | EN_ESTUDIO |
| Falla de equipo de distribución | Predijo desconexión de switches de acceso y límites de VRRP; satisfactorio | EN_ESTUDIO |
| VRRP | IP virtual, master/backup, failover, host sin cambio de gateway, sin balanceo automático; satisfactorio con matices | EN_ESTUDIO |
| OSPF introductorio | Reconoció propósito y costo; escenario condicional, no prueba completa | EN_ESTUDIO |
| Selección de medios | Fibra multimodo entre edificios, UTP interior; justificaciones parciales | EN_ESTUDIO |
| VLAN, VLSM, STP, ACL, configuración detallada, seguridad | No evaluados en sus respectivas etapas | NO_DIAGNOSTICADO |

**Ninguna competencia pasa a DOMINADO_VERIFICADO** por esta sesión. **No se asigna REFORZAR globalmente** a un tema a partir de una imprecisión aislada; las precisiones y pruebas pendientes están listadas abajo.

### Imprecisiones, pendientes y refuerzo dirigido

- **Fibra multimodo:** se afirmó que el máximo general es 2 km; no hay límite universal. Verificar categoría (OM), velocidad, ópticas, presupuesto óptico y distancia real. Selección multimodo provisionalmente posible, pero no acreditada.
- **Switch multicapa vs router:** la escasez de puertos no es el fundamento principal; justificar funciones L3, rendimiento y diseño modular, sin confundir crecimiento de terminales con necesidad de puertos físicos de routing.
- **Disponibilidad:** VRRP resuelve la redundancia del primer salto, no fallas del switch único de distribución ni la continuidad de toda la LAN. Especificar dominio de falla y conexión efectiva.
- **VRRP:** prioridad y preemption determinan si el master original reasume su rol al volver.
- **OSPF:** costo acumulado y configuración de métricas; convergencia no necesariamente inmediata; no confundir gateway virtual local con rutas de capa 3 hacia redes destino.
- **Redundancia entre edificios:** confirmar topología exacta por enlace, si es L2 o L3, diversidad de trayectorias y qué pasa al cortar B–C. No declarar “malla completa” sin enlaces correspondientes.
- **Vertical UTP:** diferencia entre backbone vertical y horizontal; comprobar longitudes reales (no solo alturas de pisos), capacidad agregada, PoE e interferencias según necesidades. Estudiar selección de medios en etapa VI.
- **STP, ACL, VLAN y VLSM:** no marcarlos como errores: todavía no fueron desarrollados ni evaluados en sus etapas.
- **[APUNTE]** `Redes I.md` contiene dudas antiguas sobre qué es IP y bits, y una numeración inconsistente de capa de red; **no** se comprobó que esas dudas persistan. Solo explorar si aparecen bloqueos durante casos posteriores.

### Reglas de la evaluación acordadas

- Anunciar el inicio y cierre de cada etapa. No exigir la configuración profunda de protocolos de etapas posteriores para dar por completa arquitectura.
- Distinguir fallo conceptual comprobado, imprecisión y decisión de ingeniería bajo restricción.
- No iniciar lecciones desde OSI ni asignar dominio basado en la presencia de apuntes o en completar una etapa.
- Evaluar con preguntas orales sin pistas, decisiones justificadas, caso de aplicación y repreguntas antes de verificar dominio.

## Etapa II — Iniciada, SIN respuestas (próxima sesión)

**Retomar exactamente en la pregunta 1: “Diseño de subredes”**, sin contestarla por el estudiante y sin avanzar a la etapa III.

1. ¿Cómo organizaría el direccionamiento IPv4 del campus? ¿Reservaría un bloque para cada edificio, para cada departamento o utilizaría otra estrategia?
2. ¿Qué relación establecería entre las VLAN y las subredes IP? ¿Una VLAN necesita necesariamente su propia subred?
3. ¿Cómo incorporaría el crecimiento del 30 % al diseño sin desperdiciar innecesariamente direcciones?
4. ¿Qué función desempeñaría VLSM en su propuesta y por qué lo utilizaría?

**Instrucción original del examinador:** todavía no calcular máscaras ni rangos; primero razonar la estrategia, luego ejercicios de pizarra. Bloque disponible `10.40.0.0/16`.

## Etapas III–VI — Pendientes

- **III:** inter-VLAN, enrutamiento estático/dinámico, OSPF y salida WAN.
- **IV:** STP, redundancia física/lógica, fallas y convergencia.
- **V:** VLAN como control de segmentación, ACL, firewalls, aislamiento invitados, gestión segura.
- **VI:** selección de medios, cableado estructurado, diagnóstico de fallas y pruebas.

No hay respuestas evaluadas en estas etapas. Preguntas incidentales sobre OSPF y VRRP de la etapa I constituyen solo evidencia preliminar.

## Bitácora y continuidad

- **Fecha:** 2026-11-23.
- **Tiempo efectivo:** no medido.
- **Prueba:** diagrama de pizarra aportado por estudiante y defensa oral escrita; no consta uso o no uso de apuntes.
- **Balance:** etapa I completada satisfactoriamente, con resultados parciales y pendientes específicos; etapa II planteada, no respondida.
- **Próxima acción:** primera pregunta de la etapa II, sin soluciones adelantadas.
- **Repaso sugerido:** próxima sesión: recuperación breve de topología y gateway; tras diagnóstico de etapa II, repaso focalizado de imprecisiones de la etapa I; fechas concretas pendientes de programación de próxima sesión.
- **Estado general:** EN_ESTUDIO, sin dominio verificado.
