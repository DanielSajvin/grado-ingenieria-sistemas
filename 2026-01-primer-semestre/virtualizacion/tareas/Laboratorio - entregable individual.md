***Explicación técnica:***  
- **Qué configuró**
	Se configuró una GPO, que para mayor facilidad se creo una lista blanca. En lugar de intentar bloquear aplicaciones maliciosas una por una, se estableció una regla global que prohíbe la ejecución de absolutamente cualquier programa en el equipo, permitiendo ejecutar solo los programas que se hayan agregado a la lista blanca explícitamente o que se encuentren en directorios seguros o que se hayan especificado también 
- **Cómo lo implementó**
	La GPO se aplico a una unidad organizativa dónde nos encontramos todos, esto de la siguiente manera:
	- Se creó un GPO y se vinculó a la Unidad Organizativa (OU) objetivo.
	- Dentro del editor de GPO, en la ruta **Configuración del equipo > Configuración de seguridad**, se inicializaron las Directivas de restricción de software.
	- En la carpeta de _Niveles de seguridad_, se cambió el nivel predeterminado del sistema operativo a No permitido.
	- En _Reglas adicionales_, se utilizaron las reglas de ruta (Path Rules) para permitir la ejecución "No restringida" de los programas ubicados en `C:\Windows` y `C:\Program Files`. Esto asegura que el sistema operativo y el software corporativo preinstalado sigan funcionando, mientras que cualquier otra ubicación queda bloqueada.
- **Qué riesgo mitiga**
	Esta GPO realmente es muy agresiva pero ayuda a prevenir varios problemas de seguridad, por ejemplo: 
	- Si un empleado es víctima de _phishing_ y descarga accidentalmente un virus o un script malicioso en su carpeta de Descargas, el sistema bloqueará su ejecución automáticamente porque esas rutas no pertenecen a la lista blanca.
	- Impide que los usuarios descarguen y ejecuten programas que no han sido auditados por el departamento de Sistemas, protegiendo el ancho de banda y la integridad legal de la empresa.
	- Dado que la política bloquea todo lo desconocido por defecto, protege a los equipos contra amenazas completamente nuevas que los antivirus tradicionales aún no tienen en sus bases de datos.