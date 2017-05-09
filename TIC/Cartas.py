# JUEGO DE CARTAS. Prestaciones: Puntuación, Gestión de la baraja y múltiples barajas.
import random                                                                                                   # Librería random
                                                                                                                # 
class Carta:                                                                                                    # Creación de la clase Carta. Métodos:
  def __init__(self,valor,palo):                                                                                # - Constructor: Inicializa los atributos
    self.valor = valor                                                                                          #                 de valor
    self.palo = palo                                                                                            #                 y palo.
                                                                                                                # 
  def __str__(self):                                                                                            # - Formato: Establece el formato al imprimir
    return valores[self.valor] + ' de ' + palos[self.palo]                                                      #             una carta como objeto.
                                                                                                                # 
class Baraja:                                                                                                   # Creación de la clase Baraja. Métodos:
  def __init__(self,valores,palos):                                                                             # - Constructor: Inicializa el array de cartas
    self.mazo = []                                                                                              #                 llamado mazo
                                                                                                                #                 y los valores y palos
    if str.upper(lang[0]) == 'E':                                                                               #                 dependiendo de la baraja
      for valor in range(10):                                                                                   #                 seleccionada por el usuario.
        for palo in range(4):                                                                                   # 
          self.mazo.append(Carta(valor,palo))                                                                   # 
    else:                                                                                                       # 
      for valor in range(13):                                                                                   # 
        for palo in range(4):                                                                                   # 
          self.mazo.append(Carta(valor,palo))                                                                   # 
                                                                                                                # 
  def barajar(self):                                                                                            # - Barajar: Utiliza la librería random para
    random.shuffle(self.mazo)                                                                                   #             ordenar aleatoriamente el mazo.
                                                                                                                # 
  def print_baraja(self):                                                                                       # - Print Baraja: Al imprimir la baraja se
    print('\nEn la baraja quedan:')                                                                             #                  imprimirán las cartas que
    for carta in self.mazo:                                                                                     #                  contiene el mazo.
      print(' ' + str(carta))                                                                                   # 
    print('\n')                                                                                                 # 
                                                                                                                # 
  def comparar_dos(self):                                                                                       # - Comparar: Compara los valores de las dos
    if self.mazo[0].valor > self.mazo[1].valor:                                                                 #              cartas superiores del mazo.
      print('Tu carta (' + str(self.mazo[0]) + ') es mayor que la mía (' + \
      str(self.mazo[1]) + ').\n +4 GANAS LA RONDA\n')                                                           #             Dependiendo de si es mayor o
      res = 0                                                                                                   #              menor el valor de la carta
    elif self.mazo[0].valor < self.mazo[1].valor:                                                               #              que corresponde al jugador
      print('Tu carta (' + str(self.mazo[0]) + ') es menor que la mía (' + \
      str(self.mazo[1]) + ').\n -2 PIERDES LA RONDA\n')                                                         #              se otorga más puntuación o
      res = 1                                                                                                   #              menos.
    else:                                                                                                       #             La posibilidad de empate
      print('Tu carta (' + str(self.mazo[0]) + ') es igual que la mía (' + \
      str(self.mazo[1]) + ').\n +1 EMPATE\n')                                                                   #              también otorga 1 punto.
      res = 2                                                                                                   # 
                                                                                                                # 
    self.mazo.remove(self.mazo[1])                                                                              #             Se eliminan las cartas que se
    self.mazo.remove(self.mazo[0])                                                                              #              han usado.
    print('    (Quedan ' + str(len(self.mazo)) + ' cartas en la baraja)')                                       #             Cantidad de cartas restantes.
                                                                                                                # 
    if res == 0:                                                                                                #             Puntuación.
      return +4                                                                                                 # 
    elif res == 1:                                                                                              # 
      return -2                                                                                                 # 
    else:                                                                                                       # 
      return +1                                                                                                 # 
                                                                                                                # 
# Comienzo del programa:                                                                                        # Fin de la declaración de clases.
                                                                                                                #
print('################################################################################\n\n' + \
      '  BIENVENID@ A ESTE JUEGO DE CARTAS\n\n' + \
      'En cada ronda recibirás una carta aleatoria de la baraja y el ordenador sacará la siguiente.\n' + \
      'Si el valor de tu carta es superior a la del ordenador, ¡habrás ganado la ronda!\n' + \
      'Al final de la ronda podrás elegir mostrar la baraja y barajarla escribiendo \'Y\'\n')                   # Mensaje de bienvenida.
                                                                                                                # 
lang = input(' Indique la baraja con la que desea jugar (Española o Poker):\n ')                                # Escoger baraja para jugar.
                                                                                                                # 
n = input(' Indique el número de rondas:\n ')                                                                   # Escoger el número de rondas que tendrá la
while str.isdigit(n) == False:                                                                                  #  la partida. Validar que sea un número.
  print('  El número de rondas debe ser un número entero.')                                                     # 
  n = input(' Indique el número de rondas:\n ')                                                                 # 
n = int(n)                                                                                                      # 
                                                                                                                # 
valores_esp = ['Dos','Cuatro','Cinco','Seis','Siete','Sota','Caballo','Rey','Tres','As']                        # Lista de los valores y palos de las
palos_esp = ['Oros','Copas', 'Bastos','Espadas']                                                                #  cartas de la baraja. Se utilizan para
valores_fr = ['Dos','Tres','Cuatro','Cinco','Seis','Siete','Ocho','Nueve','Diez','Principe','Reina','Rey','As'] #  componer el mazo de juego.
palos_fr = ['Picas','Tréboles','Diamantes','Corazones']                                                         # 
                                                                                                                # 
p=int(0)                                                                                                        # Puntuación = 0
                                                                                                                # 
if str.upper(lang[0]) == 'E':                                                                                   # Los valores y palos usados al crear el
  valores = valores_esp                                                                                         #  mazo de juego dependen de la baraja
  palos = palos_esp                                                                                             #  escogida por el jugador.
else:                                                                                                           # 
  valores = valores_fr                                                                                          # 
  palos = palos_fr                                                                                              # 
                                                                                                                # 
baraja = Baraja(valores,palos)                                                                                  # Creación del objeto baraja como una Baraja.
baraja.barajar()                                                                                                # Barajar el objeto baraja.
                                                                                                                # 
i=0                                                                                                             # Iterador por rondas con inicio en 0.
while i < n:                                                                                                    # 
  p += baraja.comparar_dos()                                                                                    # Añadir a la puntuación el resultado de
                                                                                                                #  comparar las cartas.
  if i < n-1:                                                                                                   # Validar el cambio de ronda hasta la
    paso_de_ronda = input(' -- Presione \'ENTER\' para continuar o \'Y\' para mostrar la baraja y barajar.\n ') #  penúltima ronda.
    if paso_de_ronda != '':                                                                                     #  Si se introduce la letra Y se imprimirá
      if str.upper(paso_de_ronda[0]) == 'Y':                                                                    #  el mazo de juego.
        baraja.print_baraja()                                                                                   #  Tras ver el mazo, se baraja de nuevo.
        baraja.barajar()                                                                                        # 
                                                                                                                # 
  if len(baraja.mazo) <= 1:                                                                                     # Aunque el número de rondas supere a las
    break                                                                                                       #  cartas de la baraja, el juego se acaba
  i+=1                                                                                                          #  cuando se llegue a las rondas indicadas
                                                                                                                #  o se acaben las cartas.
print('\n FIN DE LA PARTIDA\nTu puntuación es de ' + str(p) + ' puntos.')                                       # Puntuación final.
