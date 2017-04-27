# Complementación de bases nitrogenadas:
dict = {'A':'T','T':'A','a':'t','t':'a','C':'G','G':'C','c':'g','g':'c'}
chain = input('Introduzca la cadena de bases nitrogenadas:\n')
for i in range(len(chain)):
    if chain[i] in dict:
      print(dict[chain[i]],end='')

# Versión cíclica:
c = 's'
dict = {'A':'T','T':'A','a':'t','t':'a','C':'G','G':'C','c':'g','g':'c'}

while c != 'n':
  chain = input('Introduzca la cadena de bases nitrogenadas:\n')
  print('La cadena complementaria es:')

  for i in range(len(chain)):
    if chain[i] in dict:
      print(dict[chain[i]],end='')

  c = input('\n¿Quiere introducir otra cadena? (s/n)\n')

# Versión mecánica:
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
