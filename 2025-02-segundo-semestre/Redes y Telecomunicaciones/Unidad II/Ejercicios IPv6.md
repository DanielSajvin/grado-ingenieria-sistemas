
---

**Ejercicio 1:** Convierte a formato corto y luego comprimido
**Dirección completa:** 2001:0db8:0000:0000:0000:ff00:0042:8329
- **Corto:** `2001:db8:0:0:0:ff00:42:8329`  
    (Se quitaron ceros a la izquierda en `0db8→db8`, `0042→42`, y `0000→0`)
- **Comprimido:** `2001:db8::ff00:42:8329`  
    (La racha más larga de ceros es `0:0:0` ⇒ `::`)

**Ejercicio 2:** Convierte a formato corto y luego comprimido
**Dirección completa:** fe80:0000:0000:0000:0211:22ff:fe33:4455
- **Corto:** `fe80:0:0:0:211:22ff:fe33:4455`
- **Comprimido:** `fe80::211:22ff:fe33:4455`  
    (Se comprimen los tres `0` consecutivos después de `fe80`)

**Ejercicio 3:** Convierte a formato corto y luego comprimido
**Dirección completa:** 2001:0000:0000:abcd:0000:0000:0000:0001
- **Corto:** `2001:0:0:abcd:0:0:0:1`
- **Comprimido:** `2001:0:0:abcd::1`  
    (Hay dos rachas de ceros: `0:0` y `0:0:0`. Se comprime la más larga `0:0:0` entre `abcd` y `1`)
    
**Ejercicio 4:** Convierte a formato corto y luego comprimido
**Dirección completa:** 0000:0000:0000:0000:0000:0000:0000:0001
- **Corto:** `0:0:0:0:0:0:0:1`
- **Comprimido:** `::1`  
    (Siete hextetos `0` al inicio se comprimen en `::`)

**Ejercicio 5:** Convierte a formato corto y luego comprimido
**Dirección completa:** 2002:0a00:0100:0020:000b:0c0d:000e:00f0
- **Corto:** `2002:a00:100:20:b:c0d:e:f0`  
    (`0a00→a00`, `0100→100`, `0020→20`, `000b→b`, `0c0d→c0d`, `000e→e`, `00f0→f0`.)
- **Comprimido:** `2002:a00:100:20:b:c0d:e:f0`  
    (No hay hextetos `0` consecutivos; queda igual al corto)