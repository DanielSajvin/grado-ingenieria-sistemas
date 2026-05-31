## 1. Payload

**Qué es:** El _payload_ es la carga útil: el código o programa que hace la acción maliciosa cuando entra en un sistema.  
**Analogía:** como el contenido dentro de una caja — la caja (archivo) puede parecer inofensiva, pero lo que trae dentro es lo que realmente hace algo.  
**En tu taller:** el APK/.exe que, al abrirse, activa la cámara o teclado.  
**Defensa:** no ejecutar archivos desconocidos; usar antivirus/MDM y aplicar políticas de permisos.

---

## 2. Exploit

**Qué es:** Es un método o “truco” que aprovecha una falla en software para ejecutar código no deseado (por ejemplo, el payload).  
**Analogía:** una llave falsificada que abre una cerradura con una imperfección.  
**En tu taller:** el mecanismo que permite que el payload se ejecute en Android o Windows.  
**Defensa:** parches/actualizaciones, WAF, configuración segura.

---

## 3. Vulnerabilidad

**Qué es:** Una debilidad en un software, sistema o configuración que puede ser explotada.  
**Analogía:** una ventana sin seguro en una casa.  
**Defensa:** escaneo de vulnerabilidades, parcheo, revisión de configuraciones.

---

## 4. BeEF (Browser Exploitation Framework) — concepto general

**Qué es:** Herramienta para probar y explotar vulnerabilidades del navegador aprovechando que la víctima visita una página. Permite ejecutar módulos contra navegadores “hookeados”.  
**Analogía:** imaginar que al entrar a una sala te colocan un pequeño micrófono para luego poder hacer acciones remotas sobre lo que ves/escuchas.  
**Defensa:** actualizar navegadores, deshabilitar plugins innecesarios, políticas de contenido (CSP), bloqueo de scripts de terceros.

---

## 5. “Hooked domain” / navegador hookeado

**Qué es:** Cuando un navegador de la víctima queda “conectado” al servidor del atacante (hook), permitiendo enviar comandos al navegador.  
**Analogía:** como tener una sesión abierta en la que el anfitrión puede controlar algunas cosas en tu pantalla.  
**Defensa:** bloquear scripts, evitar abrir enlaces desconocidos, extensiones que bloquean conexiones externas.

---

## 6. Create Alert/Prompt Dialog / Redirect / iFrame Redirect

**Qué es:** Módulos que muestran ventanas emergentes (alert/prompt) o redirigen el usuario a otra página (redirigir, redirigir dentro de un iFrame).  
**Analogía:** pop-ups o “puertas” que te empujan a otro cuarto sin que lo esperes.  
**Defensa:** bloqueadores de pop-ups, políticas CSP, navegación segura.

---

## 7. Social Engineering (Ingeniería social) / Pretty Theft (módulo de BeEF)

**Qué es:** Técnicas para engañar a personas para que revelen información o realicen acciones; _Pretty Theft_ es un módulo que simula páginas/formularios para robar credenciales de forma atractiva.  
**Analogía:** alguien que se hace pasar por empleado del banco para convencerte de darle tu contraseña.  
**Defensa:** formación/concienciación, verificar URL, autenticación multifactor (MFA).

---

## 8. Phishing

**Qué es:** Ataque que utiliza mensajes (correo, web, SMS) para convencer a una persona de ejecutar una acción dañina o compartir credenciales.  
**Analogía:** una carta falsa que parece venir de tu banco pidiéndote que confirmes tu cuenta.  
**Defensa:** filtrar correos, revisar remitentes/URL, MFA, educación.

---

## 9. HTTP vs HTTPS

**Qué es:** _HTTP_ es el protocolo para cargar páginas; _HTTPS_ es HTTP cifrado (seguro) usando TLS.  
**Analogía:** HTTP = postal abierta; HTTPS = carta sellada y con sobre difícil de abrir sin romperlo.  
**Por qué importa:** BeEF y ataques por navegador suelen aprovechar contenido servido vía HTTP o scripts inseguros.  
**Defensa:** exigir HTTPS, HSTS, evitar mezclar contenido inseguro.

---

## 10. APK (Android Package)

**Qué es:** Archivo instalable de apps Android. Puede contener código legítimo o malicioso.  
**Analogía:** un instalador .msi/.exe pero para Android.  
**Defensa:** instalar solo desde fuentes confiables, revisar permisos, usar Play Protect o soluciones EDR móviles.

---

## 11. .exe (ejecutable de Windows)

**Qué es:** Archivo ejecutable en Windows. Puede contener malware (RATs, keyloggers).  
**Analogía:** programa que, al abrirlo, ejecuta instrucciones en la máquina.  
**Defensa:** firmas digitales, políticas de ejecución (AppLocker), antivirus/EDR.

