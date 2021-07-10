# GCD of two numbers:
# Euclid's algorithem
# a = b*x + remender  ( x== quotient)
# when remender = 0 ,
# then gcd == remeneder
# example: gcd of 64,48
# 64 = 48*1 + 16
# 48 = 16*3 + 0
# 16 = 0
# gcd == 16
# example: gcd of 4,18
# 18 = 4*4 + 2
# 4 = 2*2 + 0
# 2 = 0 
# gcd = 2

# first method
# import math
# G = math.gcd(4,18)
# print(G)

# 2nd way...
def GCD(a,b):
    if b == 0: # base case
        return a
    else:
        return GCD(b,a%b) #recursive case
a = int(input("enter number: "))
b = int(input("enter number: "))
print(GCD(a,b))
