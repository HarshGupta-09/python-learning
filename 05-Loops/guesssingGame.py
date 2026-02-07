
SECRET_NO = 9
flag = False 

i = 0

while i < 3 :
    guess = int (input("Guess : "))
    if guess == SECRET_NO :
       flag = True 
       break 
    i = i +1 

if flag :
    print ("YOU WON")
    
else : 
    print("You failed")
    
 
        
  
