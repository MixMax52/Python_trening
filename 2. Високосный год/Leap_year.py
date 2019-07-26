print("""\nProgramm defined leap year or not
Note: Enter year in format YYYY\n""")

def is_year_leap(year):
    if year % 4 == 0:
        print("Leap year: ", year, "True")
    else:
        print("Leap year: ", year, "False")


year = int(input("Enter any year: "))

is_year_leap(year)