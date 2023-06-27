
def S_L(sh, ht):
  br= sh*ht
  return print("+ Salário bruto: {}\n- IR: {:.1f}\n- INSS: {:.1f}\n- Sindicado: {:.1f}\n= Salário Líquido: {:.1f}".format(br, br*0.11 ,br*0.08,br*0.05,br-(br*0.11 + br*0.08 + br*0.05)))
S_L(float(input("Digite quanto ganhas por hora\n")), float(input("Digite quantas horas trabalhaste este mês\n")))