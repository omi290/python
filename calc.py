def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def calculator():
    a=int(input("enter first no."))
    b=int(input("enter second no."))
    op = input("enter the operator")
    if op=="+":
        print(add(a,b))
    elif op=="-":
        print(sub(a,b))
    elif op=="*":
        print(mul(a,b))
    elif op=="/":
        print(div(a,b))
    else:
        print("enter valid operator")

calculator()