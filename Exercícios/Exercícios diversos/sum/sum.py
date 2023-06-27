#soma de todos os numeros pares ou impares no range. Sum all the even or odd numbers in the range.
def sum_eo(t, n):
    h = []
    y = []
    if t == 'e':
       for number  in range(1, n+1):
         if number % 2 == 0:
           h.append(number)
       print(sum(h))
    elif t == 'o':
      for number in range(1, n+1):
        if number % 2 != 0:
          y.append(number)
      print(sum(y))
      
sum_eo(input('Enter "e" for an even number or "o" for an odd number:\n'), int(input('Please enter a number:\n')))
