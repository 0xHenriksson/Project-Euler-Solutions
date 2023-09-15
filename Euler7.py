# By listing the first six prime numbers: 2,3,5,7,11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?
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


def primeFinder(L):

    c = 2
    n = 0

    while c < L:

        n+=6
        if isPrime(n+1):
            c += 1
        if isPrime(n-1):
            c += 1
    return n + 1

b = primeFinder(10001)
print(b)
