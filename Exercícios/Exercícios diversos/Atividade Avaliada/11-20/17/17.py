n1= float(input("Digite um número:\n"))
n2 =float(input("Digite outro número:\n"))
n3 =float(input("Digite mais um número:\n"))
if n1 > n2+n3:
  print("O número {} é maior do que a soma dos números {} e {} (obs: a soma de de ambos é {})".format(n1, n2, n3,  n2 + n3))
elif n1 < n2+n3:
  print("O número {} é menor do que a soma dos números {} e {} (obs: a soma de de ambos é {})".format(n1, n2, n3, n2 + n3))
else:
  print("O número {:.0f} é igual à soma dos números {:.0f} e {} (obs, a soma de de ambos é {:.0f}".format(n1, n2,n3,  n2 + n3))