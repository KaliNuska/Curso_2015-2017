# Transductores lumínicos y de visión
## Introducción a los transductores
Los transductores son dispositivos que convierten una señal de naturaleza física (mecánica, térmica, magnética, eléctrica, lumínica, etc.) en otra magnitud, normalmente eléctrica. Se emplean para normalizar todo tipo de señales analógicas y digitales.  
A la señal de entrada se aplica una función de transferencia en el transductor de tal forma que la señal de naturaleza física quede relacionada con la de respuesta, eléctrica.  
Un sensor es un transductor que se utiliza para medir una variable física del entorno. De esta forma: **`no todos los transductores son sensores, pero todos los sensores son transductores`**.  
Los transductores se pueden clasificar atendiendo, por ejemplo, a la energía que necesitan para su funcionamiento o a la magnitud física que transforman:  
Según la energía que necesitan para funcionar:  

| Activos | Pasivos |
|:-------:|:-------:|
| Necesitan una alimentación eléctrica externa | No requieren alimentcaión externa, pues se basan exclusivamente en propiedades y leyes físicas |

Según la magnitud que transforman:
> Posición linear o angular, desplazamiento, velocidad linear o angular, aceleración, fuerza y par, nivel, presión, caudal, temperatura, proximidad, luminosidad...

## Transductores lumínicos
Los transductores lumínicos, luminosos, de iluminación o de luz se emplean, por ejemplo, para medir variaciones en la luminosidad de un entorno, como sensores de posición para activar o desactivar sistemas o analizar si el recubrimiento de  ciertos objetos es metálico o no.
Por lo general, los transductores lumínicos son pasivos ya que no se conectan a una fuente eléctrica externa para dar respuesta a la magnitud física a medir, pues se basan en propiedades físicas, como el efecto fotoeléctrico.

