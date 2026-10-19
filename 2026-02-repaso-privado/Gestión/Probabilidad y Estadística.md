La estadística es la ciencia encargada de recolectar, organizar, resumir, analizar e interpretar datos para la toma de decisiones racionales bajo condiciones de incertidumbre. 

**Población (N)**
Conjunto total y exhaustivo de todos los elementos, individuos, transacciones, mediciones o unidades de análisis que comparten una característica observable común bien delimitada en el espacio y en el tiempo. 

**Muestra (n)**
Subconjunto representativo seleccionado a partir de la población objetiva. Debe conservar, a escala menor, la variabilidad y estructura de la población para que las conclusiones sean generalizables. Se trabaja con muestra por limitaciones de tiempo, costo económico de evaluación exhaustiva, pruebas destructivas o inaccesibilidad de la población completa. 

**Estadística Descriptiva**
Métodos y técnicas orientados exclusivamente a organizar, tabular, graficar y resumir las propiedades numéricas de un conjunto de datos recopilados, sin emitir generalizaciones más allá de los datos observados. Describe lo que ocurrió. 
Ejemplo: calcular el tiempo promedio de entrega de sprints en Jira durante el último trimestre y graficar el porcentaje de retrasos. 

**Estadística Inferencial**
Métodos que permiten extraer conclusiones, estimaciones o pronósticos sobre una población total a partir del análisis de una muestra, cuantificando el grado de incertidumbre o probabilidad de error en dicha generalización. Ejemplo: estimar el costo promedio por ticket de soporte para el próximo año con un intervalo de confianza del 95%, basándose únicamente en una muestra aleatoria de los últimos 6 meses. 

**Parámetro**
Describe a la población. Se calcula usando toda la población, suele ser desconocido o difícil de obtener, es un valor fijo y constante (siempre que la población no cambie).

**Estadístico**
Describe a la estadística o emplea la muestra. Se calcula usando una muestra, es conocido y fácil de calcular, es una variable aleatoria (cambia según la muestra que se use en ese momento). 

Para entenderlo mejor: en la estadística inferencial se utilizan los estadísticos para estimar o aproximarse a los parámetros. Como es casi imposible encuestar o medir a toda una población, calculamos el estadístico de una buena muestra y aplicando fórmulas de margen de error, se estima el valor real del parámetro. 

**Variables**
Una variable es cualquier característica, cualidad o magnitud observable en las unidades de estudio que pueden asumir diferentes valores. Por su naturaleza existen dos tipos de variables: 
- **Cualitativas (Categóricas)**, registran atributos, cualidades o categorías no numéricas. 
- **Cuantitativas (Numéricas)**, registran mediciones numéricas donde las distancias y operaciones aritméticas tienen significado. 
	- **Discretas**, surgen de procesos de conteo. Solo toman valores enteros aislados dentro de un rango (no admite valores intermedios). Por ejemplo: número de defectos por módulo de software (0, 1, 2, ...), cantidad de servidores caídos en un mes. 
		- _Pensar en cosas que no se pueden partir a la mitad. Cosas en las cuáles no se pueden tener un valor intermedio_.
	- **Continuas**, surgen de procesos de medición. Pueden tomar infinitos valores dentro de un intervalo continuo de número reales (dependen de la precisión del instrumento). Ejemplo: tiempo de ejecución de una consulta SQL en milisegundos (14,32 ms), presupuesto devengado en un proyecto. 
		- _Entre dos números cualesquiera (por ejemplo, entre 1 y 2), siempre existe la posibilidad de encontrar otro valor intermedio si el instrumento de medición es lo suficientemente preciso._