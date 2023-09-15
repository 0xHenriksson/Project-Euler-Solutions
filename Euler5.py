# Euler Project Challenge 5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

def lcm(a,b):
    gcd = math.gcd(a,b)
    return((abs(a*b)//gcd))

max = 2
for i in range(2,21):
    max=lcm(max,i)

print(max)
