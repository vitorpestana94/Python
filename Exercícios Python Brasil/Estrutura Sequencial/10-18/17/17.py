def Ltinta2(a):
  consumolitro = a/6*1.1
  q_lata = int(consumolitro/18)
  if consumolitro % 18 != 0:
    q_lata += 1
  q_galao = int(consumolitro/3.6)
  if consumolitro % 3.6 != 0:
    q_galao+= 1  
  latamisturada = int(consumolitro/18)
  galaomisturado = int((consumolitro - latamisturada*18)/3.6)
  if consumolitro % 3.6 != 0:
    galaomisturado += 1
  return print("Caso você compre apenas latas, terá de comprar {} lata(as)\ne custará ao todo R$ {}.\n\nCaso você compre apenas galões, terá de comprar {} galões\ne isto custará ao total {}.\n\nCaso queira mistura galões e latas, visando economizar tinta, consumirás {} latas e {} galões e custará {} ao todo.".format(q_lata, q_lata*80, q_galao, q_galao*25, latamisturada, galaomisturado,galaomisturado*25 + latamisturada*80))
Ltinta2(float(input("Digite a área a ser calculada:\n")))