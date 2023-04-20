import pytest

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

def test_faturamento_Mensal():
  assert faturamento_mensal({'SP': 20,'RJ':10, 'MG':5, 'ES': 4, 'Outros': 1}) == 'O percentual de representação que cada estado foi:\nSP: 50.0\nRJ: 25.0\nMG: 12.5\nES: 10.0\nOutros: 2.5'

  assert faturamento_mensal({'SP': 1,'RJ':2, 'MG':3, 'ES': 4, 'Outros': 5}) == 'O percentual de representação que cada estado foi:\nSP: 6.7\nRJ: 13.3\nMG: 20.0\nES: 26.7\nOutros: 33.3'

  assert faturamento_mensal({'SP': 5,'RJ':4, 'MG':3, 'ES': 2, 'Outros': 1}) == 'O percentual de representação que cada estado foi:\nSP: 33.3\nRJ: 26.7\nMG: 20.0\nES: 13.3\nOutros: 6.7'
  
if __name__ == "__main__":
    pytest.main(['-svv', __file__])
