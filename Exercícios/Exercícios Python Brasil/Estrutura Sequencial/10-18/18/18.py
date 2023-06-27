def vel(t, v):
  return print("O tempo de download de um arquivo de tamanho {} MB a partir de um link de internet de velocidade {} Mbps é: {} minutos".format(t, v, int((t/(v/8))/60)))
vel(float(input("Digite o tamanho do arquivo em MB\n")), float(input("Digite a velocidade do link de download em Mbps\n")))