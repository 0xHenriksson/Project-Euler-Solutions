#Finds the largest prime factor of a number
import math

def maxPrime(n):

    #Initialize max prime facotr with the lowest one
    maxPrime = -1

    #Print number of 2s that divide n
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1 #equivalent to n /= 2

    # n is odd now, skip the even numbers and iterate only odd
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i

    #handles prime number greater than 2
    if n > 2:
        maxPrime = n

    return int(maxPrime)

print(maxPrime(600851475143))


