## Problemas en redes sin administración centralizada 
- Cada computadora tiene usuarios locales. Las contraseñas se administran en cada equipo
- No existe control centralizado. Los permisos se configuran manualmente 
- No hay políticas de seguridad uniformes 
Esto genera desorden, problemas de seguridad y pérdida de tiempo administrativo 

## ¿Qué es Active Directory?
Es un servicio de directorio desarrollado por Microsoft que permite administrar de forma centralizada todos los recursos de una red. Todo se controla desde un servidor 
Permite gestionar: 
- Usuarios 
- Servidores 
- Políticas de seguridad 
- Computadoras 
- Permisos 
- Acceso a recursos 

## ¿Qué es un controlador de dominio?
Domain Controller, es el servidor que ejecuta Active Directory 
- Autenticar usuarios, valida las credenciales de cada usuario que intenta iniciar sesión
- Autorizar accesos, determina a qué recursos puede acceder cada usuario 
- Administrar políticas de seguridad, aplica reglas de seguridad de forma centralizada 
- Gestionar computadoras, administra todos los equipos dentro de la red 

## ¿Qué es un Dominio?
Es un conjunto de computadoras, usuarios y recursos administrados de forma centralizada
Cuando una computadora entra al dominio: 
- Ya no usa cuentas locales
- Usa cuentas del servidor 
- Hereda políticas de seguridad 

#### ¿Cuál es la diferencia entre usuario local y usuario de dominio?
Usuario local: 
- Solo existe en una computadora 
- No funciona en otros equipos
- No se administra centralmente 

Usuario de dominio: 
- Se crea en el servidor 
- Puede iniciar sesión en cualquier equipo del dominio 
- Puede recibir políticas de seguridad automáticamente 

### ¿Qué objetos administra Active Directory?
Los principales son: 
- Usuarios
- Computadoras 
- Grupos
- Unidades organizativas 
Estos objetos permiten organizar y controlar la red 

### ¿Qué son las unidades organizativas (OU)?
Permiten organizar objetos dentro del dominio. Funcionan como carpetas administrativas. Esto permite aplicar políticas diferentes a cada área

## ¿Qué son las Políticas de Grupo?
Permiten aplicar reglas automáticas a usuarios o computadoras. Estas políticas se conocen como: **_Group Policy (GPO)_**, sirven para controlar el comportamiento de los equipos dentro del dominio. 
Un administrador puede definir reglas como: 
- Longitud mínima de contraseña 
- Bloqueo de cuentas después de varios intentos fallidos 
- Tiempo máximo de sesión
- Prohibir instalación de software 

## ¿Qué es DHCP?
Dynamic Host Configuration Protocol, es un servicio que asigna automáticamente direcciones IP a los dispositivos de una red. 
En una red sin DHCP se tiene que configurar manualmente lo siguiente: 
- Dirección IP
- Máscara de red
- Puerta de enlace
- Servidor DNS

### ¿Qué hace DHCP?
Asigna automáticamente: 
- Dirección IP, identificador único del dispositivo en la red
- Gateway, puerta de salida hacia otras redes 
- Máscara de red, define el rango de la red local
- Servidor DNS, traduce nombres de dominio a direcciones IP

## ¿Cómo funciona DHCP?
1. Solicitud, hace una petición
2. Oferta, el servicio mira cuáles tiene disponibles 
3. Petición, procesa la petición inicial y le dice cuál es la que tiene disponible para el dispositivo que hizo la petición
4. Confirmación, el servidor se la asigna y el dispositivo la acepta 

### ¿Cuál es la relación entre Active Directory y DHCP?
En redes empresariales ambos servicios trabajan juntos.
Active Directory administra: 
- Usuarios 
- Computadoras
- Permisos

DHCP administra: 
- Direcciones IP

