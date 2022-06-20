# Find the largest palindrome made from the product of two 3-digit numbers.
# ex. 91 * 99 = 9009

# Logic: 
#
# Number is five or six digits 
# the first digit must be the last digit in the number, 
# the second digit must be seond to last digit

# If six digits
# the middle digits must be equal 
# the last must be the first

# If five digits
# center digit remains the same

def getProduct(i: int):
  for x in range(100, 1000):
    product = i*x
    if (isPalindrome(product)):
      return product
  return 0


def isPalindrome(i: int):
  palindromeString = str(i)
  if(palindromeString == palindromeString[::-1]):
    return True
  return False

def main():
  currentPalindome = 1
  for i in range(100, 1000):
    product = getProduct(i)
    if(product >= currentPalindome):
      currentPalindome = product
  print(currentPalindome)


if __name__ == '__main__':
  main()