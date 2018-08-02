from sys import argv
script, input_file = argv

def add(a,b):
    print(f"Adding: {a} + {b}")
    return a+b

def subtract(a,b):
    print(f"subtract: {a} - {b}")
    return a-b

def multiply(a,b):
    print(f"multiplying {a}*{b}")
    return a*b

def divide(a,b):
    print("Dividing {a}/{b}")
    return a/b

print("lets do some math")

age = add(29,1)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print("Here is a puzzle.")
what = add(age,subtract(height,multiply(weight,divide(iq,2))))
print("That becomes: ",what "can you di it by hand")
