from tkinter import *
from functools import partial

root = Tk()
root.geometry('300x250+200+200')
root.title('Calculadora de IMC')
root.resizable(True,True)
root.maxsize(width=900, height=700)
root.minsize(width=100, height=70)
root.configure(bg='#FFFFFF')
e1_variable = StringVar()
e2_variable = StringVar()
e1 = Entry(root, textvariable=e1_variable)#altura
e1.grid(row=2, column=0, padx = (68,0), pady=(50,5))
lb1 = Label(root, text='Sua altura:', bg='#FFFFFF')
lb1.grid(row=2, column=0, padx = (0,170), pady=(50,5))

e2 = Entry(root, textvariable=e2_variable) #peso
e2.grid(row=3, column=0,padx = (68,0))
lb2 = Label(root, text='Seu peso:',bg='#FFFFFF')
lb2.grid(row=3, column=0, padx = (0,170), pady=(0,0))
lb = Label(root, text='Bem-vindo(a)',relief=SUNKEN, bg='#FFFFFF')
lb.grid(row=0, column=0,padx = (50,0), pady=(30))

def imc():
  h = float(e1_variable.get())
  p = float(e2_variable.get())
  imc = p/(h*h)
  if imc <= 16.0:
    j = "magreza grave."
  elif 16 < imc <= 17:
    j = "magreza moderada."
  elif 17 < imc <= 18.5:
    j = "magreza leve."
  elif 18.5 < imc <= 25:
    j = "um peso saudável, ideal."
  elif 25 < imc <= 30:
    j = "obesidade leve."
  elif 30 < imc <= 35:
    j = "obesidade moderada."
  elif 35 < imc < 40:
    j = "obesidade severa."
  elif 40 <= imc:
    j = "obesidade mórbida."
  lb['text'] = f'''Seu IMC é: %.2f.\nVocê tem ''' % imc + j

bt = Button(root, text="Calcular IMC", bg='#C1C1FF', command=partial(imc))
bt.grid(row=5, column=0, padx = (68,0), pady=(10))

root.mainloop()