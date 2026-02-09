
student = {
    "name" : "Harsh Gupta",
    "age" : 20,
    "is_verified" : True
}

# Accesing 
print(student["name"])
print(student.get('age'))

# Adding and updating 
student["Marks"] = 90 # Add
student["age"] = 22 # update

# Removing elemt 

student.pop('age')
del student['Marks']
print(student)
student["age"] = 22
student['Deparment'] = 'CSE'
print(student)

# Looping

# Only on Keys

for keys in student :
     print(keys)    

    #  Only on values 

print("*************")
for val in student.values():
     print(val)

print("************")

# On both key and value 
for k , v in student.items() :
     print(k,v)