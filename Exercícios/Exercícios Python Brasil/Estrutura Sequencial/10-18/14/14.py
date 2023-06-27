def pesc(p0):
  if p0 > 50:
    print("Você vai ter q pagar de multa {:.1f} reais.".format((p0-50)*4))
  else:
    print("Você não vai pagar multa.")
pesc(float(input("digite o peso total do pescado\n")))