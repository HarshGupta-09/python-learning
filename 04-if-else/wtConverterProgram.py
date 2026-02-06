
weight = int(input("Enter your weight : "))

type = input("(L)bs OR (K)gs : ")

if type.upper() == 'L':
    print(weight * 0.45) 
else:
    print(weight * 2.20)

