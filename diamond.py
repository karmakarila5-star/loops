rowsize = int(input("enter the number of rows:"))
if rowsize % 2 == 0: 
    halfdiamrow = int(rowsize/2)
else:
    halfdiamrow = int(rowsize/2) + 1
space = halfdiamrow - 1
for i in range(1,halfdiamrow +1):
    for j in range(1,space + 1):
        print(end =" ")
    space = space - 1
    num = 1
    for j in range(2*i -1):
        print(end=str(num))
        num = num +1
    print()  
space = 1
for i in range(halfdiamrow):
    for j in range(1,space+1):
        print(end =" ")
        space = space + 1
        num = 1
    for j in range(1,2*(halfdiamrow-i)):
            print(end=str(num))
            num = num + 1
    print()