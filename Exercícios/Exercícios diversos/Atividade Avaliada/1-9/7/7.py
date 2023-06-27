while True:
  n1=float(input("Calculadora de Regra de Três Simples:\n0- Exit\n\nPrimeira Fração:\t\tSegunda Fração:\nNumerador\t\t\t\tNumerador\n----------\t\t X\t\t---------\nDenominador\t\t\t\tVariável\n\n\nDigite o numerador da primeira fração:\n"))
  if n1 == 0:
    break
  else:
    n2=float(input("Digite o denominador da primeira fração\n"))
    n3=float(input("Digite o numerador da segunda fração\n"))
    n4= n2*n3/n1
    n5= n1*n3/n2
    op = input("\n\nDigite:\n\n1-Para grandezas diretamente proporcionais.\n2-Para grandezas inversamente proporcionais.\n0-Para fechar o programa\n")
    if op == "0" or n1=="0":
      break
    if op == "1":
      print("\nO denominador da segunda fração é: {:.1f}".format(n4))
    elif op == "2":
      print("\nO denominador da segunda fração(a variável) é: {:.1f}".format(n5))
    else:
      print("Opção inválida!Entre com 1 ou 2!")
    op2 = input("\nDesejas sair?\n1-Sim\n2-Não\n")
    if op2 == "1":
      break