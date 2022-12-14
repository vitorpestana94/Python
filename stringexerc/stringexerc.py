""" 
Proposta do exercício:
Através de um input que fornecerá uma string "s", retorne outra string em que
todas as ocorrências do primeiro caracter da string "s"
foram alterados para '*', tirando a primeira.
Exemplo: 'babble' se tornará 'ba**le'.
"""

"""
Exercise statement:
with an input that will provide a string "s", return a string that all the ocurrences of the first
character are replaced for "*", except the first one.
Example: 'babble' will return 'ba**le'
"""

def fix_start(s):
    return "{}{}".format(s[0],s.title().lstrip(s[0].title()).replace(s[0], "*"))

print(fix_start(input("Digite a palavra:\n")))
