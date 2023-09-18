# Workout the first ten digits of the sume of the one-hundred 50-digit numbers

# Open the file and read the numbers
with open('Euler13.txt', 'r') as f:
    numbers = f.readlines()

# Convert the numbers to integers and sum them up
total = sum(int(number) for number in numbers)

# Convert the sum to a string, then take the first 10 digits
first_ten_digits = str(total)[:10]

print(first_ten_digits)