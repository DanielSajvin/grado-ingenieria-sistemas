Se usa el dataset `datos_limpios_refugio.csv` que tiene las siguientes columnas:
- `fecha_hora` (cuándo salió el animal)
- `tipo_resultado` (Adoption, Transfer, Euthanasia, etc.)
- `tipo_animal` (Dog, Cat, Bird, Other)
- `raza` varias razas
- `color` varios colores
- `edad_en_dias` (un número)
- `esterilizado` (Si, No, Desconocido)
- `sexo` (Macho, Hembra, Desconocido)

## Elementos que se tienen que agregar
### 1. Segmentación de Datos (Filtros Interactivos)
Filtros principales que servirán para explorar el dashboard
- Tipo de Gráfica: Segmentación de datos (Slicer)
- Columnas:
    - `tipo_animal` (para filtrar entre Perros, Gatos, etc.)
    - `esterilizado` (para ver el efecto de la esterilización)
    - `sexo` (para comparar Machos vs. Hembras)

### 2. Indicadores Clave (KPIs)
Tipo cards con los números más grandes e importantes.
- Tipo de Gráfica: Tarjeta (Card)
- Visual 1: Total de Animales
    - Columna: `tipo_animal` (y en el campo, selecciona "Recuento" o "Count").
- Visual 2: Total de Adopciones
    - Columna: `tipo_resultado` (y en el campo, selecciona "Recuento").
    - Filtro (a nivel de visual): un filtro _a esta tarjeta_ para mostrar solo donde `tipo_resultado` es "Adoption".
- Visual 3: Edad Promedio (en días)
    - Columna: `edad_en_dias` (y en el campo, selecciona "Promedio" o "Average").

### 3. Gráficas Principales (El "Qué" y "Quién")
#### Gráfica A: ¿Cuál es el destino de los animales?
- Tipo de Gráfica: Gráfico de anillos o pie (Donut Chart)
- Propósito: Mostrar el porcentaje de cada resultado (Adopción, Transferencia, etc.)
- Columnas:
    - Leyenda (Legend): `tipo_resultado`
    - Valores (Values): `tipo_resultado` (con "Recuento")
#### Gráfica B: ¿El resultado depende del tipo de animal?
- Tipo de Gráfica: Gráfico de barras 100% apiladas (100% Stacked Bar Chart)
- Propósito: Comparar la _proporción_ de resultados entre Perros, Gatos y Otros.
- Columnas:
    - Eje (Axis): `tipo_animal`
    - Leyenda (Legend): `tipo_resultado`
    - Valores (Values): `tipo_resultado` (con "Recuento")
#### Gráfica C: ¿Cómo afecta la edad a los resultados?
- Tipo de Gráfica: Gráfico de barras (Bar Chart)
- Propósito: Ver cuántos animales hay en cada rango de edad.
- Columnas:
    - Eje (Axis): `edad_en_dias`. a la hora de agregar en teoría debería automáticamente sugerir "agrupar" esto. Se agrupa y crea "bins" o grupos de edad (ej. 0-100 días, 100-200, etc.).
	    - IMPORTANTE, para esto basarse en los bins que se crearon en el modelo de predicción
    - Valores (Values): `tipo_resultado` (con "Recuento")
- Crear la columna `categoria_edad` que está en el modelo de predicción (Cachorro, Joven, Adulto, Senior) y usar esa columna en el eje.

### 4. Gráficas de Detalle (El "Cuándo" y "Cómo")

#### Gráfica D: ¿Cuáles son las razas más comunes?
- Tipo de Gráfica: Gráfico de barras horizontales (Bar Chart)
- Propósito: Mostrar las razas más frecuentes en el refugio.
- Columnas:
    - Eje (Axis): `raza`
    - Valores (Values): `raza` (con "Recuento")    
- IMPORTANTE En el panel de "Filtros" de esta gráfica, tiene la opción de "Top N" y se tiene que poner "Top 10" para el de `raza`, esto porque si no va a intentar mostrar las miles de razas que existen.
#### Gráfica E: ¿Cómo han evolucionado los resultados a lo largo del tiempo?
- Tipo de Gráfica: Gráfico de líneas (Line Chart)
- Propósito: Ver tendencias de adopción, transferencias, etc., por año o mes.
- Columnas:
    - Eje (Axis): `fecha_hora` (Power BI creará automáticamente una jerarquía de Año, Trimestre, Mes. Usa "Año" y "Mes").
    - Leyenda (Legend): `tipo_resultado`
    - Valores (Values): `tipo_resultado` (con "Recuento")