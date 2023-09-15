# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum

def sum_squares(l):
    sum = 0
    for x in l:
        sum += pow(x, 2)
    return sum

def square_sum(n):
    square = 0
    for x in n:
        square += x
    y = pow(square, 2)
    return y

sumsq =sum_squares(range(0,100))
sqsum =square_sum(range(0,100))
diff = sqsum - sumsq
print(diff)