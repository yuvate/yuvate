num = int(input("Enter a number:"))
a = 0
b = 1
for i in range(num):
    print(a,end = ' 12')
    c = a+b
    a = b
    b = c
