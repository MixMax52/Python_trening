print(""" Programm 'Simple arithmetic operation'
\t allowable numbers: ONLY integer \n\n""")


def arithmetic(A, B, oper):
    if oper == "+":
        print("{} + {} = {}" .format(A, B, A + B))
    elif oper == "-":
        print("{} - {} = {}" .format(A, B, A - B))
    elif oper == "*":
        print("{} x {} = {}" .format(A, B, A * B))
    elif oper == "/":
        print("{} / {} = {}" .format(A, B, A / B))
    else:
        print("Неизвестная операция")


A = int(input("Enter any number-1: "))
B = int(input("Enter any number-2: "))
oper = input("Enter arithmetic operation(+, -, *, /) :  ")

arithmetic(A, B, oper)