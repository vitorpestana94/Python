
"""
Um programa que identifica um palíndromo, seja uma palavra ou uma frase.A função is_palindrome_sentence retira qualquer caractere que não seja letras e 
número enquanto o resto do código identifica se de fato se trata de um palindrome. Na verdade, esta não é a melhor solução, todavia é a que pensei por mim mesmo.
This is a program that identifies a palindrome word or a palindrome sentence. The function is_palindrome_sentence eliminate any character that is not a letter or a number.
Actually, that is not the best possible solution, however is the solution that i thougth by myself.
"""
def is_palindrome_sentence(x):
  return x[::-1].casefold().replace("?", "").replace(",", "").replace(".", "").replace(":", "").replace(" ", "").replace("!", "").replace("’","") == x.casefold().replace("?", "").replace(",", "").replace(".", "").replace(":", "").replace(" ", "").replace("!","").replace("’", "")

h=input("\nPlease, enter a sentence:\n")
is_palindrome_sentence(h)

if is_palindrome_sentence(h):
  print("\nThe sentence: '{}'\nis a palindrome".format(h))
else:
  print("\nThe sentence '{}'\nis not a palindrome".format(h))
