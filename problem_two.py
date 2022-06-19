""" 
By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms. 

BREAKDOWN
For all the fibonacci numbers whose value is less than 4,000,000 find the sum of the even fibonacci numbers
"""
# 1. Get the fibonacci entire fibonacci sequence from 0 - n where n is the fibonacci number that values less than 4,000,000
# 2. Parse the list, if the number is even add it to the total sum value, otherwise skip this number

def getNextFibonacciNumber(nPrev, nPrevPrev):
  return nPrev + nPrevPrev

def getFibSequence():
  fibSequence = [0, 1]
  for i in range(0, 100):
    nextFibNumber = getNextFibonacciNumber(fibSequence[len(fibSequence) - 1], fibSequence[len(fibSequence) - 2])
    if(nextFibNumber >= 4000000):
      break
    fibSequence.insert(len(fibSequence), nextFibNumber)
  return fibSequence

def main():
  evenFibNumberSum = 0
  fibSequence = getFibSequence()
  for i in fibSequence:
    if (i % 2 == 0):
      evenFibNumberSum = evenFibNumberSum + i
  return evenFibNumberSum

if __name__ == '__main__':
  print(main())