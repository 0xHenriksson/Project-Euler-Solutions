# Project-Euler-Solutions
A collection of my Project Euler solutions

- `Euler3.py`: This script finds the largest prime factor of a number. It uses a simple iterative method to divide the number by its smallest prime factor until it becomes a prime itself. The time complexity is O(sqrt(n)).
- `Euler4.py`: This script finds the largest palindrome made from the product of two 3-digit numbers. It uses a nested loop to generate products and checks for palindromality by comparing digits. The time complexity is O(n^2).
- `Euler5.py`: This script finds the smallest positive number that is evenly divisible by all of the numbers from 1 to 20. It uses the mathematical concept of least common multiple (LCM) and the time complexity is O(n).
- `Euler6.py`: This script finds the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. It uses two functions to calculate the sum of squares and the square of the sum. The time complexity is O(n).
- `Euler7.py`: This script finds the 10001st prime number. It uses a function to check if a number is prime and a loop to find the 10001st prime. The time complexity is O(n log log n) due to the prime number theorem.
- `Euler8.py`: This script finds the thirteen adjacent digits in a 1000-digit number that have the greatest product. It uses a sliding window approach to calculate the product of 13 adjacent digits. The time complexity is O(n).
- `Euler9.py`: This script finds the Pythagorean triplet for which a + b + c = 1000. It uses a nested loop to generate triplets and checks if they satisfy the Pythagorean theorem. The time complexity is O(n^2).
- `Euler10.py`: This script finds the sum of all the primes below two million. It uses a function to check if a number is prime and a loop to sum all primes below two million. The time complexity is O(n log log n) due to the prime number theorem.
- `Euler11.py`:
This solution has a time complexity of O(n^2) where n is the size of the grid. This is because we are iterating over each cell in the grid once. The space complexity is O(1) as we are not using any additional space that scales with the input size.
- `Euler12.py`: This script finds the first triangle number to have over five hundred divisors. It generates triangle numbers and for each one, calculates the number of divisors using prime factorization. The time complexity is approximately O(n sqrt(n)) where n is the triangle number, due to the need to iterate over each triangle number and calculate its divisors.
- `Euler13.py`: This script calculates the first ten digits of the sum of one-hundred 50-digit numbers. It reads the numbers from a file, converts them to integers, sums them up, and then takes the first ten digits of the sum. The time and space complexity are both O(n), where n is the total number of digits, as it iterates over each digit once and stores all digits in memory.
