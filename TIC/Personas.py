# Gestión de personas mediante tres atributos: Nombre, edad y sexo.
# Prestaciones: Mayores, menores, orden por edad y discriminación por sexo.
class Persona:                                                                                                 # Creación de la clase persona. Métodos:
  def __init__(self):                                                                                          # - Constructor: inicializa los atributos en blanco
    self.nombre = None                                                                                         # 
    self.sexo = None                                                                                           # 
    self.edad = None                                                                                           # 
                                                                                                               # 
  def toString(self):                                                                                          # - Dar formato al imprimir el objeto. De esta forma, en vez 
    return(' ' + str.capitalize(self.nombre) + ', ' + str.upper(self.sexo) + ', ' + str(self.edad) + ' años.') #    de que python devuelva la ubicación en la memoria del
                                                                                                               #    objeto, sale un texto personalizado.
  def preguntar_valores(self):                                                                                 # - Preguntar valores con los que rellenar los atributos.
    self.nombre = input('Nombre ' + str(i+1) + ': ')                                                           #    Leer entrada para cada nombre.
    while str.isalpha(self.nombre) == False:                                                                   #    Validar entrada según:
      print('El nombre no es válido. Introduzca sólo caracteres alfabéticos')                                  #     Caracteres alfabéticos, sin espacios ni puntuación.
      self.nombre = input('Nombre ' + str(i+1) + ': ')                                                         #    Una vez validado queda almacenado el nombre.
                                                                                                               # 
    self.sexo = input('Sexo ' + str(i+1) + ': ')                                                               #    Leer entrada para el sexo de cada persona.
    while (len(self.sexo) > 1) or (str.upper(self.sexo) != 'V') & (str.upper(self.sexo) != 'M'):               #    Validar entrada según:
      print('Dato incorrecto. Introduzca solo un caracter (V, M)')                                             #     m, M, V ó v.
      self.sexo = input('Sexo ' + str(i+1) + ': ')                                                             #    Una vez validado queda almacenado el sexo.
                                                                                                               # 
    self.edad = input('Edad ' + str(i+1) + ': ')                                                               #    Leer entrada para cada edad.
    while str.isdigit(self.edad) == False:                                                                     #    Validar entrada según:
      print('La edad debe ser un número entero de años.')                                                      #     Número entero mayor o igual a 0.
      self.edad = input('Edad ' + str(i+1) + ': ')                                                             #    Una vez validado queda almacenada la edad.
    self.edad = int(self.edad)                                                                                 #    Además se convierte a tipo 'entero'.
                                                                                                               # 
                                                                                                               # 
n = input("¿Cuántas personas quiere analizar?\n")                                                              # 'n' guarda el número de personas a analizar
while str.isdigit(n) == False or int(n) < 1:                                                                   # Validar 'n' según:
  print('El número de personas debe ser un número natural.')                                                   #  Número entero positivo.
  n = input("¿Cuántas personas quiere analizar?\n")                                                            # Una vez validado se almacena en 'n'.
n = int(n)                                                                                                     # 'n' se convierte a tipo 'entero'.
                                                                                                               # 
array = []                                                                                                     # Creación de una lista vacía, 'array', que contendrá
                                                                                                               #  a todas las personas.
for i in range(n):                                                                                             # Bucle que guardará los datos de las 'n' personas.
                                                                                                               # 
  temp = Persona()                                                                                             # Objeto temp de la clase Persona.
  temp.preguntar_valores()                                                                                     # Se le dan valores a los atributos de temp.
                                                                                                               # 
  array.append(temp)                                                                                           # Se mete temp en el array de personas.
                                                                                                               # 
                                                                                                               # 
maximo = 0                                                                                                     # El menor mayor valor posible es 0.
minimo = 99                                                                                                    # El mayor menor valor posible es 99.
                                                                                                               # 
mayor = []                                                                                                     # Para sacar todas las personas con la edad más alta
menor = []                                                                                                     #  y más baja, creo un array de los mayores y otro de
                                                                                                               #  los menores.
