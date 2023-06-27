from math import ceil
def L_tinta(a):
  return print("Você gastará {:.0f} lata(as) e o preço total destas é R$ {:.0f}".format(a/3/18,ceil(a/3/18)*80))
L_tinta(float(input("Informe a área em metros quadrados que deverá ser pintada:\n")))