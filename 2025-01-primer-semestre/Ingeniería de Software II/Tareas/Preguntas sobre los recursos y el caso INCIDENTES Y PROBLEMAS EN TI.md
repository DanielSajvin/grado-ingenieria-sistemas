<hr>

1. **Pregunta: ¿Cuál es la diferencia fundamental entre un incidente y un problema en el contexto de TI?**
	La diferencia principal es que un incidente es una interrupción puntual del servicio que requiere que se solucione de forma inmediata para restaurar su funcionamiento, mientras que un problema es la causa raíz de uno o varios incidentes. El incidente se enfoca en la respuesta rápida; el problema, en la resolución profunda y permanente, es decir, es más a largo plazo.

2. **Pregunta: En el caso de "Textiles Quetzal", ¿por qué crees que se describe mejor como un problema en lugar de múltiples incidentes aislados?**
	Porque todos los incidentes reportados tienen un patrón común y también se analiza forman como una especie de cadena, el problemas que se presenta por ejemplo: lentitud en servicios de red. Indica que hay una causa raíz compartida, que puede ser en la infraestructura de red o en el servidor, lo cual lo convierte en un problema sistémico más que en varios incidentes independientes.

3. **Pregunta: ¿Qué riesgos implica no abordar la causa raíz de los incidentes recurrentes?**
	- Pérdida de productividad.
	- Frustración de los usuarios y mala reputación tanto para el software como para la empresa.
	- Posible daño a la infraestructura por sobrecarga.
	- Costos ocultos por soluciones temporales, ya que al final es más costos estar a cada rato arreglando algo que solucionar desde la raíz.
	- Riesgo de una falla mayor que afecte toda la operación.

4. **Pregunta: ¿Qué criterios utilizarías para priorizar la investigación y resolución de un problema en TI?**
	- Analizar el verdadero impacto en la operación de la empresa.
	- Número de usuarios afectados.
	- Frecuencia con que ocurre.
	- Estudiar que tan grave es la falla para los usuarios del servicio involucrado.
	- Riesgo de empeorar si no se atiende.
	- Costo estimado de no resolverlo o solo resolverlo de forma reactiva en comparación con resolver el problema desde la raíz.

5. **Pregunta: ¿Qué tipo de herramientas o técnicas podrían utilizarse para diagnosticar la causa de la lentitud en la red de "Textiles Quetzal"?  (en los recursos que se te han proporcionado, cada uno Atlassian e IBM, tiene sus propias herramientas.   Podrías pensar en alguna herramienta o técnica que no sea la de ellos?**
	- Wireshark: para analizar el tráfico de red y detectar cuellos de botella.
	- PRTG Network Monitor: para monitoreo en tiempo real.
	- Ping y tracert: para pruebas básicas de conectividad y latencia.
	- NetFlow o SNMP: para revisar el uso de red por dispositivo.
	- Análisis de logs del servidor: para identificar procesos anómalos o picos de carga.  

6. **Pregunta: ¿Por qué es importante realizar pruebas después de implementar una posible solución a un problema de TI?**
	Para verificar que la solución realmente resuelve el problema, sin introducir nuevos errores. Además, permite validar el rendimiento bajo condiciones reales y medir mejoras objetivas. Entonces básicamente para ver que si se solucionó el problema y no afectó otras partes del software.

7. **Pregunta: ¿Qué rol juega la comunicación con los usuarios durante la gestión de un problema como el de "Textiles Quetzal"?**
	- Mantener a los usuarios informados para tratar reducir  su frustración.
	- Obtener retroalimentación útil sobre cuándo y cómo se presenta el problema.
	- Validar si la solución fue efectiva desde su perspectiva.
	- Generar confianza en el área de TI.

8. **Pregunta: ¿Podrías mencionar alguna acción proactiva que el departamento de TI de "Textiles Quetzal" podría haber tomado para prevenir este tipo de problemas?**
	- Implementar monitoreo preventivo del tráfico y recursos del servidor.
	- Realizar mantenimiento periódico de la infraestructura.
	- Documentar y analizar incidentes anteriores para identificar patrones y que la solución futura sea más fácil.
	- Capacitar al personal en el uso eficiente de los recursos tecnológicos.

9. **Pregunta: ¿Cómo se puede documentar el proceso de resolución de un problema para futuras referencias y para el aprendizaje del equipo de TI?**
	- Se puede crear una especie de informe técnico con:
	    - Fecha y descripción del problema.
	    - Incidentes relacionados.
	    - Pasos realizados para diagnosticar.
	    - Solución aplicada.
	    - Resultados de pruebas posteriores.
	    - Lecciones aprendidas.
	- Guardar en una base de conocimientos interna accesible al equipo.

10. **Realiza una síntesis de los recursos que se proporcionan en el portal.  ¿Podrías agregar algo más interesante que tengas en otra fuente?**
	Los recursos explican que un incidente es un evento que afecta un servicio y requiere respuesta rápida, mientras que un problema es la causa subyacente (que es un problema más profundo y tiene un raíz a la cuál se debe atacar) que debe analizarse y corregirse para evitar recurrencias. Ambos conceptos son fundamentales para mantener la continuidad operativa y mejorar los servicios de TI.
	
	Aporte adicional:  
	Según Microsoft Docs y Cisco, una práctica muy útil es usar el enfoque de “Root Cause Analysis” (RCA) con técnicas como el diagrama de Ishikawa (causa-efecto) o los 5 Porqués, para identificar la causa real del problema, y no solo sus síntomas. Esto mejora la eficacia de las soluciones aplicadas y permite un aprendizaje organizacional más sólido.