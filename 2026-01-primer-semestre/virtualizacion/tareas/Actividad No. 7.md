**NAT**
Configure ambas máquinas virtuales en modo NAT.
Responda:
- Qué dirección IP obtiene Windows y cuál Linux.
    IP en Windows: 192.168.142.129
    IP en Linux: 192.168.142.130
    ![[Pasted image 20260225123517.png]]

![[Pasted image 20260225123630.png]]

- Ambos sistemas tienen acceso a Internet. Demuéstrelo.
	Ubuntu: 
	![[Pasted image 20260225123820.png]]

	Windows: 
	![[Pasted image 20260225123937.png]]

- Windows puede comunicarse directamente con Linux. Explique.
	![[Pasted image 20260225124231.png]]

	![[Pasted image 20260225124305.png]]
	
- Linux puede comunicarse directamente con Windows. Explique.
    ![[Pasted image 20260225125008.png]]

	![[Pasted image 20260225125057.png]]
	
- Qué tipo de conexión representa este modo en un entorno real.
	Podría ser una Vlan pero también sería solo con un switch, porque no se puede salir a otra red

**Bridge Adapter**
Configure ambas máquinas en Bridge Adapter.
Responda:

- Qué IP obtiene Windows y qué IP obtiene Linux.
	IP Máquina Anfitrión:  192.168.0.4
	IP Linux: 10.125.207.226
	IP Windows: 
	
	![[Pasted image 20260225213832.png]]

	![[Pasted image 20260225213856.png]]

- Las direcciones pertenecen al mismo rango de la red real.
	Aquí se puede ver la IP de la red real, y si nos damos cuenta las virtuales también están en la misma red porque son reconocidos como equipos físicos en la misma red, por lo que sí están en el rango real
	![[Pasted image 20260225213954.png]]
    
- Windows puede comunicarse con Linux. Demuéstrelo.
	![[Pasted image 20260225214204.png]]

	![[Pasted image 20260225214229.png]]
	
- Desde otra computadora de la red sería posible ver estas máquinas virtuales. Explique.
	Si se podrían ver, ya que al final la red reconoce cada máquina virtual como un equipo real o físico, entonces es como otro equipo más en la red
    
- Por qué este modo hace que la máquina virtual funcione como un equipo físico.
	Lo que pasa es que VMware crea una dirección MAC virtual para cada máquina virtual, y la tarjeta de red de la máquina anfitrión crea un puente entre la máquina virtual y el router en este caso del ISP y cómo tiene otra MAC el router cree que es un equipo físico más y lo trata como un dispositivo nuevo y real. 

**Internal Network (IP manual obligatoria)**
Configure ambas máquinas en Internal Network con el mismo nombre de red.  
Configure direcciones IP manuales en ambas máquinas.

Responda:
- Qué dirección IP configuró en Windows y cuál en Linux.
	IP Windows: 192.168.50.10
	IP Ubuntu: 192.168.50.20
	![[Pasted image 20260225224547.png]]

	![[Pasted image 20260225224722.png]]
- Pueden comunicarse entre sí. Demuéstrelo.
	![[Pasted image 20260225224827.png]]
	![[Pasted image 20260225225050.png]]
- Tienen acceso a Internet. Explique por qué.
	No se tiene acceso a internet porque lo que se creo fue una red internar totalmente independiente de la red principal, adicional a esto lo que hace VMware internamente es crear un switch virtual que conecta la máquina virtual de Windows con la de Ubuntu, y este es switch virtual es de capa dos por lo que no puede "salir" a otra red por lo tanto no puede salir a internet
- Puede la computadora física comunicarse con ellas. Justifique.
	No porque estas máquinas virtuales están en una red privada es decir otra red distinta a donde se encuentra la computadora física 
- Qué ocurre si una de las máquinas tiene IP en otra subred diferente.
	Pierden la comunicación porque a pesar de estar conectados al mismo cable virtual si tienen dirección IP diferente no se pueden comunicar

**Host-Only Adapter**
Configure ambas máquinas en Host-Only Adapter.
Responda:
- Qué IP obtiene cada sistema.
	IP Windows: 192.168.12.129
	IP Ubuntu: 192.168.12.128
	![[Pasted image 20260226122745.png]]

	![[Pasted image 20260226122801.png]]
	
- Windows puede comunicarse con la computadora física. Demuéstrelo.
	IP máquina física: 192.168.12.1
	![[Pasted image 20260226122939.png]]

	![[Pasted image 20260226123028.png]]
	
- Linux puede comunicarse con la computadora física.

	![[Pasted image 20260226123105.png]]
	
- Windows y Linux pueden comunicarse entre sí.

	![[Pasted image 20260226123153.png]]

	![[Pasted image 20260226123240.png]]
- Por qué este modo puede ser útil para pruebas controladas.
	Una de las ventajas es que acá "se está incluyendo" también a la máquina anfitrión entonces si tenemos recursos que necesitamos utilizar como una base de datos por ejemplo, también la podremos acceder desde las máquinas virtuales, también nos permitiría ver si servicios o servidores de DHCP o Active Directory funciona y sin afectar a la red principal 

**Reto de complejidad**
Configure dos adaptadores en la máquina Linux:
- Adaptador 1 en Internal Network (misma red usada antes)
- Adaptador 2 en NAT

La máquina Windows debe permanecer solo en Internal Network.

Responda:
- Linux tiene ahora acceso a Internet. Demuéstrelo.
	![[Pasted image 20260226124847.png]]
	
- Linux puede comunicarse con Windows.
	![[Pasted image 20260226124929.png]]

	![[Pasted image 20260226125001.png]]
	
- Por qué Linux puede tener Internet y Windows no. Explique.
	Lo que pasa es que Windows está virtualmente conectado al switch virtual de capa 2 que crea VMware, Ubuntu también está conectado a este porque ambos están en una LAN, pero Ubuntu también está conectado por medio de NAT al router virtual de VMware, entonces la NAT es la que se encarga de traducir las peticiones y así es como también por medio de anfitrión logra salir a internet 
- Qué función cumple cada adaptador en Linux dentro de este escenario.
	El adaptador que está en LAN cumple la función de comunicar todos los dispositivos que se encuentren dentro de esa misma LAN
	Ahora el NAT, es como el enlace de salida que le permite comunicarse con internet por medio del anfitrión 
- Este esquema se parece a qué tipo de equipo real (PC común, router/gateway o servidor aislado). Explique su elección.
	Se parece a un router/gateway ya que en Linux al tener dos adaptadores de red uno en LAN donde se comunica con Windows y otro en NAT donde tiene salida a internet tiene la posibilidad de enrutar o dirigir información o paquetes de una red a otra, en este caso sería que si Windows quisiera algo de internet lo haría a través de Ubuntu, es decir, Windows entregaría la petición a Ubuntu y este la procesa y le devuelve el resultado 
