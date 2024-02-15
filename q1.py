# functions checks whether a number is prime or not
def checkPrime(n):
  """ Checks whether a number is prime or not """
  #number has to be greater than 2
  if n < 2:
    return False
  #n*0.5 calculates half of n. For example if n is 10, then n*0.5 is 5. The +1 is included 
  #for rounding down any decimal number to the nearest integer. This condition calculates the 
  #upper limit for the loop.
  for i in range (2, int(n*0.5 + 1)):
    if n%i == 0:
      return False
  return True

def getPrimeNumbers(n):
  """ Returns a list containing all prime numbers from 2 to n """
  num = []
  for i in range(2, n + 1):
    if checkPrime(i):
      num.append(i)
  return num

#This ensures that the code runs when the script is executed directly and not imported
#as a module.
if __name__ == "__main__":
  print(getPrimeNumbers(23))
