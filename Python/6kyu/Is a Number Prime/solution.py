# The reason why we should only check up until the square root
# of the given number is because if a number n is not a prime,
# it can be factored into two factor a and b: n = a * b.
# 
# If both a and b were greater than the square root of n,
# then a * b would be greater than n. So at least one of those
# factors must be less than or euqla to the square root of n.

import math

def is_prime(num):
  if num <= 1:
      return False
      
  for i in range(2, int(math.sqrt(num))+1):
      if num % i == 0:
          return False
  return True