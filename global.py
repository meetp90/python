 
g = 10
def f():
    global g 
    g = 12
    print(g)

# f()
print(g)