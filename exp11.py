from collections import Counter

with open("text.txt","r") as f:
    lines = f.readline()
    count = dict(Counter(lines))
    print(count)