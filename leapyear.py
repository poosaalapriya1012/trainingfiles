year = int(input("Enter year: "))
is_leap_year = False

if year % 4 == 0:
    is_leap_year = True
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False

print(is_leap_year)
