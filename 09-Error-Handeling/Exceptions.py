

try : 
    x = 2
    y = 0
    z = x/y
except:
 print("Can't divide by 0")

#  using try , except , finally , else 

try : 
   num = int(input("Enter Number : "))

except : 
   print("Invaid number")

else : 
   print("You enterned " , num)

finally : 
   print("Done")