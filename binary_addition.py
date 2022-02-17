import math

def binaryaddition(a,b):
    c = a+b
    binar = bin(c).replace("0b","")
    return binar

print(binaryaddition(2, 2))