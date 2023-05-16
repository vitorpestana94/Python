def pideal(s, a):
  if s == 'h'.casefold():
    p = (72.7*a) - 58
  elif s == 'm'.casefold():
    p = (62.1*a) - 44.7
  else:
    print("Você selecionou uma opção inválida! O programa será fechado!")
  return print("O seu peso ideal é {:.1f}".format(p))

pideal(input("Digite 'h' para calcular o seu peso ideal caso sejas homem\ne 'm' caso sejas mulher.\nCaso digites uma opção inválida, o programa será fechado.\n"), float(input("Digite a sua altura, por favor.\n")))
