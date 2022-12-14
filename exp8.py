for i in range(1,6):
    for _ in range(5 - i):
        print(" ",end="")
    for j in range(i):
        print(chr(65+5+j-i),end= " ")
    print()
for i in range(1,6):
    for _ in range(i):
        print(" ",end="")
    for j in range(5 - i):
        print(chr(65+i+j),end=" ")
    print()