year = int(input("Enter year: "))
is_leap_year = False

if (year % 4 == 0 and year%100!=0) or (year%400==0):
    is_leap_year=True
    

print(is_leap_year)
