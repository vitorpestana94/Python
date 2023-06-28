import cmath
n1= float(input("Digite a parte real do primeiro número complexo que desejas somar com o segundo:\n"))
n2= float(input("Digite a parte imaginária do primeiro número complexo que desejas somar com o segundo:\n"))
n3= float(input("Digite a parte real do segundo número complexo que desejas somar com primeiro:\n"))
n4= float(input("Digite a parte imaginária do segundo número complexo que desejas somar com primeiro:\n"))
nc1= complex(n1, n2)
nc2= complex(n3, n4)
print("A soma dos números complexos {} e {} é: {}\n".format(nc1, nc2, nc1*nc2))