---

## 12. msfvenom / Metasploit (concepto)

**Qué es:** Herramienta para generar payloads/metasploit modules destinados a pruebas de penetración — genera archivos que pueden otorgar acceso remoto.  
**Analogía:** kit de herramientas que crea la caja con la “herramienta” interna (payload).  
**Nota ética:** uso permitido para pruebas autorizadas y educativas únicamente.  
**Defensa:** detección basada en comportamiento, reglas de firewall, EDR.

---

## 13. RAT (Remote Access Trojan) / Control remoto

**Qué es:** Software que otorga control remoto completo del dispositivo a quien lo controla.  
**Analogía:** un control remoto que permite manejar la TV, cámara y micrófono de otra persona.  
**Defensa:** monitoreo de procesos, permisos, bloqueo de conexiones salientes no autorizadas.

---

## 14. Keylogger (captura del teclado)

**Qué es:** Programa que registra las teclas que una persona pulsa — usado para robar contraseñas.  
**Analogía:** alguien tomando notas de todo lo que escribes en tu teclado.  
**Defensa:** usar autenticación sin contraseña (MFA), EDR, revisiones de integridad.

---

## 15. Acceso a cámara/micrófono y grabación de sonido

**Qué es:** El payload puede intentar encender la cámara o micrófono para espiar. En móviles depende de permisos y vulnerabilidades.  
**Analogía:** alguien encendiendo una cámara oculta en tu habitación.  
**Defensa:** controlar permisos, indicator lights, denegar permisos persistentes, actualizaciones.

---

## 16. Reverse shell / Listener / LHOST LPORT (concepto)

**Qué es:** Técnica donde la máquina víctima inicia la conexión hacia el atacante (reverse shell), que está escuchando (listener). LHOST/LPORT son la IP/puerto donde escucha el atacante.  
**Analogía:** en vez de que el ladrón entre en la casa, la casa llama al ladrón y le abre la puerta.  
**Defensa:** monitorizar conexiones salientes inusuales, Firewall, egress filtering (bloquear puertos).

---

## 17. Cross-Site Scripting (XSS) — breve

**Qué es:** Inyección de código (JavaScript) en páginas web que afecta a los visitantes. BeEF suele aprovechar XSS para “hookear” navegadores.  
**Analogía:** alguien pega una nota maliciosa en un libro de la biblioteca que, al leerla, te obliga a hacer algo.  
**Defensa:** sanitizar entradas, Content Security Policy (CSP), validación del lado servidor.

---

## 18. Clickjacking / iFrame attacks

**Qué es:** Técnica para engañar a un usuario para que haga clic en un elemento oculto dentro de un iFrame o superposición.  
**Analogía:** poner un botón peligroso encima de uno inofensivo; tú crees que pulsas "Aceptar" pero en realidad pulsas otra cosa.  
**Defensa:** X-Frame-Options, frame-ancestors en CSP, UI hardening.

---

## 19. Escalada de privilegios (privilege escalation)

**Qué es:** Cuando un atacante consigue subir sus permisos para realizar más acciones (ej. usuario → administrador).  
**Analogía:** entrar a una cuenta básica y luego “robar” el pase VIP.  
**Defensa:** principio de mínimo privilegio, parches, monitorización.

---

## 20. Objetivo y ética de la ciberseguridad

**Qué es:** La ciberseguridad protege confidencialidad, integridad y disponibilidad (CIA). La ética obliga a realizar pruebas solo en entornos autorizados y consensuados.  
**Analogía:** seguridad es como protección de una casa: no rompes la casa del vecino para probar una cerradura sin permiso.  
**Defensa/Práctica:** autorización por escrito, entorno aislado (lab), registros y responsabilidad.

---

## 21. Honeypot / Entorno controlado (laboratorio)

**Qué es:** Un entorno intencionalmente inseguro o aislado usado para aprender o atrapar ataques sin riesgo a sistemas reales.  
**Analogía:** una sala de prácticas donde todo está controlado para no dañar la casa real.  
**Recomendación:** siempre realiza las demostraciones en VM/LAN aislada y con permisos formales.

---

## 22. Mitigaciones generales rápidas (lista para presentar)

- Mantener sistemas y navegadores actualizados.
    
- Usar HTTPS y políticas CSP/HSTS.
    
- Formación en phishing e ingeniería social.
    
- Autenticación multifactor (MFA).
    
- EDR/antivirus y filtrado de tráfico saliente.
    
- Políticas de permisos en móviles (revisar y denegar permisos innecesarios).
    
- Aislar tu laboratorio y no exponerlo a Internet público sin protección.