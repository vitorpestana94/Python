def print_n_lines(integer = int(input("Informe um número:\n")), line=""):
  if integer <= 0:
    print("ERROR!\nO número informado não pode ser menor ou igual a 0!")
  
  for x in range(integer):
    for y in range(x, integer):
      line+=(str((integer-y)**2)+" ")
    line+="\n"
  
  print("\n"+line)

print_n_lines()