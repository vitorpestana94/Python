def fibo(entrada):
  
  numero_1, fibonacci = 0, 0
  numero_2 = 1
  
  while fibonacci < entrada:
    
    fibonacci = numero_1 + numero_2
    numero_1 = numero_2
    numero_2 = fibonacci
     
  return "O número {} faz parte da sequência de fibonacci.".format(entrada) if fibonacci == entrada else "O número {} não faz parte da sequência de fibonacci.".format(entrada)

print(fibo(int(input("Informe um número:\n"))))
