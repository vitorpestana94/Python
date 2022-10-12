""" 
esse programa identifica quantas latas, galões ou mistura de ambos será necessário para pintar 
uma área informada via input e quanto isto custará. Considerando, obviamente, 
quanto metros a tinta cobra e quanto cada galão e lata contem. Este programa é um exercício da página: https://wiki.python.org.br/EstruturaSequencial

""" 
"""
#This program calculate how many cans and gallons will be necessary to paint an area provided by the input and how much it will cost. There are 3 paiting scenarios. 
First scenery, buying only cans; second scenery, buying only gallons; third scenery, buying both cans and gallons. The program considerates the ink cover capacity and
how many liters are avaliable to paint in the gallon and in the can. This program is a exercice from the page: https://wiki.python.org.br/EstruturaSequencial
"""
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

#leve explicação


def Ltinta2(a): #o parametro a é a área
  consumolitro = a/6*1.1 #quantidade de litros considerando o rendimento *0.1
  q_lata = int(consumolitro/18) #quantidade de latas considerando consumo
  if consumolitro % 18 != 0: #caso o número lata n seja o suficiente para cobrir a área, mais uma é adicionada. É bom lembrar que o resto desta divisão(consumolitro pelo litro da lata) equivale à área que faltaria pintar.
    q_lata += 1
  q_galao = int(consumolitro/3.6) #quantidade de galões considerando consumo
  if consumolitro % 3.6 != 0: #caso o número de galões n seja o suficiente para cobrir a área, mais um é adicionado.
    q_galao+= 1  
  latamisturada = int(consumolitro/18) #variável identica a q_lata. Todavia, foi criada para ser manipulada na próxima variavel.

  galaomisturado = int((consumolitro - latamisturada*18)/3.6)
  print(consumolitro)
  print(consumolitro/18)
  print((consumolitro - latamisturada*18)/3.6)#para misturar latas e galões é preciso considerar que, obviamente, a lata sempre cobrirá uma área maior, porém, por este mesmo motivo, se forem adicionadas demais, as sobras serão excessivas. Sendo assim, a menor quantidade possível de latas(sendo o consumo total atendido com o complemento dos galões) é o ideal para evitar que se tenha muitos litros em excesso. Logo, diminuindo o número de latas multiplicado por 18(para virar litros) do consumo total de litros e dividindo tudo isso por 3.6(para descobrir a quantidade de galões) é possível descobrir a quantidade de galões necessários para complementar o mínimo possível de latas.Lembrando sempre que a variável latamistura n sofre incrimento.
  if consumolitro % 3.6 != 0:
    galaomisturado += 1
  return print("Caso você compre apenas latas, terá de comprar {} lata(as)\ne custará ao todo R$ {}.\n\nCaso você compre apenas galões, terá de comprar {} galões\ne isto custará ao total {}.\n\nCaso queira mistura galões e latas, visando economizar tinta, gastará {} latas e {} galão e ao todo custará {}.".format(q_lata, q_lata*80, q_galao, q_galao*25, latamisturada, galaomisturado,galaomisturado*25 + latamisturada*80))
Ltinta2(float(input("Digite a área a ser calculada:\n")))