[Transductores Lumínicos](https://waleskadorante.wordpress.com/2017/01/23/transductores-luminosos/)
### Fundamento
Para poder explicar el funcionamiento de los transductores de luz, es necesario conocer qué es la luz y cómo se comporta.

##### *Onda electromagnética*
Maxwell demostró la naturaleza electromagnética de la luz, en la que el campo eléctrico y el campo magnético cumplen una misma ecuación de onda armónica:  
[![](http://i.imgur.com/eN9KGB3.png)](http://i.imgur.com/TY27u5t.png)
##### *Energía, Potencia e Intensidad de una onda electromagnética*
Dicha onda transporta energía al hacer vibrar todas las partículas sucesivamente. Se puede afirmar que la velocidad de propagación de la onda coincide con la velocidad de propagación de la energía de la onda, de forma que la ecuación energética de la onda es la siguiente:  
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
De igual forma, cuando una onda lumínica plana se propaga por un medio, la intensidad puede permanecer constante, en cuyo caso se dice que el medio por el que discurre es no absorbente, o ir disminuyendo conforme la onda recorre distancia, en cuyo caso el medio es absorbente. La absorción de intensidad por un medio depende de la frecuencia de la onda. Para frecuencias inferiores a 20 Ghz la onda electromagnética proporciona energía cinética a las moléculas y éstas rozan entre sí por lo que pierden parte de la energía en forma de calor. Cuando la frecuencia es muy superior, la onda electromagnética se comporta como un haz de fotones, los cuales chocan con los electrones de los átomos y les proporcionan energía para alcanzar mayor nivel energético (orbital) dentro del propio átomo. Cada fotón del haz posee una energía dada por la ecuación `E[Energía] = h[Constante de Planck] · f[frecuencia]`.

##### *Captación de intensidades lumínicas*
La absorción de la luz por un medio material, lo que  se analiza mediante las siguientes magnitudes:
 * *Transmitancia*: cociente entre la intensidad transmitida y la intensidad incidente.
  
 * *Absorbancia*: opuesto del logaritmo decimal de la transmitancia
 ![](http://i.imgur.com/2IeAthC.png)

La intensidad transmitida a un material absorbente depende tanto del propio material o medio como de la distancia que recorre la luz en él. La ley de Lambert relaciona la intensidad de la luz en función de la distancia que recorre en el medio absorbente, y la ley de Beer relaciona la intensidad transmitida en función de la concentración de la disolución (el medio):  
![](http://i.imgur.com/zUAWfAq.png)
### Clasificación de transductores lumínicos
 * Fototubos:  
Un fototubo es un transductor cuyo funcionamiento se basa en el efecto fotoeléctrico: cuando un fotón con suficiente energía llega a un metal, arranca un electrón de dicho metal. La composición de un fototubo, o célula fotoeléctrica, es: un tubo de vidrio donde se hace el vacío, en cuyo interior se coloca un metal de forma semicilíndrica y al otro extremo un electrodo metálico. Se alimenta con corriente continua de tal forma que el polo negativo se conecta al metal cilíndrico (cátodo) y el positivo se conecta a una resistencia en serie con el otro electrodo (ánodo).  
Al incidir la luz sobre el metal cilíndrico, desprende electrones que son atraídos por el electrodo positivo. Así se genera una corriente y se crea una diferencia de potencial eléctrico entre los bornes de la resistencia, el cual es proporcional a la intensidad de la luz incidente sobre la célula fotoeléctrica.
 * Fotomultipicadores:  
Cuando la intensidad de la luz incidente en el fototubo es muy pequeña, por lo que se generaría una corriente demasiado pequeña, pero se quiere un transductor que trabaje con intensidades muy bajas de luz, se emplea el fotomultiplicador.  
En este transductor los electrones que emergen del cátodo en vez de llegar directamente al ánodo, llegan a otro electrodo, dínodo, en el que chocan, arrancando un mayor número de electrones que los que generarían llegando al ánodo directamente. Éstos se dirigen hacia otro dínodo y le arrancan mas electrones aún. El proceso se repite tantas veces como dínodos contenga el fotomultiplicador. Finalmente todos los electrones llegan al ánodo y generan la intensidad de corriente y la diferencia de potencial en el circuito exterior del fotomultiplicador.
 * Fotorresistencias:  
Las fotorresistencias son semiconductores (`Si`, `Ge`) cuya resistencia eléctrica depende del flujo luminoso que incide sobre ellas.  
La intensidad que incide sobre ellas por unidad de superficie, medida en `lux`, se denomina Iluminancia.  
La ecuación que relaciona la resistencia en función de la iluminación es:  
![](http://i.imgur.com/qftXGRf.png)  
De la ecuación se deduce que al aumentar la iluminación disminuye la resistencia, por lo que se comporta como una resistencia `NTC`.  
Sin embargo, la precisión de las fotorresistencias es bastante baja y su capacidad de respuesta a pequeños cambios, lenta, lo que reduce su aplicación a funciones sencillas como el control del encendido de farolas o el ajuste de los valores de imagen (exposición, brillo, uso de flash) al hacer una fotografía.  
![](http://i.imgur.com/bua4N11.png)
 * Fotodiodos:  
Cuando una unión PN de un diodo es iluminada con radiación electromagnética (visible o invisible), la barrera de potencial (diferencia de potencial eléctrico formada por el campo eléctrico existente entre las cargas positivas y negativas) de la unión se altera. La variación de la barrera de potencial puede medirse mediante un voltímetro y expresarse en función de la intensidad lumínica incidente.  
El fotodiodo se construye con tres zonas semiconductoras (PIN): una N (con electrones libres), otra P (con falta de electrones) y otro semiconductor intrínseco (puro) entre las dos zonas.  
Al conectar un fotodiodo a un circuito mediante una resistencia, por ésta circula una corriente proporcional a la intensidad luminosa incidente, de modo que la incidencia de luz provoca una corriente en el sentido inverso al del diodo.  
![](http://i.imgur.com/12GkRkd.png)  
 * Fototransistores:  
Al igual que el fotodiodo, un fototransistor también posee una unión PN que se debe iluminar con radiación electromagnética.  
En el fototransistor, es la base y el emisor lo que forma la unión PN.
Al iluminarla, se forma el diodo Base-Emisor, siendo la radiación electromagnética la encargada del aporte energético para que se produzca la corriente en el diodo. El fototransistor se conecta a una fuente de tensión mediente una resistencia en el colector, permitiendo que circule la corriente por el transistor en el sentido Colector-Emisor cuando recibe iluminación.  
![](http://i.imgur.com/YSJGpWj.png)  
 * Sensores ópticos:  
Los sensores ópticos presentan numerosas aplicaciones en la detección de objetos en funcionamiento como transductores de proximidad o posición. Utilizan un emisor de infrarrojos, generalmente, y que forma una barrera con un fototransistor o fotodiodo.  
![](http://i.imgur.com/6bCVm1N.png)  
   + Sensores de reflexión:  
El LED emisor y el receptor se encuentran en el mismo módulo o encapsulado. Es necesario que el objeto sea reflectante para que el haz de luz de refleje e incida en el receptor.  ![](http://i.imgur.com/MNqmXJu.png)![](http://i.imgur.com/NpvVOpj.png)  
   + Sensores de proximidad:  
   Nuevamente, el LED emisor y el receptor se ubican en el mismo encapsulado. Para detectar la posición, el sensor de proximidad emite un haz luminoso modulado, que puede reflejarse al impactar con otro objeto y ser detectado por el receptor, que evalúa la señal percibida.  
   ![](http://i.imgur.com/XliHSiC.png)  
   + Sensor Fotoeléctrico de Barrera:  
   En los detectores de barrera, el objeto se interpone entre el emisor del haz luminoso y el receptor. Dependiendo de si la luz llega o no al receptor, se produce la conmutación.  
   ![](http://i.imgur.com/LiYd4m9.png)
   ![](http://i.imgur.com/UXGZ66e.png)  
   + Sensor Fotoeléctrico de Retroreflexión:  
   El funcionamiento es análogo al del sensor de barrera, pero en los sensores de retrorreflexión el emisor y el receptor están en el mismo encapsulado y el elemento opuesto a ellos es un reflector.  
   ![](http://i.imgur.com/WOmKMzj.png)  
   ![](http://i.imgur.com/yL67fZJ.png)  
   + Sensor Fotoeléctrico Reflectivo Difuso:  
   En este sensor, es el objeto a detectar el que realiza la función de reflector. Estos sensores permiten aproximar la distancia del objeto utilizando varios receptores como se aprecia en el esquema:  
   ![](http://i.imgur.com/96jERj3.png)
   ![](http://i.imgur.com/6GiiNFw.png)  
## Transductores de visión
Los transductores de visión o de imagen son sensores presentes en cualquier dispositivo de grabación de imagen. Su funcionamiento se basa en convertir la atenuación de las ondas de luz, al atravesar o verse reflejadas por cuerpos, en señales eléctricas. De esta forma detectan y capturan la informacion para componer la imagen.  
Se comercializan como chips que se componen de millones de fototransistores y la imagen que producen depende de la cantidad de fototransistores implicados en la composición de la misma. En un chip de visión o de imagen, cada uno de los fototransistores que lo componen reciben el nombre de píxel. Un sólo chip suele contener varios millones de píxeles (del inglés *`picture element`*, elemento de imagen), por lo que se habla del número de Megapíxeles al describir un sensor.  
La sensibilidad del sensor depende de lo que se denomina *eficiencia cuántica*, esto es, la la cantidad mínima de fotones que deben incidir en cada fototransistor para que tenga lugar el efecto fotoeléctrico. El número de electrones que se desprenden es directamente proporcional a la intensidad lumínica. El proceso que sigue en el funcionamiento de un sensor varía dependiendo de qué modelo de sensor se utilice:  

| CCD | CMOS |
|:----|:-----|
| Los electrones producidos son transferidos de cada píxel detector o *fotosite* al amplificador de señal, que será transmitida a la computadora de la imagen. | La señal se amplifica antes de salir de cada *fotosite*, para lo que hay un amplificador por cada pixel. Esto soluciona problemas de interacción entre píxeles que tienen lugar en los sensores CCD, pero disminuye la superficie sensible a la luz. |

En cualquiera de estos dos casos la obtención del color se produce analizando uno de los tres colores primarios e interpolando los otros dos. Esto no ocurre en los sensores Foveon, que tienen tres detectores de color en cada pixel para no realizar interpolación alguna.  
Como curiosidad cabe añadir que los sensores Kodak perciben los colores `cian`, `magenta` y `amarillo`, en lugar de `rojo`, `verde` y `azul`, por demostrar mejor sensibilidad en ciertas circunstancias.

## Conclusión
Para terminar, recomiendo encarecidamente los siguientes artículos (el primero en inglés) para aquellos más interesados en los fundamentos de la fotografía y de sus sensores:  
 * [`Image Sensor Architectures for Digital Cinematography` de **DALSA**](https://render.githubusercontent.com/view/pdf?commit=97b191f3536074836f28305b4241f72de1dfd5ce&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f4b616c694e75736b612f437572736f5f323031352d323031372f393762313931663335333630373438333666323833303562343234316637326465316466643563652f5465636e6f6c6f6769615f496e647573747269616c2f496d6167655f53656e736f725f4172636869746563747572655f576869746570617065725f4469676974616c5f43696e656d615f30303231382d30305f30332d37302e706466&nwo=KaliNuska%2FCurso_2015-2017&path=Tecnologia_Industrial%2FImage_Sensor_Architecture_Whitepaper_Digital_Cinema_00218-00_03-70.pdf). [PDF](https://github.com/KaliNuska/Curso_2015-2017/raw/master/Tecnologia_Industrial/Image_Sensor_Architecture_Whitepaper_Digital_Cinema_00218-00_03-70.pdf)  
 * [`Fundamentos de fotografía digital` de **Efraín García** y **Rubén Osuna**](http://www2.uned.es/personal/rosuna/resources/photography/ImageQuality/fundamentos.imagen.digital.pdf) y [más artículos](http://www2.uned.es/personal/rosuna/resources/fotografia.htm).

## Fuentes
 * [`Transductores` del **Departamento de Tecnología de la Universidad de Valencia**](http://www.uv.es/~navasqui/Tecnologia/Tema4.pdf)  
 * [`Los transductores. Sus tipos` del **IES Alfonso X el Sabio de Toledo**](http://iesalfonsox.es/wp-content/uploads/2015/07/Tema10.-transductores.-Sus-tipos.pdf)  
 * [`Sensores y transductores` de la **Escuela Universitaria de Ingenieria Mecanica - Universidad de Tarapaca** (Chile)](http://www.eudim.uta.cl/files/5813/2069/8949/fm_Ch03_mfuentesm.pdf)  
