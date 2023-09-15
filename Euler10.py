# Find the sum of all the primes below two million.
import math

def isPrime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3

    h = math.floor( 1 + math.sqrt(n))
    i = 5

    while i <= h:
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
        i += 6
    return True

arr = []

for number in range(0,2000000):
    if isPrime(number):
        arr.append(number)
    else:
        continue

print(sum(arr))