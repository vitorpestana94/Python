n1=int(input("Digite um número para saber sua tabuada:\n"))
print(f'\n\nA tabuada de {n1} é:')
for z in range(1, 11):
  print("{} x {} = {}".format(n1,z,n1*z))    