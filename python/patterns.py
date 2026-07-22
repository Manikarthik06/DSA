"""n=5
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()"""

"""n = 3
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
for i in range(1,n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()"""

"""n=153
a=0
m=str(n)
for i in range(len(m)):
    b=n%10
    a=a+b**3
    n=n//10
if n==a:
    print("it is a armstrong number:",a)
else:
    print("not a armstrong number:",a)"""

n=5
