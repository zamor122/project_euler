# Find the sum of all the multiples of 3 or 5 below 1000.
def findRange():
  answerSum = 0
  for i in range(0, 1000):
    if(i % 3 == 0):
      answerSum = answerSum + i
      continue
    if(i % 5 == 0):
      answerSum = answerSum + i
      continue
  return answerSum


def main():
  sum = findRange()
  print(sum)

if __name__ == '__main__':
  main()

#Lesson Learned: READ THE QUESTION