# Project: Calculator 
'-----------------------------'
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    keep_going = True
    n1 = int(input("First Number: "))

    while keep_going == True:
        for i in operations:
            print(i)
        symbol = input("Choose an operation? ")
        n2 = int(input("Second Number: "))
        
        ans = operations[symbol](n1,n2)
        print(f"{n1} {symbol} {n2} = {operations[symbol](n1,n2)}")
        
        user_choice = input(f"Do you want to continue with {ans} [Y/N]? ")

        if user_choice == "Y":
            n1 = ans
        else:
            keep_going = False
            print("\n" * 20)
            calculator()

calculator()