def positive_numbers():
  
  numbers =[]
  odd_numbers= []
  number_occurrence = {}
  sum=0
  bool = True
  
  print("Digite um número positivo ou 0 para gerar um relatório:\n")
  
  while (bool):
    number = int(input(""))
    if number != 0:
      numbers.append(number)
    else:
      for x in range(len(numbers)):
        sum+=numbers[x]
        if numbers[x] % 2 != 0:
          odd_numbers.append(numbers[x])
      
      numbers.sort()
      odd_numbers.sort()
      number_occurrence= list(set(numbers))
      
      print("\nRelatório:\n\nA -Foram lidos {} números;\nB-O maior número lido foi o número {}.\nC-A média dos números lidos é {}.\nD-O menor número impar fornecido é {}.\nE-A quantidade de vezes que cada número ocorreu foi:\n".format(len(numbers), numbers[-1], sum/len(numbers), odd_numbers[0]))
      
      for y in range(len(number_occurrence)):
        print("O número {} ocorreu {} vezes.".format(number_occurrence[y], numbers.count(number_occurrence[y])))
      bool=False

positive_numbers()