def wordCount(t):
  """ Retrieves data from a text file and returns a dictionary """
  dict = {}
  with open (t, 'r') as f:
    for lineNum, line in enumerate(file, start=1):
      words = line.split()
      for word in words:
        if word in dict:
          dict[word].append(lineNum)
        else:
          dict[word] = [lineNum]
  return dict

if __name__ == "__main__":
  print(wordCount('test2.txt'))
