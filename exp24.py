try:
    print(5/0)
except ZeroDivisionError as zero:
    print(zero)

l = []
try:
    m = max(l)
except ValueError as val:
    print("no values")

try:
    print(10+"10")
except TypeError as type:
    print(type)

try:
    print(5/0)
except ArithmeticError as arth:
    print(arth)

try:
    print([1,2,3][3])
except IndexError as Index:
    print(Index)

class valExcp(Exception):
    def __init__(self,val):
        self.val = val
    
    def __str__(self):
        return f"val = {self.val}"

try:
    raise valExcp(5)
except Exception as exp:
    print(exp)