for person in array:                                                                                           # Buscar la edad más alta de entre todas las personas.
  if person.edad > maximo:                                                                                     #  Si es más alta que la anterior más alta, se
    maximo = person.edad                                                                                       #   reemplaza por la nueva alta.
                                                                                                               # 
  if person.edad < minimo:                                                                                     #  Si es más baja que la anterior más baja, se
    minimo = person.edad                                                                                       #   reemplaza por la nueva baja.
                                                                                                               # 
for person in array:                                                                                           # Almacenar en los array mayor y menor a las personas
  if person.edad == maximo:                                                                                    #  que tienen la edad más alta y baja (encontradas en
    mayor.append(person)                                                                                       #  el paso anterior).
  if person.edad == minimo:                                                                                    # 
    menor.append(person)                                                                                       # 
                                                                                                               # 
print('\nLa persona más mayor es:\n')                                                                          # Texto.
for person in mayor:                                                                                           # Como puede haber más de una persona que tenga la
  print(person.toString())                                                                                     #  máxima edad, necesito un bucle para sacarlas todas.
print('\nLa persona más joven es:\n')                                                                          # Texto.
for person in menor:                                                                                           # Como puede haber más de una persona que tenga la
  print(person.toString())                                                                                     #  mínima edad, necesito un bucle para sacarlas todas.
                                                                                                               # 
                                                                                                               # 
def ordenar_burbuja(coleccion):                                                                                # Defino una función para ordenar utilizando el
  n = len(coleccion)                                                                                           #  algoritmo burbuja. 'n' será ahora el total de
  i = 0                                                                                                        #  elementos a ordenar.
  while i < n:                                                                                                 # Se ordena sustituyendo uno por el anterior si se
    j = i                                                                                                      #  da que uno es menor que el anterior.
    while j < n:                                                                                               # 
      if coleccion[i].edad > coleccion[j].edad:                                                                # 
        temp = coleccion[i]                                                                                    # 
        coleccion[i] = coleccion[j]                                                                            # 
        coleccion[j] = temp                                                                                    # 
      j += 1                                                                                                   # 
    i += 1                                                                                                     # 
                                                                                                               # 
                                                                                                               # 
ordenar_burbuja(array)                                                                                         # Llamar a la función de ordenar
                                                                                                               # 
print('\nLas personas ordenadas de menor a mayor edad:\n')                                                     # Texto.
for a in array:                                                                                                # Sacar todas las personas del array, que ya ha sido
  print(a.toString())                                                                                          #  ordenado.
                                                                                                               # 
                                                                                                               # 
def discriminar(listado):                                                                                      # Defino una función para separar hombres de mujeres
  hom = []                                                                                                     #  en distintos array: 'hom' y 'muj'. La función
  muj = []                                                                                                     #  también imprime el resultado.
  for persona in listado:                                                                                      # Para todas las personas del parámetro 'listado'.
    if str.upper(persona.sexo) == 'V':                                                                         # Si el sexo introducido es v o V, se añade a la
      hom.append(persona)                                                                                      #  lista de hom.
    elif str.upper(persona.sexo) == 'M':                                                                       # Si el sexo introducido es m o M, se añade a la
      muj.append(persona)                                                                                      #  lista de muj.
  print('\nHombres:\n')                                                                                        # Texto.
  for persona in hom:                                                                                          # Imprime todos los hombres de hom.
    print(persona.toString())                                                                                  # 
  print('\nMujeres:\n')                                                                                        # Texto.
  for persona in muj:                                                                                          # Imprime todas las mujeres de muj.
    print(persona.toString())                                                                                  # 
                                                                                                               # 
                                                                                                               # 
discriminar(array)                                                                                             # Lalar a la función de deiscriminar pasando el
                                                                                                               #  contenido de array como parámetro por referencia.
input('\n-- Pulse ENTER para salir --')                                                                        # Confirmación de salida
