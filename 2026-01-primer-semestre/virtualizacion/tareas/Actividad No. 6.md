## Escenario 1

### **Preguntas:**  
**¿Cómo configurarías la VM?**  
Usaríamos el adaptador de red NAT

**¿Cómo garantizarías que siga funcionando si cambia la red WiFi?** 
Esta crea internamente una red entonces el anfitrión funciona como un router, y la VM accede al WiFi mediante el anfitrión entonces solo hace falta configurar el nuevo WiFi en el anfitrión y la VM se conectaría automáticamente  

**¿Qué problema podría aparecer durante la demostración?**
Si el anfitrión tiene problemas para conectarse a WiFi todas las VM también tendrán problemas

## Escenario 2 

### **Preguntas**
**¿Qué configuración usarías realmente?** 
Usaríamos el adaptador de red, red interna, con configuración extra de NAT para acceder a internet

**¿Qué riesgo técnico exacto tendría usar Bridge?**  
El riesgo de usar puente es el mismo riesgo que se tendría al tener una máquina física real, es decir, que también podría acceder a la red real 

**¿Qué señal indicaría que la configuración es insegura?**
Es el hecho de que se está accediendo a la red real como si fuera otra máquina física

## Escenario 3
### **Preguntas**
**Diseña la red completa (pueden combinar modos de red).**
![[Diagrama en blanco - Página 1 (3).jpeg]]


**Explica por qué una sola configuración no es suficiente.**  
Porque el escenario es muy específico y requiere de varias restricciones que solo una configuración no era suficiente 

**¿Qué error conceptual cometería un estudiante principiante?**
Pensar que una sola configuración es suficiente