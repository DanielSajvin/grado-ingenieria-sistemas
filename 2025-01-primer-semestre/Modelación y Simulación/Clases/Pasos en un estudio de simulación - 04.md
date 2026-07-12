## 01. Definición del problema
- ¿Por qué se estudia el sistema y qué objetivos se persigue con ello?

Se busca transformar una situación confusa e indeterminada, reconocida como problemática, es necesario comprender el sistema a modelar. 

Cómo definir el problema: 
1. Planteamiento del problema
2. Justificación, (por qué, en que afecta)
3. Causas y efectos del problema
4. Objetivo
5. Hipótesis (plantearse una pregunta)
6. Razón del por qué la simulación es la herramienta óptima para el estudio

## 02. Planificación del proyecto
Estima que recursos son necesarios para llevar a cabo el estudio: dinero, personal, hardware de computación, recursos software, etc. Si estos recursos no están disponibles debe replantearse al alcance del estudio. Se estiman los recursos, se hacen las estimaciones de si se tiene lo necesario.

Como parte de la planificación deben considerarse todos aquellos factores que son críticos para el éxito del proyecto, tales como: 
1. ¿Están claramente definidos los objetivos del estudio?
2. ¿Por qué se realiza el estudio?
3. ¿Qué se pretende obtener del estudio?
4. ¿Se dispone de los recursos adecuados y suficientes para poder realizar el estudio: tiempo, personal, software, ordenares, entre otros?
5. ¿Se han identificado los usuarios potenciales o clientes de los resultados del estudio?
## 03. Definición del sistema 
Debe definirse qué aspectos de la realidad constituyen el sistema bajo estudio.
Se tiene que ir a ver como funciona en la realidad, que aspectos de la realidad construyen el sistema.

Se trata de identificar el pequeño conjunto de características o propiedades del sistema eficiente para servir los objetivos específicos del estudio. A grandes rasgos, la metodología para la construcción del modelo podría ser la siguiente: 
Escoger las variables de salida, lo cual resulta relativamente sencillo una vez definido el objetivo del estudio 

Entrada -> Proceso -> Salida
## 04. Formulación conceptual del proyecto 
Desarrollo de un modelo preliminar, ya sea gráficamente (mediante diagrama de bloques) o en pseudocódigo, en el que se definen los componentes, las variables descriptivas y las interacciones (la lógica) que constituyen el modelo del sistema.


La esencia del arte del modelado son la abstracción y la simplificación

- La construcción del modelo se realiza identificando qué componentes del sistema afectan a estas variables de salida y decidiendo, para cada uno de ellos, si debe ser incluido en el modelo o si debe ser 
## 05. Diseño preliminar del experimento 
Consiste en definir que acción se va a ejercer sobre el modelo y cómo se va a medir su comportamiento. Se trata, por tanto, de definir qué variables son las entradas y cuáles las salidas, cómo va a modificarse el valor de las entradas y cómo van a recogerse los datos de la salida. 
- Identificar escenarios que se pueden dar

_Diseño preliminar del experimento_
Consiste en definir qué acción se va a ejercer sobre el modelo y cómo se va a medir su comportamiento. 

_1. Definición de objetivos del experimento_
Especificar claramente qué se espera lograr con la simulación.
Tareas:
1. Identificar las preguntas de investigación que el experimento debe responder 
2. Establecer objetivos específicos y metas medibles para la simulación

_2. Selección de variables de entrada y salida_
¿Qué factores controlarás y qué medirás?
- Variables de entrada, son los factores que puedes ajustar en la simulación. Estos podrían ser configuraciones del sistema, condiciones iniciales o cualquier otro pará metro que influya en el comportamiento del sistema.
- Variables de salida, son los resultados que medirás para evaluar el desempeño del sistema o el impacto de las variables de entrada. 

_03. Diseño de escenarios_
¿Cómo se configurarán las pruebas?
Aquí se decide los diferentes escenarios que se probará durante la simulación. Cada escenario es una combinación específica de valores para las variables de entrada.  (clave de la simulación)

_04. Configuración de parámetro del experimento_
¿Cuánto tiempo durará y cuántas veces se repetirá?
En esta etapa, se define cómo se llevará a cabo la simulación en términos de tiempo y repetición.
- Duración 
- Número de repeticiones 

_05. Métodos de recolección de datos_
Define cómo se registrará los resultados de la simulación y cómo se almacenará para sus análisis posterior

_06. Evaluación de recursos necesarios_
Asegurarse de tener todos los recursos necesarios para realizar la simulación
* Hardware
* Software
* Personal

_07. Pruebas de validación preliminares_
Antes de ejecutar la simulación completa, realizar pruebas preliminares para verificar que todo esté configurado correctamente. 

_08. Documentación del diseño del experimento_
Documentar todos los aspectos del diseño del experimento para asegurar que pueda ser replicado y comprendido por otros.
## 06. Preparación de los datos de entrada
Debe establecerse el procedimiento a seguir para asignar valores a cada una de las variables de entrada durante la simulación.

Su propósito es asegurar que los datos utilizados sean adecuados y estén en el formato correcto para garantizar que los resultados de la simulación sean precisos y significativos. 

1. Recolección de datos, consiste en la obtención de los datos necesarios que se utilizarán en la simulación. 
	- Fuentes, bases de datos, encuestas, sensores, experimentos previos, datos históricos, etc. 
	- Consideraciones, asegurarse de que los datos sean relevantes y actuales para el contexto de la simulación
		- Primera enfocada a los clientes y otra a la parte de gestión (coordinador de cajas, cajeros)
		- Cree que el proceso se vuelve lento debido a (a, b, c, d) las preguntas más difíciles al final
		- Cree que el número de cajeros es suficiente 
		- Qué agregaría usted para mejorar su experiencia a la hora de comprar 
## Traducción del modelo
Consiste en describir las partes del modelo y su funcionamiento empleando un lenguaje de simulación. De este modo ya puede ejecutarse la simulación.

## Verificación y validación
Se trata de estudiar si el modelo opera como debiera y si la salida del modelo es creíble y representativa del comportamiento del sistema.

## Diseño experimental final
En este punto se diseña un experimento que proporcione la información necesaria para poder contestar a las preguntas planteadas en el estudio. Típicamente el experimento consiste en cierto número de réplica
- Probar y probar y seguir probando 

## Experimentación
Realización del experimento de simulación diseñado anteriormente. 

_Experimento:_  Un procedimiento para conocer el comportamiento de los sistemas es la experimentación. Este ha sido el método empleado durante siglos para avanzar en el conocimiento: plantear las preguntas adecuadas acerca del comportamiento de los sistemas y mediante experimentación. Se conoce el comportamiento de un sistema
Se experimenta a la hora de estar realizando pruebas en el desarrollo de software. 
Hasta cierto punto un experimento es una emulación. 
Es un ensayo con todo el contexto real, no es una implementación como tal. 

La experimentación sobre el sistema real puede ser inviable: 
- Es porque el sistema aún no exista físicamente.
- El experimento puede producir perjuicio o incomodidad. 
- El tiempo requerido para la realización del experimento lo hace irrealizable. 
- Algunos experimentos son peligrosos. 
- Se requiere modificar variables que en el sistema real o bien no están accesibles. 
- El elevado costo económico del experimento. 
- 

## Análisis e interpretación
Consiste en inferir conclusiones a partir de los datos obtenidos de la simulación 

## Implementación y documentación
