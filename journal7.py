# compare and copy a string without using in-built functions
# copying a string to another
a = 'string'
b = ''
for i in a:
    b += i
print(a, b)
# comparing to string
c = 'string'
d = 'string'
if c == d and len(c) == len(d):
    print('similar')
else:
    print('not similar')
