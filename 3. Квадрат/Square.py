print("""\nProgramm 'Square' calculated Perimeter, Area of a square and Diagonal square on one side\n""")

import math


def square(side):
    perimeter = side * 4
    area = side ** 2
    diag = side * (math.sqrt(2))
    print("Perimeter: ", perimeter)
    print("Area of a square: ", area)
    print("Diagonal: ", diag)


side = float(input("Enter one side a square: "))

square(side)