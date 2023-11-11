# smart streetlight program
# taking time in 24hr format as input from the user
t = int(input('enter the time in 24hr format (note=give only hour not minutes)'))
if 18 >= t <= 5:
    print('ON')
elif t <= 0:
    print('invalid input')
else:
    print('OFF')
