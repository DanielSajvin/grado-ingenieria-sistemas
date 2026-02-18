
<hr>

### Parte 1 – Análisis del escenario

1. **¿Cuántos servidores físicos existen actualmente?**
	Actualmente existen 7 servidores físicos, ya que tienen uno para cada servicio, los cuáles son: 
	- Servidor Web
	- Servidor de Base de Datos
    - Servidor de Correo
    - Servidor de Archivos
    - Servidor de Autenticación
    - Servidor de IoT
    - Servidor de Backups

2. **¿Qué problemas genera tener todos los servicios en la misma red?**
	El principal problema es de seguridad, ya que si alguien no autorizado tiene acceso a la red por lo tanto tendrá acceso a todos los servicios, también la parte de segmentación, al estar todo en la misma red se puede dar el caso de que información innecesaria esté llegando a lugares o departamentos que no corresponden, lo cuál hace que la red se sature. En caso de fallos también es está muy mal, porque si falla la red principal y al estar todos los servicios ahí todos van a caer y la empresa se quedará sin nada. 

3. **¿Qué impacto tiene este diseño en términos de escalabilidad?**
	El proceso de dar mantenimiento por ejemplo o querer agregar dispositivos o al querer realizar alguna configuración en la red, esto terminará afectando a todos los servicios y puede que en algunos beneficie pero en otros vaya a afectar, lo ideal es que esté todo segmentado y si algo se quiere hacer crecer sólo se enfoca en esa parte sin tener que afectar a los demás servicios. 
    
4. **¿Qué riesgos de seguridad se identifican?**
	Si se tiene acceso a la red principal se tiene acceso a todos los servicios, en caso de fallos todos los servicios se van a caer. 

### Parte 2 – Propuesta de mejora aplicando virtualización

Se debe:
- Reducir la cantidad de servidores físicos.
- Agrupar servicios de forma lógica.
- Aplicar segmentación mediante VLANs.
- Justificar qué servicios deben estar aislados.

Los servidores de Backups se podrían mantener físicos cómo también el de archivos y base de datos. Pero no que estos sean los principales si no que serían a modo de respaldo únicamente. Después todos los otros e incluyendo estos se pueden virtualizar.



La segmentación mediante VLANs se realiza con el objetivo de segmentar y ya de esta forma se puede organizar de mejor manera, sería una VLAN para cada departamento, también se vería la parte de que VLAN se puede comunicar con otras, ya que existen por ejemplo la VLAN de Recursos Humanos no tendría por qué comunicarse con la de Ventas. 

Los servicios que van a estar aislados serán: Base de datos, autenticación, backups, IoT, Archivos. Esto porque incluyen información sensible o el hecho de que alguien con malas intenciones acceda a ellos si nos puede afectar en gran manera. Un pequeño ejemplo si alguien manipula el servicio de autenticación podría autenticarse a el mismo y así ya tener acceso a nuestro sistema. 

Agrupación de los servidores: 
- Servidor web
- Servidor de correo 
- Servidor de autenticación 

- Servidor de base de datos 
- Servidor de IoT 
 
- Servidor de backups 
- Servidor de archivos

### Parte 3 – Simulación en Cisco Packet Tracer

**Topología Final**
![[Pasted image 20260211125933.png]]

Segmentación por medio de VLANs
![[Pasted image 20260211130023.png]]

### Parte 4 – Validación

Si existe comunicación, el DHCP funciona y el enrutamiento dinámico también
![[Pasted image 20260211130318.png]]

### Parte 5 – Conclusión

1. **¿Cuántos servidores físicos existían al inicio?**
	Al inicio existían 7 servidores físicos 
    
2. **¿Cuántos servidores físicos quedan en la propuesta?**
	Se logró reducir 4 servidores, por lo tanto ya únicamente quedaron 3 servidores físicos
    
3. **¿Qué conceptos de virtualización se aplicaron?**
	En sí la virtualización es el pasar recursos físicos a lógicos, que fue lo que se hizo en esta práctica y también la propiedad que dice que la virtualización ayuda a aprovechar de mejor manera, ya que en un mismo servidor ahora se tienen más de un servicio, a diferencia de cómo se tenía al inicio de que era un servidor para cada servicio, ahora aprovecha de mejor manera el servidor y este aloja más de un servicio a la vez 
    
4. **¿Qué ventajas ofrece el nuevo diseño frente al modelo tradicional?**
	Ya solo con la parte de segmentar por VLANs ofrece la ventaja de seguridad de que si algún servidor es atacado solo van a caer esos servicio y no todos, también que si se accede solo se tiene acceso a eso y hasta ahí llegaría, no se puede acceder a otros servicios. También el enrutamiento dinámico ayuda a la disponibilidad de la red, ya que no si un canal se cae no importa porque busca otro camino y siempre se logra la comunicación. En la parte de escalabilidad ahora es más fácil, ya que los servidores se pueden virtualizar y eso hace que el agregar uno nuevo no sea tan complejo como comprar uno físico, instalarlo y detener operaciones por ejemplo, ya que una de las ventajas que ofrece es que eso se podría realizar en caliente sin afectar a los servicios. 
