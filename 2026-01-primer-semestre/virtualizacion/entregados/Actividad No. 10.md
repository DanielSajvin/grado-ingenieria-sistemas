1. **Elección de los dos servidores a migrar**
   - **Expliquen por qué eligieron esos dos, qué los hace más urgentes o más viables.**
	Elegimos los servidores B y C por las siguientes razones:
	   - **Servidor C :** es la prioridad técnica más  importante, porque la empresa tiene una política de respaldo débil (semanal y no probada). Si se virtualiza el punto de respaldo permite utilizar Snapshots y clones, asegurando que tengamos una forma más confiable antes de tocar los servidores de producción.
	- **Servidor B:** debido a la flexibilidad del servidor consideramos que puede permitir reinicios nocturnos, y esto daría el margen de operación necesario para corregir errores de drivers o red sin que se caiga la planta central. Mover este servidor valida la conectividad de las tablets en el entorno virtual.

2. **Tipo de migración para cada uno**
   - **¿En caliente o en frío? ¿Parcial o completa? ¿Manual o automatizada? Justifiquen cada decisión técnica.**
	- **Servidor B: Migración en Caliente**
	    - **Justificación:** Permite copiar los datos mientras el servicio sigue activo. El "downtime" se reduce únicamente al momento del cutover (apagar el físico y encender el virtual) para evitar conflictos de IP.
	- **Servidor C, Migración en Frío.**
	    - **Justificación:** Al ser un servidor de archivos (NFS) y respaldos, la integridad del sistema de archivos es vital. Una migración en frío garantiza que no haya escrituras pendientes durante el proceso, evitando la corrupción de bloques en Linux.

3. **Herramienta a utilizar**
   - **¿VMware Converter, Clonezilla Live, SCVMM u otra? Fundamenten su elección según el caso.**
	**VMware vCenter Converter Standalone**.
	
	- **Fundamentación:** Es la herramienta nativa y gratuita más eficiente para entornos ESXi. Maneja automáticamente la inyección de drivers necesarios para que el OS reconozca el hardware virtual. Además, permite redimensionar los discos durante la migración, algo vital dado el espacio limitado en el clúster actual.

4. **Plan de pasos**
   - **Desde la auditoría hasta la validación final.**
	- **Auditoría y Limpieza:** Eliminación de archivos temporales y desinstalación de software de gestión de hardware físico (ej. HP Insight, Dell OpenManage).
	- **Preparación de Red:** Reserva de las IPs fijas en el switch virtual y configuración de la VLAN correspondiente en el ESXi.
	- **Ejecución de P2V (Servidor B):** Iniciar clonación en caliente al 90%. El 10% final (sincronización) se hará en la ventana de mantenimiento.
	- **Ejecución de P2V (Servidor C):** Apagar servicios NFS, arrancar con el agente de conversión y realizar el clonado completo.
	- **Instalación de VMware Tools:** Tras el primer arranque virtual, instalar las herramientas para optimizar el rendimiento de video, red y ratón.
	- **Pruebas de Aceptación (UAT):** Verificación de conectividad de tablets (Servidor B) y montajes NFS (Servidor C).

5. **Retos críticos y solución**
   - **Identifiquen al menos dos riesgos reales (por ejemplo, pérdida de datos, IP fija, drivers, tiempo de inactividad) y propongan soluciones viables.**
	- **Reto: Incompatibilidad de Drivers (Kernel Panic en CentOS 7).**
	    - **Solución:** Tras la migración, si el servidor no arranca, iniciaremos en _Rescue Mode_ para reconstruir el archivo `initramfs`, asegurando que se carguen los drivers de almacenamiento virtual de VMware.
	- **Reto: Conflicto de IP Fija y Tabla ARP.**
	    - **Solución:** Al realizar el cambio, ejecutaremos un "gratuitous ARP" o reiniciaremos el switch virtual para limpiar la caché de direcciones MAC, asegurando que las tablets encuentren al Servidor B virtual de inmediato.