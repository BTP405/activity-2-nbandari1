#The decorator function defines a nested function called wrapper that calls func
def decorator(func):
  def wrapper(*args):
    num, lineNum = func(*args)
    #f strings are used to embed datatypes directly into a string
    print(f"For line no. {lineNum}:")
    print(f"The numbers read: {numbers}")
    print(f"The count of the numbers read: {len(numbers)}")
    print(f"The average of the numbers: {round(sum(numbers)/len(numbers),2)}")
    print(f"The maximum of the numbers: {max(numbers)}\n\n")
  return wrapper

#this is used to apply the decorator function the stat function, so that whenever stat
#function is called, it automatically calls the decorator function.
@decorator
def stat(nums, lineNum):
  """ This will invoke the decorator function """
  return nums, lineNum


def printStats(t):
  """ Retieves data from text file in lines of numbers and calls decorator function for each line read """
  with open(t, 'r') as file:
    for lineNum, line in enumerate(file, start=1):
      #this converts the line of numbers to a list of float type numbers
      num = line.split();
      num = list(map(float, num))
      #this calls the stat and decorator functions for every line
      stat(num, lineNum)

if __name__ == "__main__":
printStats('test3.txt')
