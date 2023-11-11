# program to find area of circle, semicircle, rectangle, square, cylinder,sphere
# solving this program using functions
def cir():
    r = int(input('enter the radius of circle'))
    area = 3.14159265359 * r * r
    print('area of circle =', area)


def scir():
    r = int(input('enter the radius of semicircle'))
    area = (3.14159265359 - (r * r)) / 2
    print('area of semicircle=', area)


def rec():
    l = int(input('enter the length of rectangle'))
    w = int(input('enter the width of the rectangle'))
    if l == w:
        print('enter a valid input')
    else:
        area = l * w
        print('area of rectangle=', area, 'cm^2')


def sqr():
    l = int(input('enter the length or width of the square'))
    area = l * l
    print('area of square=', area)


def cyl():
    r = int(input('enter the radius of the cylinder'))
    h = int(input('enter the height of the rectangle'))
    area = (2 * 3.14159265359 * r * h) + (2 * 3.14159265359 * r * r)
    print('area of cylinder=', area)


def sph():
    r = int(input('enter the radius of the sphere'))
    area = 4 * 3.14159265359 * r * r
    print('area of sphere=', area)


ob = ['1.circle', '2.semicircle', '3.rectangle', '4.square', '5.cylinder', '6.sphere']
print('program  to find area of the following')
print(ob)
n = int(input('enter the number of the objects whose area you want to find'))
if n == 1:
    cir()
elif n == 2:
    scir()
elif n == 3:
    rec()
elif n == 4:
    sqr()
elif n == 5:
    cyl()
elif n == 6:
    sph()
else:
    print('invalid input')
