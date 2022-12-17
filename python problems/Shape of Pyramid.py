n=int(input())

for i in range(1,(n*2),2):
    
    space=(n*2-i)//2  # space on both sides from 1st row
    
    print(" " * space + i *"*" + " " *space)
    
n=5
    *    
   ***   
  *****  
 ******* 
*********
   
