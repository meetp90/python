with open("text1.txt","r") as f:
    lines = f.readlines()

for i in lines:
    print(i[::-1])
