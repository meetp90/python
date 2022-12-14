def hanoi(n,source,destination,temp):
    if n == 1:
        print("Moving disk from",n," from",source,"to ",destination)
        return
    hanoi(n-1,source,temp,destination)
    print("Moving disk from",n," from",source,"to ",destination)
    hanoi(n-1,temp,source,destination)

hanoi(3,'A','C','B')
