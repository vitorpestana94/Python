from math import sqrt
n1=float(input("Quanto mede o primeiro cateto do triângulo retângulo?\n"))
n2=float(input("Quanto mede o segundo cateto do triângulo retângulo?\n"))
n3 = float(sqrt((n1**2)+(n2**2)))
print("A hipotenusa deste triângulo retângulo de catetos {} e {}, respectivamente, é: {:.1f} ".format(n1, n2, n3))