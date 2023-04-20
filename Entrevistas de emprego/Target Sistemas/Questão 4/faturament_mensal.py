def faturamento_mensal(dic):
  total=0

  for x, y in enumerate(dic):
    total+=dic[y]
  
  percentual_SP = dic["SP"]/total*100
  percentual_RJ = dic["RJ"]/total*100
  percentual_MG = dic["MG"]/total*100
  percentual_ES = dic["ES"]/total*100
  percentual_outros = dic["Outros"]/total*100
  
  return 'O percentual de representação que cada estado foi:\nSP: {:.1f}\nRJ: {:.1f}\nMG: {:.1f}\nES: {:.1f}\nOutros: {:.1f}'.format(percentual_SP, percentual_RJ, percentual_MG,  percentual_ES, percentual_outros)
