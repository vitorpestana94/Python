def nomefunc(n1, n2, n3):
  return print("O produto do dobro de {} pela metade de {} é {}\n A soma do triplo de {} com {} é {}\nO número {} elevado ao cubo é {}.\n".format(n1, n2, (n1*2)*(n2/2), n1, n3, 3*n1+n3, n3, n3**3))
nomefunc(int(input("Digite um número inteiro\n")), int(input("Digite outro número inteiro\n")), float(input("Digite um número real\n")))
