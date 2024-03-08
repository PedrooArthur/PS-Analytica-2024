def main():
 ent = input("Digite um número ")
 num_list = []
 freq = []
 while ent != 'f':

  a = verif(ent)
  if a == 0:
    num = int(ent)
    if len(num_list) == 0:
      num_list.append(num)
      freq.append(1)
    else:
        if num in num_list:
           for i in range(len(num_list)):
              if num == num_list[i]:
                freq[i] += 1
        else:
          num_list.append(num)
          freq.append(1)
          
          
      
    ent = input("Digite um número ")
  else:
    ent = input("Digite um número ")  
 
 
 for i in range(len(num_list)): print(f"o número {num_list[i]} foi digitado {freq[i]} vezes ")


def verif(ent):
   try:
      float(ent)
      print("Válido")
      return 0
   
   except ValueError:
      print("Inválido")
      return 1
if __name__=='__main__':
    main()
  