import matplotlib.pyplot as plt

def graphSnowfall(t):
  """ Retrieves data from text file and displays information as a bar graph """
  range = ["0-10", "11-20", "21-30", "31-40", "41-50"]
  count = [0] * len(range)
  
  with open(t, 'r') as f:
    for line in f:
      c = int(line)
      for i, r in enumerate (ranges):
        lowerLimit, upperLimit = map(int, r.split('-'))
        if lowerLimit <= c <= upperlimit:
          count[i0] += 1
          break

   fig, ax = plt.subplots()
    # takes x-axis and y-axis
    ax.bar(ranges, counts)
    ax.set_ylabel("Number of occurrences")
    ax.set_xlabel("Ranges (cms)")
    ax.set_title("Snowfall accumulation")

    plt.show()

if __name__ == "__main__":
    graphSnowfall('test.txt')
