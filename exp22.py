l1 = [i for i in range(10)]
l2 = [i for i in range(10)]
l3 = list(map(lambda x,y : x+y,l1,l2))
print(l3)
l4 = list(map(lambda a: a**3,filter(lambda a: a & 1,l1)))
print(l4)