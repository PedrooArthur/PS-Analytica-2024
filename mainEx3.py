
def main():
 notas = [100,50,20,10,5,2]
 moedas =[1,0.50,0.25,0.10,0.05,0.01]

 valor =  input("Digite um valor: ")
 ver = verif(valor)

 if len(valor.split(".")[-1]) == 2 and ver == 0:
  qtd_notas, qtd_moedas = div(float(valor))
   
  for i in range(len(qtd_notas)):
    print(f"a nota {notas[i]} apareceu {qtd_notas[i]} vezes")

  for i in range(len(qtd_moedas)):
   print(f"a nota {moedas[i]} apareceu {qtd_moedas[i]} vezes")    

 else:
   print("oi") 

def div(valor):
  notas = [100,50,20,10,5,2]
  moedas =[1,0.50,0.25,0.10,0.05,0.01]
  qtd_notas = []
  qtd_moedas = []

  for nota in notas:
     val = valor // nota
     qtd_notas.append(val)
     valor = valor % nota

  for moeda in moedas:
     val = valor // moeda
     qtd_moedas.append(val)
     valor = valor % moeda     

  return qtd_notas , qtd_moedas
   
def verif(valor):
  try:
     float(valor)
     print("Válido")
     return 0
  except ValueError:
     print("Inválido") 
     return 1


if __name__ == '__main__':
    main()