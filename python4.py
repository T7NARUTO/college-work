# Add,Sub,Mul, and Div of Octal Numbers

a = int(input("Enter a Octal number"), 8)
b = int(input("Enter a Octal number"), 8)
add = a + b
sub = a - b
mul = a * b
div = int(a / b)
print("Addition=", oct(add), "Subtraction=", oct(sub), "Multiplication=", oct(mul), "Division=", oct(div))