from math import sqrt, pow
a= float(input("Digite o coeficiente 'a':\n"))
b= float(input("Digite o coeficiente 'b':\n"))
c= float(input("Digite o coeficiente 'c':\n"))
d= (pow(b,2))-(4*a*c)
if a == 0:
  print("\nO coeficiente 'a' deve ser diferente de 0.")
elif d<0:
  print("\nNão existem raízes reais para esta equação.")
else:
  x1= ((-b +(sqrt(d)))/(2*a))
  x2= ((-b -(sqrt(d)))/(2*a))
  print("\nA equação composta pelos coeficientes 'a'= {}, 'b'= {} e c= {} possuí as seguintes raízes:\n\n'x1'= {:.1f}\n'x2'= {:.1f}".format(a,b,c,x1,x2))