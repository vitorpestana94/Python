import pytest

def fibo(entrada):
  
  numero_1, fibonacci = 0, 0
  numero_2 = 1
  
  while fibonacci < entrada:
    
    fibonacci = numero_1 + numero_2
    numero_1 = numero_2
    numero_2 = fibonacci
     
  return "O número {} faz parte da sequência de fibonacci.".format(entrada) if fibonacci == entrada else "O número {} não faz parte da sequência de fibonacci.".format(entrada)

def test_fibo():
  
  assert fibo(1) == "O número 1 faz parte da sequência de fibonacci."
  assert fibo(2) == "O número 2 faz parte da sequência de fibonacci."
  assert fibo(3) == "O número 3 faz parte da sequência de fibonacci."
  assert fibo(6) == "O número 6 não faz parte da sequência de fibonacci."
  assert fibo(9) == "O número 9 não faz parte da sequência de fibonacci."
  assert fibo(13) == "O número 13 faz parte da sequência de fibonacci."
  assert fibo(90) == "O número 90 não faz parte da sequência de fibonacci."
  assert fibo(610) == "O número 610 faz parte da sequência de fibonacci."
  assert fibo(988) == "O número 988 não faz parte da sequência de fibonacci."
  assert fibo(6765) == "O número 6765 faz parte da sequência de fibonacci."
  
if __name__ == "__main__":
    pytest.main(['-svv', __file__])
