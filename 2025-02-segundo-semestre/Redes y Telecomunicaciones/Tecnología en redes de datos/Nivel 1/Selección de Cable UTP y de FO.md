Cableado Horizontal, par trenzado, no mayor a 100 mts
Cableado Vertical, fibra óptica, si puede distancia mayor a 100 mts

### Par trenzado 
UPT, FTP, STP
UTP, sin blindaje, a altas velocidades puede tener transferencia (RJ45)
FTP, dispone de una pantalla metálica para mejor transferencias externas 
STP, con blindaje, cada par tiene una pantalla anti transferencias, cable robusto caro y difícil de instalar, para que sea más eficaz se tiene que conectar a tierra física, se utiliza en radio difusoras o grandes motores electricos 
![[Pasted image 20251018215229.png]]

Categorias
CAT 3, hasta 10 Mbps
CAT 5, hasta 100 Mbps, oficinas LAN
CAT 5e, datos hasta 1000 Mbps 
CAT 6, 1 gb por segundo 

![[Pasted image 20251018215445.png]]

## Tipos de Fibras
Fibra multimodo, nucleo de mayor diametro
Fibra monomodo, un solo rayo de luz

Cable interior de fibra optica, menor a 2km 

![[Pasted image 20251018215649.png]]

Jumper optico, cordon de parcheo 
![[Pasted image 20251018215833.png]]


|   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
    
|Host|Departamento|ID de Red|Máscara de Subred|CIDR|Rango Utilizable|Gateway|Broadcast|
|90|Ingeniería y Producción|10.0.0.0|255.255.255.128|/25|10.0.0.1 - 10.0.0.126|10.0.0.1|10.0.0.127|
|80|Software|10.0.0.128|255.255.255.128|/25|10.0.0.129 - 10.0.0.254|10.0.0.129|10.0.0.255|
|70|Energía|10.0.1.0|255.255.255.128|/25|10.0.1.1 - 10.0.1.126|10.0.1.1|10.0.1.127|
|45|Dirección General|10.0.1.128|255.255.255.192|/26|10.0.1.129 - 10.0.1.190|10.0.1.129|10.0.1.191|
|45|Ventas|10.0.1.192|255.255.255.192|/26|10.0.1.193 - 10.0.1.254|10.0.1.193|10.0.1.255|
|40|RRHH y Seguridad|10.0.2.0|255.255.255.192|/26|10.0.2.1- 10.0.2.62|10.0.2.1|10.0.2.63|
|25|Legal y Finanzas|10.0.2.64|255.255.255.224|/27|10.0.2.65 - 10.0.2.94|10.0.2.65|10.0.2.95|