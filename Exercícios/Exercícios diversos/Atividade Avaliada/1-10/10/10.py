n1=float(input("Digite um número\n"))
n2=float(input("Digite outro número\n"))
n3 = float((n2*1/n1)*100)
if n3 < 100:
  print("{} é %{} de {} ".format(n2, n3, n1))
else:
  print("{} é %{} maior que {} ".format(n2, n3, n1))