# program to find prime numbers in an array
def arrayinput(x):
    for i in range(x):
        el = int(input('enter a element'))
        a.append(el)


def prime(x):
    for i in range(2, x):
        if (x % i) == 0:
            break
    else:
        p.append(x)


n = int(input('enter the limit of the array '))
print('this is a program to find prime numbers in an array')
a = []
p = []
arrayinput(n)
for i in a:
    prime(i)
print('prime no=', p)
