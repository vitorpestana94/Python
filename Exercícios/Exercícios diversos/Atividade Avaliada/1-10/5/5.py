n1=float(input("Digite um número:\n"))
n2=float(input("Digite mais um número\n"))
s=input("\nDigite qual operação desejas realizar:\n+ para adição\n- para subtração\nx para multiplicação\n/ para divisão.\n")
if s == "+":
  print("A soma do número {} com o número {} é {}".format(n1, n2,n1+n2))
elif s=="-":
  print("A subtração do número {} pelo número {} é {}".format(n1, n2, n1-n2))
elif s=="x":
  print("A multiplicação do número {} pelo número {} é {:.2f}".format(n1, n2, n1*n2))
elif s=="/":
  print("A divisão do número {:.1f} pelo número {:.1f} é {:.2f}".format(n1, n2, n1/n2))