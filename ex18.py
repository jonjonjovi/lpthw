def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1,arg2):
    print(f"arg1:{arg1}, arg2:{arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("i got nothin.")

print_two("jon","H")
print_two_again("jon2","H2")
print_one("one")
print_none()
