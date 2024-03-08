def main():
 horario =  input("Digite a hora: ") 
 while horario != 'f' :
    aux1 = verif_len(horario)
    if  aux1 == 0  :
      hora_min = horario.split(":")
      hora = hora_min[0]
      min = hora_min[1]
      aux2 = verif_num(hora)
      aux3 = verif_num(min)   
      if aux2 == 0 and aux3 == 0:
        hora_min = horario.split(":")
        hora = int(hora_min[0])
        min = int(hora_min[1])
        if 0 <= hora < 24 and 0 <= min < 60 : 
          if hora >= 12  :
            grau_hora = (hora - 12)*30
            grau_min = min*6
          else :
            grau_hora = hora*30
            grau_min = min*6

          graus = abs(grau_min - grau_hora)
          if graus > 180:
            graus = abs(graus-360)

          print(f"os ponteiros fazem : {graus} graus")  
        else:
          print("Inválido")  
      else:
        print("Inválido")
    else:
      print("Inválido")

    horario =  input("Digite a hora: ") 
  
  
def verif_num(hora):
 try:
    float(hora)
    return 0
 except ValueError:
   return 1
   
def verif_len(horario):
 
 if len(horario) == 5:
   if horario[2] == ':':
    return 0
   else:
     return 1
     
 else:
   return 1 

if __name__ == '__main__':
  main()
  

  
 