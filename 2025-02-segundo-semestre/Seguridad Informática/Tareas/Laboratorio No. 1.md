
---

## Análisis de Comandos 

| **Comando**                                                | **Herramienta**   | **Función**                                                                  |
| ---------------------------------------------------------- | ----------------- | ---------------------------------------------------------------------------- |
| `record_mic`                                               | Audio             | Graba audio desde el micrófono de la víctima durante un tiempo determinado.  |
| `kill <PID>`                                               | Meterpreter       | Finaliza un proceso activo en la máquina remota (como `chrome.exe`).         |
| `keyscan_start``keyscan_dump``keyscan_stop`                | Keylogger interno | Inicia, muestra y detiene la captura de pulsaciones del teclado.             |
| `ps`                                                       | Meterpreter       | Listar los procesos en ejecución                                             |
| `play`<br>`play /home/kali/Downloads/archivo_de_audio.wav` | Meterpreter       | Reproducir un archivo de audio de forma de onda (.wav) en el sistema destino |
## Algunas capturas de lo logrado

Comando: `ps`

![[Pasted image 20250720173649.png]]
![[Pasted image 20250720173720.png]]

Comando: `keyscan_start``keyscan_dump``keyscan_stop`

![[Pasted image 20250721193457.png]]

## Propuesta de mitigación con base en la norma ISO/IEC 27001

Durante el ataque simulado se logró evidenciar el control remoto total del equipo víctima mediante el uso de payloads de tipo **reverse shell**. Las acciones ejecutadas incluyeron grabación de audio desde el micrófono, registro de pulsaciones del teclado (keylogger), finalización de procesos y reproducción de archivos de audio. Este tipo de invasión o control del equipo claramente compromete la **confidencialidad, integridad y disponibilidad** de los activos de información, permitiendo la recopilación de datos sensibles y el control absoluto del sistema afectado.

El riesgo no solo es técnico, sino también humano, ya que comúnmente se basa en engañar al usuario para que ejecute el archivo malicioso. En entornos reales, esto puede llevar a la pérdida de datos sensibles, interrupciones operativas, daño reputacional y sanciones legales por incumplimiento de normativas de protección de datos.

### Controles del Anexo A de la ISO/IEC 27001:2022

| **Código ISO 27001** | **Nombre del control**                      | **Aplicación en este caso**                                                                                     |
| -------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| A.5.24               | Gestión de vulnerabilidades técnicas        | Realizar escaneos periódicos y pruebas de penetración para identificar y corregir vulnerabilidades explotables. |
| A.6.4                | Controles de acceso                         | Aplicar el principio de mínimo privilegio y segmentación de redes para limitar el alcance de un ataque exitoso. |
| A.5.7                | Capacitación en seguridad de la información | Capacitar al personal para reconocer archivos y comportamientos sospechosos, evitando la ejecución de malware.  |
| A.8.16               | Protección contra software malicioso        | Implementar soluciones antivirus avanzadas con capacidad de análisis de comportamiento y sandboxing.            |
| A.8.23               | Monitoreo de seguridad de la red            | Usar sistemas IDS/IPS y SIEM para detectar conexiones no autorizadas y comportamientos anómalos en tiempo real. |
| A.5.17               | Seguridad de la configuración               | Establecer configuraciones seguras en los sistemas operativos para evitar ejecuciones no autorizadas.           |
| A.8.16               | Restricciones de instalación de software    | Impedir que usuarios no autorizados instalen o ejecuten programas fuera de los aprobados.                       |



