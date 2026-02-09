
def greet (name = "User"):
    print("Hi there !!")
    print("Hello",name)

greet()
greet("Harsh")

#

def sum (a,b):
    return a + b 

print(sum(2,5))

# Multiple args function 

def total (*nums):
    return nums

print(total(10,20,30,40,50))