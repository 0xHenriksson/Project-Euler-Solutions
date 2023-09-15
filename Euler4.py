# Project Euler Challenge 4
# Objective: A palindromic number reads the same both ways. The largest palindrome made from the product of two
# 2-digit multiplicand is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit multiplicand.


def numGenerator():
    # generate product of two 3-digit multiplicands
    for multiplicand in range(100, 999):
        for multiplicand2 in range(999, 100):
            value = []
            value.append = multiplicand * multiplicand2
            return str(value)


def palindrome(num_string, length):
    length = len(str(num_string))
    for letters in l:
        if num_string(letters) == num_string(length - letters):
            return num_string
        else:
            continue


list = []

for multiplicand in range(100, 999):
    for multiplicand2 in range(999, 100, -1):
        product = multiplicand * multiplicand2  # create product of three-digit multiplicands
        string = str(product)  # turn product into string
        length = len(string)  # find length of string
        iterations = 0
        while iterations < length:  # iterate through length of string, comparing from outer digits
            if string[iterations] == string[length - iterations -1]: # inward to check from palindromality
                list.append(string)
                iterations += 1
            else:
                iterations += 1
                continue

print(sorted(list))
