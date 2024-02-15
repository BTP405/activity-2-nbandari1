# functions checks whether a number is prime or not
def checkPrime(n):
  """ Checks whether a number is prime or not """
  #number has to be greater than 2
  if n < 2:
    return False
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


if __name__ == "__main__":
  print(getPrimeNumbers(23))
