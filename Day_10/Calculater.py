def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
def calculater():
 should_accumulate= True
 num1 = float(input("what is the first number?:"))

 while should_accumulate:
    for symbol in operations:
        print(symbol)
    opeartion_symbol = input("pick an opearation:")
    num2 = float(input("what is the next number?:"))
    answer = operations[opeartion_symbol](num1,num2)
    print(f"{num1}{opeartion_symbol}{num2}={answer}")
    choice=input(f"Type 'y' to continue calculating with {answer},or type 'n' to start a new calculation: ")

    if choice == "y":
     num1 = answer
    else:
     should_accumulate = False
     print("\n*20")
     calculater()
     
calculater()

 