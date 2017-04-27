# Complementación de bases nitrogenadas:
Base = {'A':'T','T':'A','a':'t','t':'a','C':'G','G':'C','c':'g','g':'c'} # Establecer el diccionario con los pares complementarios.
chain = input('Introduzca la cadena de bases nitrogenadas:\n')           # Lectura de la cadena de entrada.

for i in range(len(chain)):                                              # Bucle de tantas iteraciones como caracteres se han introducido.
    if chain[i] in Base:                                                 # Si el caracter del índice i está registrado en el diccionario,
      print(Base[chain[i]],end='')                                       # Se imprime su definición, en este caso, su base complementaria.

#############################################################################################################################################

# Versión cíclica:
c = 's'                                                                  # Cuando c valga n deja de repetirse el programa
Base = {'A':'T','T':'A','a':'t','t':'a','C':'G','G':'C','c':'g','g':'c'} # Establecer el diccionario con los pares complementarios

while c != 'n':                                                          # Repetir hasta que el usuario indique con 'n' que no desea repetir.
  chain = input('Introduzca la cadena de bases nitrogenadas:\n')         # Lectura de la cadena de entrada, guardada en 'chain'
  print('La cadena complementaria es:')                                  # Texto

  for i in range(len(chain)):                                            # Bucle de tantas iteraciones como caracteres contenga la cadena.
    if chain[i] in Base:                                                 # Si el caracter del iterador i está registrado en el diccionario,
      print(Base[chain[i]],end='')                                       # Se imprime su definición, es decir, su base complementaria.

  c = input('\n¿Quiere introducir otra cadena? (s/n)\n')                 # Confirmar salida del programa

#############################################################################################################################################

# Versión mecánica. Va comprobando que el caracter sea una base y la cambia por su complementaria:
c = 's'

while c != 'n':
  array = input('Introduzca la cadena de bases nitrogenadas:\n')
  chain = []
  
  for i in range(len(array)):
    chain.append(array[i])

  for l in range(len(array)):
    if chain[l] == 'A':
      chain[l] = 'T'
    elif chain[l] == 'a':
      chain[l] = 't'
    elif chain[l] == 'T':
      chain[l] = 'A'
    elif chain[l] == 't':
      chain[l] = 'a'
    elif chain[l] == 'C':
      chain[l] = 'G'
    elif chain[l] == 'c':
      chain[l] = 'g'
    elif chain[l] == 'G':
      chain[l] = 'C'
    elif chain[l] == 'g':
      chain[l] = 'c'
    else:
      chain[l] = ''

  print('La cadena complementaria es:')

  for j in range(len(chain)):
    print(chain[j],end='')

  c = input('\n¿Quiere introducir otra cadena? (s/n)\n')
