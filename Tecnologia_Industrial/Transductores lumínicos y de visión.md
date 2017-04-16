# Transductores lumínicos y de visión
## Introducción a los transductores
Los transductores son dispositivos que convierten una señal de una naturaleza física en otra energética, normalmente eléctrica. Se emplean para normalizar señales analógicas y digitales para su posterior análisis en otros elementos del sistema automático.
A la señal de entrada se aplica una función de transferencia en el transductor de tal forma que la señal de naturaleza física quede relacionada con la de respuesta, eléctrica.
Un sensor es un transductor que se utiliza para medir una variable física del entorno. De esta forma: **`no todos los transductores son sensores, así como todos los sensores son transductores`**.
[Transductores](https://waleskadorante.wordpress.com/2017/01/23/transductor/)

## Transductores lumínicos
Los transductores lumínicos, luminosos, de iluminación o de luz se emplean, por ejemplo, para medir variaciones en la luminosidad de un entorno, como sensores de posición para activar o desactivar sistemas o analizar si el recubrimiento de  ciertos objetos es metálico o no.
Por lo general, los transductores lumínicos son pasivos ya que no se conectan a una fuente eléctrica externa para dar respuesta a la magnitud física a medir, pues se basan en propiedades físicas, como el efecto fotoeléctrico.

[Transductores Lumínicos](https://waleskadorante.wordpress.com/2017/01/23/transductores-luminosos/)
### Fundamento
##### *Onda electromagnética*
Maxwell demostró la naturaleza electromagnética de la luz, en la que el campo eléctrico y el campo magnético cumplen una misma ecuación de onda armónica:  
[![](http://i.imgur.com/eN9KGB3.png)](http://i.imgur.com/TY27u5t.png)
##### *Energía, Potencia e Intensidad de una onda electromagnética*
Dicha onda transporta energía al hacer vibrar a todas las partículas sucesivamente. Se puede afirmar que la velocidad de propagación de la onda coincide con la velocidad de propagación de la energía de la onda, de forma que la ecuación energética de la onda es la siguiente:  
[![](http://i.imgur.com/4LJM94K.png)](http://i.imgur.com/wG00ymL.png)  
La potencia de la onda electromagnética lumínica es energía total emitida dividida por el tiempo que ha llevado emitirla:  
[![](http://i.imgur.com/FguUgGV.png)](http://i.imgur.com/liAbM6i.png)  
Esta potencia es propagada por la suma de todos los frentes de onda. Si la superficie de propagación (o frente de onda) es esférica, se trata de una onda tridimensional, la potencia se distribuye por el volumen de la esfera que tiene como centro el generador de la onda. Si la onda es bidimensional, el frente de onda por el que se propaga la potencia es el cilindro de luz que sale del plano generador en una dirección. Este último es el caso del rayo láser.  
La  intensidad de la onda electromagnética se define como la potencia dividida por la superficie del frente de onda. La intensidad de una onda bidimensional es diferente a la de la onda tridimensional:

| Onda bidimensional | Onda tridimensional |
|:------------------:|:-------------------:|
| [![](http://i.imgur.com/VpII9ZR.png)](http://i.imgur.com/VpII9ZR.png) | [![](http://i.imgur.com/JIE3zl9.png)](http://i.imgur.com/JIE3zl9.png) |

##### *Interacción de la onda electromagnética con la materia*
Las interacciones que la luz tiene con la materia son: `reflexión`, `refracción` y `absorción`.  
Cuando una onda lumínica bidimensional incide sobre una superficie que separa dos medios diferentes se cumple que la suma de la intensidad reflejada y la intensidad refractada o absorbida, equivale a la intensidad que incide.  
De igual forma, cuando una onda lumínica plana se propaga por un medio la intensidad puede permanecer constante, en cuyo caso se dice que el medio por el que discurre es no absorbente, o ir disminuyendo conforme la onda recorre distancia, en cuyo caso el medio es absorbente. La absorción de intensidad por un medio depende de la frecuencia de la onda. Para frecuencias inferiores a 20 Ghz la onda electromagnética proporciona energía cinética a las moléculas y éstas rozan entre sí por lo que pierden parte de la energía en forma de calor. Cuando la frecuencia es muy superior, la onda electromagnética se comporta como un haz de fotones, los cuales chocan con los electrones de los átomos y les proporcionan energía para alcanzar mayor nivel energético (orbital) dentro del propio átomo. Cada fotón del haz posee una energía dada por la ecuación `E[Energía] = h[Constante de Planck] · f[frecuencia]`.

### Captación de intensidades lumínicas
La absorción de la luz por un medio material se analiza mediante las siguientes magnitudes:
 * *Transmitancia*: cociente entre la intensidad transmitida y la intensidad incidente.
  
 * *Absorbancia*: opuesto del logaritmo decimal de la transmitancia
 ![](http://i.imgur.com/2IeAthC.png)

La intensidad transmitida a un medio absorbente depende tanto del propio medio como de la distancia que recorre la luz en él. La ley de Lambert relaciona la intensidad de la luz en función de la distancia que recorre en el medio absorbente, y la ley de Beer relaciona la intensidad transmitida en función de la concentración de la disolución (el medio):  
![](http://i.imgur.com/zUAWfAq.png)
### Clasificación de transductores lumínicos

 * Fototubos
 * Fotomultipicadores
 * Fotorresistencias
 * Fotodiodos
 * Fototransistores
 * Sensores ópticos
  * Sensores de proximidad:
  * Sensor Fotoeléctrico de Barrera
   ![](http://i.imgur.com/yL67fZJ.png)  
   ![](http://i.imgur.com/UXGZ66e.png)  
  * Sensor Fotoeléctrico de Retroreflexión
  * Sensor Fotoeléctrico Reflectivo Difuso
   ![](http://i.imgur.com/HthE5bX.png)  
  * 
## Transductores de visión
 * *Procesamiento por píxeles*
 * Cámaras mediante CCD () [](https://commons.wikimedia.org/wiki/File:Delta-Doped_Charged_Coupled_Devices_(CCD)_for_Ultra-Violet_and_Visible_Detection.jpg)
   [](http://wwwuser.cnb.csic.es/~fotonica/Photonic_en/Review/ccd1.htm)
 * Cámaras de vídeo
## Fuentes
 * [Transductores (p24)](http://iesalfonsox.es/wp-content/uploads/2015/07/Tema10.-transductores.-Sus-tipos.pdf)
 * [Clasificación + Aplicaciones (19) + Fotoeléctricos (14) + ](http://www.eudim.uta.cl/files/5813/2069/8949/fm_Ch03_mfuentesm.pdf)
