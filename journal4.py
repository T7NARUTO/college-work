# program to find type of number
n = int(input("enter a number "))
if n == 0:
    print('number is zero')
elif n > 0:
    print('number is positive')
elif n < 0:
    print('number is negative')
else:
    print('invalid input')