## Modelo OSI

1. **Capa física**, todo lo relacionado con la interconexión de los dispositivos (cables)
2. **Enlace de datos**, es la que hace que se produzca la transferencia de datos entre dos sistemas a través de una red
	1. LLC (control de enlace lógico), su función es convertir la electricidad o el wi-fi en 1 y 0 
	2. MAC (control de acceso al medio), se encarga de mover los paquetes de 1 y 0 desde una interfaz de red hasta otra interfaz de red. 
3. **Capa de red**, se encarga de enrutar los datos. Seleccionar y enviar paquetes de datos a través de la ruta más eficiente. 
	1. _Protocolos_, OSPF (sirve para determinar la ruta más rápida que deben seguir los datos dentro de una red), IP, IPsec, ARP, NAT, ICMP
4. **Capa de transporte**, se coordina todo el tránsito de datos y el intercambio. Si se recibió o no, velocidad y destino. Se define el puerto por donde va a entrar la información 
	1. _Protocolos_, TCP y UDP
5. **Capa de sesión**, establece la "sesión" en donde los sistemas se van a comunicar. Se controla la capacidad de establecer o no una conexión
	1. _Protocolos_, NetBIOS, RPC, PPTP, PAP
6. **Capa de presentación**, encriptado y cifrado de datos. Se encarga de presentar los datos en una especie de formato. 
7. **Capa de aplicación**, se encarga de establecer la comunicación entre la aplicación que el usuario ve y la red. 
	1. _Protocolos_, HTTPs, DNS, FTP, SMTP

## Modelo TCP/IP

---

