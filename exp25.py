import re

name_re = r'Mr.+|Ms.+|Mrs.+'
web_re = r'www.+in|www.+org|plus.+com|www.+com'
mail_re = r'\S+@+\S+'
phone_re = r'\S[^a-zA-Z\n]+\d+\S[^a-zA-Z\n]'

with open("regex.txt","r") as f:
    lines = f.readlines()
    lines = list(map(lambda a:a.strip(),lines))
    print(lines)


for line in lines:
    names = re.findall(name_re,line)
    if len(names) > 0:
        print(names[0])

for line in lines:
    website = re.findall(web_re,line)
    if len(website) > 0:
        print(website[0])

for line in lines:
    mail = re.findall(mail_re,line)
    if len(mail) > 0:
        print(mail[0])

for line in lines:
    phone = re.findall(phone_re,line)
    if len(phone) > 0:
        print(phone[0])
