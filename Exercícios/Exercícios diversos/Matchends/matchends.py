"""
Com uma lista de strings fornecida através de argumentos, retorne a contagem do número de
strings onde o comprimento destas é maior que dois e os dois últimos caracteres são os mesmos.
por exemplo: o argumento ['aba', 'xyz', 'aa', 'x', 'bbb'] retorna 3.
"""

"""
with a string list provide by the function argument, return the count of the strings with length 
higher than two and with identical last two characters.
for example: the argument ['aba', 'xyz', 'aa', 'x', 'bbb'] return 3.
"""

def match_ends(words):
  c=0
  while c < len(words):
    for x, y in  enumerate(words):
      if len(words[x]) >= 2 and words[x][0] == words[x][-1]:
        c+=1
    return c
  
print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
