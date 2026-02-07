
names = ["Harsh" , "Diwakar" , "Jai", "Pandey","Electrical"]

print(names)
print(names[3])

names.append("sonu")
names.insert(2,"Sanskar")
print(names)

names.remove("Jai")

# Program to find the largest number in  a list 

nums = [12,23,434,533,45,33,56,33,33,33]
max = -1

for i in nums :
    if i > max :
        max = i

print(max)


uniques = []

for i in nums : 
    if  i not in uniques :
        uniques.append(i)

print(nums)
print(uniques)