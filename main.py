ch =input("enter a charcter")
print("ASCII value of given character is ", ord(ch))
n = int(input("enter a number"))
x = bin(n)
print(x)
n = int(input("enter a number"))
for i in range (0,n):
    print(i**i )
r =int (input("enter the rows"))
print("mirror triangle")
for i in range(1,r+1):
    for j in range(1,r+1):
        if(j<=r-i):
            print('',end = '')
        else:
            print('*',end = '')
    print()