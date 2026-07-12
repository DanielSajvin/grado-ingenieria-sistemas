Analice los recursos cargados:

Abra las herramientas de desarrollo del navegador (Ctrl + Shift + I o Cmd + Option + I) y diríjase a la pestaña Network.

Recargue la página y observe los recursos que se cargan.

## 1. Identifique el archivo HTML principal, las hojas de estilo CSS, los archivos JavaScript y otros recursos (imágenes, fuentes, etc.).
Anote cuáles de estos recursos presentan los tiempos de carga más elevados.

HTML principal
![[Pasted image 20250121111357.png]]

Archivos JavaScript
![[Pasted image 20250121111453.png]]

Imágenes 
![[Pasted image 20250121111533.png]]

Archivos CSS
![[Pasted image 20250121111611.png]]

Lo que más tardó tiempo en cargar fueron los archivos CSS, el que tardó más tuvo un tiempo de 157ms.

## 2. Inspeccione el DOM y los estilos:

Diríjase a la pestaña Elements y examine el DOM generado por el navegador.
![[Pasted image 20250121112359.png]]

Seleccione un elemento de la página y observe qué estilos CSS están aplicados.
![[Pasted image 20250121112543.png]]

Modifique temporalmente uno de los estilos y describa cómo afecta el diseño visual de la página.
![[Pasted image 20250121113026.png]]
Cambié el color de fondo para que sea más visible, entonces logré identificar que puedo ir seleccionando con el mouse lo que quiero cambiar y de esa forma ubicar el código y así poder realizar algún cambio.

## 3. Investigue el proceso de renderizado:

Abra la pestaña Performance y registre el proceso de carga de la página.
![[Pasted image 20250121113433.png]]

![[Pasted image 20250121113733.png]]

## Opcional: Explore el rendering visual:

(Si está disponible) Active la pestaña Rendering en las herramientas de desarrollo.
Habilite "Paint Flashing" para observar qué áreas de la pantalla son repintadas al interactuar con la página.
![[Pasted image 20250121113916.png]]

## Preguntas para responder:

### ¿Cuántos recursos cargó la página en total? ¿Cuál fue el recurso más grande y cuánto tiempo tardó en cargarse?
La página descargó un total de 56 recursos, el recurso más grande fue de 883 B y tardó 107 ms 

### ¿Qué estilos CSS observó aplicados al elemento que inspeccionó? 
![[Pasted image 20250121114429.png]]

### ¿Qué ocurrió al modificar uno de ellos?
Lo que modifiqué fue el color de fondo
![[Pasted image 20250121114603.png]]

### Según la pestaña Performance, ¿Cuánto tiempo tardó la página en mostrar el contenido? 
La página tardó 0.72ms en mostrar el contenido

### Si utilizó "Paint Flashing", ¿Qué descubrió sobre las áreas que el navegador repinta al interactuar con la página?
Es muy útil para identificar que otros vínculos o referencias que pueden ser de otra página en la misma y que estos se encuentran en la página en la que estoy actualmente 
### ¿Qué es LCP y CLS?
LCP y CLS son métricas de rendimiento web que forman parte de las Core Web Vitals (CWV).  LCP significa Largest Contentful Paint y CLS significa Cumulative Layout Shift. 

- **LCP**
    Mide el tiempo que tarda en cargarse el elemento visual más grande de una página web. Este elemento suele ser una imagen o un vídeo, pero también puede ser un texto grande. 
- **CLS**
    Mide la estabilidad visual de una página web, es decir, si el diseño se desplaza de forma inesperada. Esto puede ocurrir cuando se carga una imagen o un anuncio por encima de un texto.