print("""\nProgramm 'Seasons' indicates the time of the year by the number of the month\n""")

def season(month):
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]
    if month in winter:
        print("Month number ", month, "- зима")
    elif month in spring:
        print("Month number ", month, "- весна")
    elif month in summer:
        print("Month number ", month, "- лето")
    elif month in autumn:
        print("Month number ", month, "- осень")
    else:
        print("Incorrect number")


month = int(input("Enter any month: "))

season(month)