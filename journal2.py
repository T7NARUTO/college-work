"""
program to convert the following and vice versa
1.Fahrenheit to celcius
2.meter to millimeter
3.inch to centimeter
4.gram to kilogram
5.meter to kilometer
"""


# defining the functions
def ftc():
    a = input('do you want to vice versa?(type yes or no)')
    if a == 'yes':
        c = int(input('enter celcius'))
        f = (c * (9 / 5)) + 32
        print('fahrenheit=', f)
    elif a == 'no':
        f = int(input('enter fahrenheit'))
        c = (f - 32) * (5 / 9)
        print('celcius=', c)
    else:
        print('invalid input')


def mtmi():
    a = input('do you want to vice versa?(type yes or no)')
    if a == 'yes':
        mi = int(input('enter millimeter'))
        m = mi / 1000
        print('meter=', m)
    elif a == 'no':
        m = int(input('enter meter'))
        mi = m * 1000
        print('millimeter=', mi)
    else:
        print('invalid input')


def itc():
    a = input('do you want to vice versa?(type yes or no)')
    if a == 'yes':
        c = int(input('enter centimeter'))
        i = c / 2.54
        print('inch=', i)
    elif a == 'no':
        i = int(input('enter inch'))
        c = i * 2.54
        print('centimeter=', c)
    else:
        print('invalid input')


def gtk():
    a = input('do you want to vice versa?(type yes or no)')
    if a == 'yes':
        kg = int(input('enter kilogram'))
        g = kg * 1000
        print('gram=', g)
    elif a == 'no':
        g = int(input('enter gram'))
        kg = g / 1000
        print('kilogram=', kg)
    else:
        print('invalid input')


def mtkm():
    a = input('do you want to vice versa?(type yes or no)')
    if a == 'yes':
        km = int(input('enter kilometer'))
        m = km * 1000
        print('meter=', m)
    elif a == 'no':
        m = int(input('enter meter'))
        km = m / 1000
        print('kilometer=', km)
    else:
        print('invalid input')


ob = ['1.Fahrenheit to celcius', '2.meter to millimeter', '3.inch to centimeter', '4.gram to kilogram',
      '5.meter to kilometer']
print('program to convert following and vice versa')
print(ob)

# getting input from user
n = int(input('enter the number of the above which you want to convert or vice versa'))
if n == 1:
    ftc()
elif n == 2:
    mtmi()
elif n == 3:
    itc()
elif n == 4:
    gtk()
elif n == 5:
    mtkm()
else:
    print('invalid input')
