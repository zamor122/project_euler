# What is the largest prime factor of the number 600851475143?

#BREAKDOWN
# Return only the largest prime factor of the number, not all


# Prime factorization is the list of numbers whose product is the origin parent number

# Take parent number and continue to parse

# Possible logic: Find all factors of the number, test each one, if the number is prime and greater than the current largest factor, set that number
maxPrimeFactor = 0
previousFactor = 0
currentQuotient = 0

def isPrime(n: int):
  for i in range(2, (n-1)):
    if(n % i == 0):
      return False
  return True

def findFactor(n):
  for i in range(2, 600851475143):
    if (n % i == 0):
      global currentQuotient
      global previousFactor
      currentQuotient = n/i
      previousFactor = i
      break

if __name__ == '__main__':
  findFactor(600851475143)
  while (currentQuotient != 0):
    findFactor(currentQuotient)
    if(isPrime(previousFactor)):
      maxPrimeFactor = previousFactor
      print("Max Prime Factor: ", maxPrimeFactor)
      print("Previous Factor: ", previousFactor)
      print("Current Quotient: ", currentQuotient)
      print("----------------------------------------")
  print("!!!!!!!!done!!!!!!!!!!!")
  print("Max Prime Factor: ", maxPrimeFactor)
  print("Previous Factor: ", previousFactor)
  print("Current Quotient: ", currentQuotient)
  print("----------------------------------------")


  
      