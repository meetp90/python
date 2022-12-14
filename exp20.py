def perfect(num):
    add = 0
    for i in range(1,int(num/2)+1):
        if num % i == 0:
            add += i
    if add == num:
        return True
    return False

print(perfect((28)))