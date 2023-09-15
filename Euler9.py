import time

start_time = time.time()

#Function to generate numbers
#with the help of hint given in question
def pythagorean_triplet():
 for a in range(1,1000):
  for b in range(1,1000):
   c = 1000-a-b
   if (a**2+b**2) == c**2:
    return a*b*c

#printing the result
print(pythagorean_triplet())

#time at the end of execution
end_time = time.time()

#Printing the total_time
print(end_time - start_time)
