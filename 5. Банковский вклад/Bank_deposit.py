def bank(a, years):
    x = 1
    summ1 = (a * 0.1) + a
    while x <= years:
        summ2 = (summ1 * 0.1) + summ1
        print("Total deposit ", x, "year: ", summ2)
        summ1 = summ2
        x += 1


a = int(input("Enter your deposit: "))
years = int(input("Enter deposit years: "))
bank(a, years)