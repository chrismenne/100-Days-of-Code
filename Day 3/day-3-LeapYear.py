year = int(input("Enter a year: "))

'''
A leap year is: 
on every year that is evenly divisible by 4
    **except** every year that is evenly divisible by 100
        **unless** the year is also evenly divisible by 400
'''

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap Year")
        else:
            print(f"{year} is not a Leap Year")
    else:
        print(f"{year} is not a Leap Year")
else:
    print(f"{year} is not a Leap Year")
