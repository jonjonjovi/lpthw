from sys import exit
def func():
    num = input()
    if num == "1":
        print("1 here")
        func()
    elif num =="2":
        print("2 here")
        func()
    elif num =="2":
        print("more")
        func()
    else:
        exit(0)
func()
