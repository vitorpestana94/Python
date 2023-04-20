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

print(faturamento_mensal({'SP': 67836.43,'RJ':36678.66, 'MG':29229.88, 'ES': 27165.48, 'Outros': 19849.53}))
