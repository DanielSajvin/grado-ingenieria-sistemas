**Caso: Simulación o Experimentación en la red de transporte público de la Ciudad de Guatemala**
**Antecedentes del problema**
- La congestión vehicular ha aumentado un 35% en los últimos 5 años, especialmente en horas pico (de 6:00 a 9:00 y de 16:00 a 19:00).
- Se han identificado puntos críticos de embotellamiento en El Trébol, el Obelisco y la conexión del Periférico con la Ruta al Atlántico.
- La falta de carriles exclusivos para buses en ciertas áreas genera demoras de hasta 40 minutos en recorridos que deberían tomar 15.
- Un 70% de los usuarios del transporte público han expresado descontento con los tiempos de espera y la sobrecarga en ciertas estaciones.

**Propuestas para solucionar el problema**
1. Experimentación en el sistema real
	- Implementar un cambio piloto en las rutas y semáforos en ciertos sectores durante un mes y medir el impacto.
	- Modificar la frecuencia de los autobuses en horarios de alta demanda y evaluar si reduce los tiempos de espera.
	- Habilitar carriles exclusivos en ciertos tramos y medir si mejora la velocidad de transporte.

**Desafíos:**
- Si el cambio genera problemas imprevistos, podría afectar a más de 300,000 pasajeros diarios.
- Requiere coordinar con la Policía Municipal de Tránsito (PMT) para hacer ajustes en tiempo real.
- Puede causar resistencia de conductores particulares al reducirse los carriles disponibles.

**2. Simulación mediante modelado computacional**
- Construir un modelo digital del tráfico en la ciudad utilizando datos históricos, sensores viales y estudios de movilidad.
- Simular los posibles efectos de los cambios sin afectar el tránsito real.
- Probar distintos escenarios antes de implementar cambios en la infraestructura.

**Desafíos:**
- Los modelos de simulación pueden no considerar factores impredecibles como fallas mecánicas de buses, bloqueos viales inesperados o accidentes.
- La simulación depende de la precisión de los datos recolectados, y errores en estos pueden llevar a conclusiones equivocadas.
- No permite evaluar la reacción real de los pasajeros y conductores a los cambios.

**Realizar:**
1. Analizar el caso y determinar si es mejor utilizar experimentación en el sistema real o simulación computacional. Justifique su elección con argumentos técnicos, económicos y sociales.
2. Identificar las limitaciones de cada método y proponer estrategias para mitigarlas.
3. Evaluar si una combinación de ambos enfoques podría ser más efectiva y cómo se podría implementar.
4. Considerar el impacto en pasajeros, conductores, la Municipalidad y el sector privado

---
# Resolución

1. **Determinar si es mejor utilizar experimentación en el sistema real o simulación:** el objetivo principal es disminuir la congestión vehicular y esto a la vez mejora los problemas que están teniendo las personas con las largas esperas del transporte y la sobrecarga, ya que si analizamos debido a los atrasos que se llegan a tener los buses también tiene que tomar medidas para ellos cumplir con su trabajo, entonces prácticamente es como una especie de cada; teniendo esto claro entonces, para afectar lo menor posible a la población lo mejor es realizar una simulación. Ya que nos va a permitir evaluar diferentes escenarios que creemos que pueden llegar a solucionar el problema y sin hacer más grave el problema actual. Con la simulación podemos hacer una aplicación con más fundamentos y que a la hora de implementarla ya podremos saber cuáles pueden ser los resultados en el sistema real y así afectando lo menor posible a la población, claro teniendo en cuenta también el ahorro que nos estaríamos haciendo al hacer una simulación y no un experimento que incurriría en gastos económicos y sobre todo el mayor riesgo que existe de que en vez mejorar resulte empeorando la situación. 
2. **Limitaciones de cada método**
	- Simulación: en este caso dependemos mucho de datos históricos y si estos no son correctos nuestra simulación tampoco lo será y por lo tanto nuestra solución de igual manera no será correcta. También teniendo en cuenta que se trata de muchos vehículos lo que se traduce a muchas personas, la cantidad de variables es muy grande, es decir, que habrán factores que dejemos por fuera de la simulación y por lo tanto puede llegar a no ser tan precisa. Una forma para solucionar la parte de los datos es que previamente a la simulación nosotros recolectemos la mayor cantidad de información, por ejemplo con sensores y detectar en que punto existe mayor cantidad de carros en que paradas es donde más se atrasan en llegar los buses la hora, y así la mayor cantidad y estos datos compararlos con los históricos y tratar de sacar un dato lo más real posible. De igual manera haciendo encuestas a las personas de que piensan sobre el problema y ya que ellos son los que experimentan el problema tendrán una visión más clara y de esta forma nos ayudaremos a tener más clara la situación y así tomaremos más factores o variables en cuenta. 
	- Experimentación: realmente es muy arriesgado poner todo en práctica de una vez, el riesgo de fracaso es mayor porque no se tuvo una planificación previa muy amplia y en caso de fallar no solo se habrán gastado recursos económicos si no que se empeora la situación y se estará afectando a 300,000 personas diarias. Para solucionar esto tenemos que tener una mejor planificación y proponer experimentos que no afecten demasiado, como puede ser probar algo en una sola zona y medir el impacto que este tuvo, ya que la ventaja del experimento es que si nos dará resultados más reales y más apegados a la realidad, lo que nos permitirá tomar una decisión más fundamentada a lo real que en la simulación.
3. **Evaluar la combinación de ambos:** considero que esto sería excelente ya que la simulación nos permitiría realizar un experimento más fundamentado y sabiendo ya cuál podría ser el resultado que este tendría a la hora de ponerlo en práctica. Los resultados de este experimento nos sería de gran ayuda a realizar nuevas  simulaciones porque son datos actuales y lo más real, como a su vez nos estaríamos dando cuenta de todos los factores que no tomamos en cuenta y que ahora ya tenemos y así ajustar la simulación para llegar a la solución del problema. 
4. **Considerar el impacto:** lo que se busca es el beneficio para todos, por lo tanto considero que no es centrarse en un problema únicamente, si no que en este caso como lo mencioné al inicio esto es una especie de cadena. Entonces al solucionar el problema principal que es el tráfico como tal, se estarían solucionando los demás. Por ejemplo: en un caso hipotético si se crean nuevos carriles para los buses estos no ocuparán espacio en el carril de carros particulares entonces existen menos vehículos en circulación y por lo tanto se logra despejar un poco más el tráfico, esto a su vez resulta en que los buses circulan de una manera más libre también y llegan a tiempo a las estaciones, por lo tanto los pasajeros esperan menos y lo buses no tiene la necesidad de estar sobrecargando de pasajeros porque realmente podrán cumplir con metas o con lo que ellos tengan como objetivo. Entonces para logran el mayor impacto positivo lo importante es ver la raíz del problema que sería planificar y coordinar de mejor manera a todos los vehículos y de esta forma como consecuencia obtenemos la resolución de los otros problemas. 