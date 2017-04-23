class Persona:
  def __init__(self):
    self.nombre = None
    self.sexo = None
    self.edad = None

  def __str__(self):
    return(' ' + str.capitalize(self.nombre) + ', ' + str.upper(self.sexo) + ', ' + str(self.edad) + ' años.')

  def preguntar_valores(self):
    self.nombre = input('Nombre ' + str(i+1) + ': ')
    while str.isalpha(self.nombre) == False:
      print('El nombre no es válido. Introduzca sólo caracteres alfabéticos')
      self.nombre = input('Nombre ' + str(i+1) + ': ')

    self.sexo = input('Sexo ' + str(i+1) + ': ')
    while (len(self.sexo) > 1) or (str.upper(self.sexo) != 'V') & (str.upper(self.sexo) != 'M'):
      print('Dato incorrecto. Introduzca solo un caracter (V, M)')
      self.sexo = input('Sexo ' + str(i+1) + ': ')

    self.edad = input('Edad ' + str(i+1) + ': ')
    while str.isdigit(self.edad) == False:
      print('La edad debe ser un número entero de años.')
      self.edad = input('Edad ' + str(i+1) + ': ')
    self.edad = int(self.edad)



n = input("¿Cuántas personas quiere analizar?\n")
while str.isdigit(n) == False or int(n) < 1:
  print('El número de personas debe ser un número natural.')
  n = input("¿Cuántas personas quiere analizar?\n")
n = int(n)

array = []

for i in range(n):

  temp = Persona()
  temp.preguntar_valores()

  array.append(temp)


maximo = 0
minimo = 99

mayor = []
menor = []

for person in array:
  if person.edad > maximo:
    maximo = person.edad

  if person.edad < minimo:
    minimo = person.edad

for person in array:
  if person.edad == maximo:
    mayor.append(person)
  if person.edad == minimo:
    menor.append(person)

print('\nLa persona más mayor es:\n')
for person in mayor:
  print(person)
print('\nLa persona más joven es:\n')
for person in menor:
  print(person)


def ordenar_burbuja(coleccion):
  n = len(coleccion)
  i = 0
  while i < n:
    j = i
    while j < n:
      if coleccion[i].edad > coleccion[j].edad:
        temp = coleccion[i]
        coleccion[i] = coleccion[j]
        coleccion[j] = temp
      j += 1
    i += 1


ordenar_burbuja(array)

print('\nLas personas ordenadas de menor a mayor edad:\n')
for a in array:
  print(a)


def discriminar(listado):
  hom = []
  muj = []
  for persona in listado:
    if str.upper(persona.sexo) == 'V':
      hom.append(persona)
    elif str.upper(persona.sexo) == 'M':
      muj.append(persona)
  print('\nHombres:\n')
  for persona in hom:
    print(persona)
  print('\nMujeres:\n')
  for persona in muj:
    print(persona)


discriminar(array)

input('\n-- Pulse ENTER para salir --')
