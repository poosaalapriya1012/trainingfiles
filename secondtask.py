s = "Programming"
if len(s) > 10:
    if s[0] == 'P':
        print("The string has more than 10 characters and starts with 'P'.")
    else:
        print("The string has more than 10 characters but doesn't start with 'P'.")
else:
    if s[-1] == 'g':
        print("The string has 10 or fewer characters and ends with 'g'.")
    else:
        print("The string has 10 or fewer characters and doesn't end with 'g'.")
