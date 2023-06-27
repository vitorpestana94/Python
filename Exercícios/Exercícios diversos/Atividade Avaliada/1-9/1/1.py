n1=float(input("Digite um número:\n"))
n2=float(input("Digite outro número:\n"))
s="O maior é o número {}"
if n1>n2:
  print(s.format(n1))
else:
  print(s.format(n2))