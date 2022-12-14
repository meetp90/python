with open("text1.txt","r") as f:
    lines = f.readlines()

print("no of lines",len(lines))
noWords = 0
for i in lines:
    words = i.split()
    print(words)
    noWords += len(words)
print(words)
print("no of words: ",noWords)
characters = 0
characters += sum(len(word) for word in lines)
print(characters)