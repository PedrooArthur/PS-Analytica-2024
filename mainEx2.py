def main():
 tab_let = ['a','b','c','d','e','f','g','h']
 tab_num = ['1','2','3','4','5','6','7','8']
 ent = input("Qual a sua posição atual e a desejada: ")


 while ent != 'f': 
  if len(ent.split()) != 2 or (len(ent.split()) ==2 and (len(ent.split()[0])!= 2 or len(ent.split()[1]) !=2 )): 
   print("Inválido 1")
   
  else:  
   pos_ini = ent.split()[0]
   pos_fin = ent.split()[1]
   if pos_ini[0] in tab_let and pos_fin[0] in tab_let and pos_ini[1] in tab_num and pos_fin[1] in tab_num:
     let_ind_ini = tab_let.index(pos_ini[0])
     let_ind_fin = tab_let.index(pos_fin[0])
     num_ind_ini = tab_num.index(pos_ini[1])
     num_ind_fin = tab_num.index(pos_fin[1])
     if abs(let_ind_ini - let_ind_fin) not in [1,2]: 
      print("Inválido")
     else:
      if abs(num_ind_ini - num_ind_fin) not in [1,2]:
       print("Inválido")
      else:
       if abs(let_ind_ini - let_ind_fin) == abs(num_ind_ini - num_ind_fin):
        print("Inválido")
       else:
        print("Válido")

   else:
     print("Inválido")
     

  ent = input("Qual a sua posição atual e a desejada: ")
   


if __name__ == '__main__':
 main()