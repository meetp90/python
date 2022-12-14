with open("text.txt","r") as f:
   lines = f.readlines()

print(lines)

with open("text1.txt","w") as f:
    f.write(" ".join(i for i in lines))