for i in range(1,6):
    for _ in range(5 - i):
        print(" ", end = "")
    for j in range(i):
        print(chr(65+j),end=" ")
    print()
