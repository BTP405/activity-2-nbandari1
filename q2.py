import matplotlib.pyplot as plt

def graphSnowfall(t):
  """ Retrieves data from text file and displays information as a bar graph """
  range = ["0-10", "11-20", "21-30", "31-40", "41-50"]
  #initializes a list to count occurences for each range
  count = [0] * len(range)
  
  with open(t, 'r') as f:
    for line in f:
      amount = int(line)
      for i, r in enumerate (ranges):
        #The loop gets an element from range then splits it from '-' and converts it to int type
        lowerLimit, upperLimit = map(int, r.split('-'))
        #This if statement checks whether the number is between the upper and lower limits or not
        #and then increments it by 1.
        if lowerLimit <= amount <= upperlimit:
          count[i] += 1
          break

    #creating a bar graph using Matplotlib
   fig, ax = plt.subplots()
    # takes x-axis and y-axis
    ax.bar(ranges, counts)
    ax.set_ylabel("Number of occurrences")
    ax.set_xlabel("Ranges (cms)")
    ax.set_title("Snowfall accumulation")

    plt.show()

if __name__ == "__main__":
    graphSnowfall('test.txt')
