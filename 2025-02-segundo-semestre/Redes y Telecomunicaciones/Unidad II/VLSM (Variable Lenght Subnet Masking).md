1. Ordenar las subredes de mayor a menor
2. Modificar la máscara de subred, dependiendo de la cantidad de host 
3. Tomar en cuenta las dos direcciones reservadas 

**Ejemplo**

_192.168.0.0/24_
- 2 subredes para 20 host
- 1 subred para 80 host
- 2 subredes para 2 host


| Host | Máscara | Dirección de Red | Broadcast | Rangos Utilizables |
| ---- | ------- | ---------------- | --------- | ------------------ |
| 80   |         |                  |           |                    |
| 20   |         |                  |           |                    |
| 200  |         |                  |           |                    |
| 2    |         |                  |           |                    |
| 2    |         |                  |           |                    |

