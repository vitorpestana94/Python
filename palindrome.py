#Uma função que identifica um palíndromo, seja uma palavra ou uma frase. A function that identifies a palindrome word or a palindrome sentence.
def is_palindrome_sentence(x):
  return x[::-1].casefold().replace("?", "").replace(",", "").replace(".", "").replace(":", "").replace(" ", "").replace("!", "").replace("’","") == x.casefold().replace("?", "").replace(",", "").replace(".", "").replace(":", "").replace(" ", "").replace("!","").replace("’", "")

h=input("\nPlease, enter a sentence:\n")
is_palindrome_sentence(h)

if is_palindrome_sentence(h):
  print("\nThe sentence: '{}'\nis a palindrome".format(h))
else:
  print("\nThe sentence '{}'\nis not a palindrome".format(h))
