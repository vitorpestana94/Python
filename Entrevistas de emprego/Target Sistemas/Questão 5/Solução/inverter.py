def inverter_string(string):
  return "O inverso da palavra {} é {}.".format(string, string[::-1])

print(inverter_string(input("Digite uma palavra:\n")))
